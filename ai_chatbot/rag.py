from typing import Tuple, List
import re
from django.conf import settings
from openai import OpenAI
from .embeddings import compute_embeddings
from .vector_db import query_chunks
from .openai_client import get_openai_client

# Relevance threshold for cosine distance (lower = more similar).
# Hits with distance above this are considered off-topic from the KB.
KB_RELEVANCE_THRESHOLD = 0.55

# Broad academic subject keywords used to gate ALL queries (KB + general fallback)
ACADEMIC_KEYWORDS = [
    # General academics
    'exam', 'study', 'homework', 'syllabus', 'curriculum', 'assignment', 'lecture',
    'course', 'grade', 'academic', 'university', 'school', 'college', 'tutorial',
    'problem', 'practice', 'education', 'alpha', 'test', 'prep', 'assessment',
    'quiz', 'project', 'thesis', 'research', 'classroom', 'textbook', 'chapter',
    'subject', 'lesson', 'topic', 'concept', 'theory', 'principle', 'formula',
    'definition', 'difference between', 'example', 'solve', 'calculate', 'derive', 'prove',
    'summary', 'note', 'revision', 'mock', 'entrance', 'competitive', 'scholarship',
    # Quick-action chips / intent phrases
    'study material', 'study materials', 'research note', 'research notes',
    'question and answer', 'questions and answers', 'questions & answers',
    'q&a', 'q & a', 'q and a',
    'mcq', 'objective question', 'subjective question', 'descriptive',
    'help me study', 'help me learn', 'help me understand', 'explain me',
    'what should i study', 'how to study', 'learning material',
    'practice question', 'sample question', 'previous year', 'past paper',
    # Subject abbreviations (short inputs)
    'bio', 'phy', 'chem', 'sci', 'maths', 'eco', 'eng', 'cs', 'it',
    'geo', 'hist', 'pol', 'soc', 'psy', 'phi', 'comm', 'acct',

    # Mathematics
    'math', 'algebra', 'geometry', 'calculus', 'trigonometry', 'statistics',
    'probability', 'equation', 'matrix', 'vector', 'integral', 'derivative',
    'polynomial', 'theorem', 'proof', 'arithmetic', 'number', 'function',
    'graph', 'coordinate', 'set theory', 'logarithm', 'permutation', 'combination',

    # Science
    'physics', 'chemistry', 'biology', 'science', 'experiment', 'hypothesis',
    'atom', 'molecule', 'cell', 'organism', 'evolution', 'genetics', 'dna',
    'force', 'motion', 'energy', 'wave', 'optics', 'thermodynamics',
    'electricity', 'magnetism', 'reaction', 'element', 'compound', 'periodic table',
    'photosynthesis', 'ecosystem', 'anatomy', 'physiology', 'botany', 'zoology',

    # Computer Science
    'algorithm', 'programming', 'code', 'software', 'database', 'network',
    'data structure', 'operating system', 'compiler', 'machine learning',
    'artificial intelligence', 'python', 'java', 'html', 'css', 'javascript',
    'recursion', 'sorting', 'searching', 'complexity', 'binary', 'loop',
    'variable', 'function', 'class', 'object', 'inheritance', 'api',

    # Humanities & Social Sciences
    'history', 'geography', 'economics', 'civics', 'political science',
    'literature', 'english', 'grammar', 'essay', 'poetry', 'prose',
    'government', 'democracy', 'constitution', 'culture', 'society', 'language',
    'philosophy', 'psychology', 'sociology', 'anthropology', 'ethics', 'logic',
    'politics', 'election', 'parliament', 'legislation', 'policy',

    # General Knowledge (GK)
    'prime minister', 'president', 'capital', 'currency', 'population',
    'country', 'continent', 'nation', 'state', 'republic', 'kingdom',
    'invention', 'inventor', 'discovery', 'scientist', 'mathematician',
    'author', 'poet', 'novelist', 'founder', 'leader', 'ruler', 'dynasty',
    'independence', 'revolution', 'war', 'treaty', 'organisation', 'organization',
    'united nations', 'world bank', 'olympic', 'nobel', 'award', 'prize',
    'planet', 'solar system', 'space', 'astronomy', 'galaxy', 'universe',
    'mountain', 'river', 'ocean', 'desert', 'climate', 'environment',
    'general knowledge', 'gk', 'current affairs', 'world history',
    'national', 'international', 'global', 'flag', 'anthem', 'emblem',

    # Commerce & Business
    'accounting', 'finance', 'business', 'marketing', 'management', 'commerce',
    'balance sheet', 'profit', 'loss', 'tax', 'investment', 'economics',
    'supply', 'demand', 'market', 'entrepreneurship', 'trade',

    # Entrance Exams
    'jee', 'neet', 'cat', 'gre', 'gmat', 'sat', 'act', 'upsc', 'gate',
    'ielts', 'toefl', 'clat', 'cuet', 'cbse', 'icse', 'igcse',
]

# Keywords that immediately indicate a non-academic / off-topic request
NON_ACADEMIC_KEYWORDS = [
    # Entertainment / Cinema / Media — explicitly blocked
    'bollywood', 'tollywood', 'kollywood', 'mollywood',
    'box office', 'box office collection', 'movie review', 'film review',
    'ott release', 'web series', 'tv serial', 'tv show', 'reality show',
    'film star', 'movie star', 'item song', 'trailer review',
    'celebrity gossip', 'celebrity news', 'gossip',
    'best actor award', 'filmfare', 'iifa', 'oscar winner actor',
    # Lifestyle / Personal
    'recipe', 'food delivery', 'cooking video',
    'online shopping', 'buy product', 'sell product',
    'book flight', 'book hotel', 'travel itinerary',
    'dating advice', 'relationship advice',
    # Misc off-topic
    'joke', 'meme', 'whatsapp status', 'instagram reel', 'tiktok',
    'gaming walkthrough', 'cheat code',
    'weather forecast', 'sports score', 'cricket score', 'football score',
    'stock price', 'share price', 'stock market tip',
]

# Entertainment check used inside generic_patterns guard
_ENTERTAINMENT_SIGNALS = [
    r'\bbollywood\b', r'\btollywood\b', r'\bkollywood\b',
    r'\bfilm star\b', r'\bmovie star\b', r'\bactor\b', r'\bactress\b',
    r'\bbox office\b', r'\bmovie review\b', r'\bfilm review\b',
    r'\bweb series\b', r'\btv serial\b', r'\bitem song\b',
    r'\bfilmfare\b', r'\biifa\b', r'\bott\b',
]


def is_academic_question(text: str) -> bool:
    """Returns True if the question is related to academics, education, or general knowledge
    (geography, history, government, science, etc.) but NOT entertainment or cinema."""
    q = (text or '').lower()

    # Gate 1: Immediately reject known non-academic / off-topic keywords
    if any(k in q for k in NON_ACADEMIC_KEYWORDS):
        return False

    # Gate 2: Immediately reject entertainment/cinema even if question looks academic
    if any(re.search(ep, q) for ep in _ENTERTAINMENT_SIGNALS):
        return False

    # Gate 3: Accept clear academic/GK subject-matter keywords
    if any(k in q for k in ACADEMIC_KEYWORDS):
        return True

    # Gate 4: Accept by interrogative pattern (who/what/where/when/why/how...)
    generic_patterns = [
        r'\bwhat is\b', r'\bwhat are\b', r'\bwhat was\b', r'\bwhat were\b',
        r'\bwho is\b',  r'\bwho was\b',  r'\bwho are\b',  r'\bwho were\b',
        r'\bwho invented\b', r'\bwho discovered\b', r'\bwho founded\b',
        r'\bwhere is\b', r'\bwhere was\b', r'\bwhere are\b',
        r'\bwhen did\b', r'\bwhen was\b', r'\bwhen is\b',
        r'\bwhich is\b', r'\bwhich was\b', r'\bwhich country\b',
        r'\bhow does\b', r'\bhow do\b', r'\bhow to\b',
        r'\bhow many\b', r'\bhow much\b', r'\bhow long\b',
        r'\bwhy is\b', r'\bwhy are\b', r'\bwhy did\b', r'\bwhy was\b',
        r'\bexplain\b', r'\bdescribe\b', r'\bdefine\b',
        r'\bsummarise\b', r'\bsummarize\b', r'\bsolve\b',
        r'\bcalculate\b', r'\bderive\b', r'\bprove\b', r'\blist\b',
        r'\btell me about\b', r'\bgive me\b', r'\bname the\b',
        # Follow-up / continuation phrases
        r'\bmore detail\b', r'\bmore details\b', r'\bmore about\b',
        r'\belaborate\b', r'\btell me more\b',
        r'\bexplain more\b', r'\bexplain further\b', r'\bexplain again\b',
        r'\bgive more\b', r'\bwant more\b', r'\bneed more\b',
        r'\bcontinue\b', r'\bgo on\b', r'\bexpand on\b',
        r'\bin more detail\b', r'\bin detail\b',
    ]
    if any(re.search(p, q) for p in generic_patterns):
        return True

    return False


def _has_relevant_kb_hits(hits: list) -> bool:
    """Check whether any of the KB hits are above the relevance threshold."""
    if not hits:
        return False
    # hits are sorted by distance ascending (most similar first)
    best_distance = hits[0].get('distance', 1.0)
    return best_distance <= KB_RELEVANCE_THRESHOLD


def sanitize_response(text: str) -> str:
    """Remove references to external AI systems from the response."""
    if not text:
        return text
    text = re.sub(r'(?i)\bopenai\b', 'Alpha AI', text)
    text = re.sub(r'(?i)\bchatgpt\b', 'Alpha AI', text)
    text = re.sub(r'(?i)\bgpt-\d+\b', 'Alpha AI', text)
    text = re.sub(r'(?i)\bas of my last (knowledge )?update(?: in [A-Za-z0-9 ,]+)?,?\s*', '', text)
    text = re.sub(r'(?i)\bas of my knowledge cutoff(?: in [A-Za-z0-9 ,]+)?,?\s*', '', text)
    return text


def strip_prompt_injections(text: str) -> str:
    """Remove common prompt-injection patterns from user input."""
    if not text:
        return text
    patterns = [
        r'(?i)ignore (all )?previous (instructions|prompts)',
        r'(?i)forget (all )?previous (instructions|prompts)',
        r'(?i)disregard (all )?previous (instructions|prompts)',
        r'(?i)ignore these instructions',
        r'(?i)you are now',
        r'(?i)role:\s*',
        r'(?i)system:\s*',
        r'(?i)assistant:\s*',
    ]
    for p in patterns:
        text = re.sub(p, '', text)
    # strip embedded code blocks that may carry hidden instructions
    text = re.sub(r'```[\s\S]*?```', '', text)
    if len(text) > 2000:
        text = text[:2000]
    return text.strip()


# Number of previous Q-A exchanges to include as conversation context
CONVERSATION_HISTORY_WINDOW = 6  # last 6 turns (= 12 messages)


def _call_llm(
    client: OpenAI,
    system_prompt: str,
    user_message: str,
    max_tokens: int,
    history: List[dict] = None,
):
    """Helper: call OpenAI ChatCompletion and return (answer, tokens_used).

    Args:
        history: Optional list of prior conversation turns in OpenAI message format:
                 [{'role': 'user', 'content': '...'}, {'role': 'assistant', 'content': '...'}, ...]
                 Injected between the system prompt and the current user_message.
    """
    messages = [{'role': 'system', 'content': system_prompt}]
    if history:
        messages.extend(history)
    messages.append({'role': 'user', 'content': user_message})

    resp = client.chat.completions.create(
        model=getattr(settings, 'AI_CHAT_MODEL', 'gpt-4o-mini'),
        messages=messages,
        temperature=0.7,
        max_tokens=max_tokens,
    )
    answer = resp.choices[0].message.content.strip()
    tokens_used = resp.usage.total_tokens if resp.usage else 0
    return answer, tokens_used


def _prepare_chat_request(
    question: str,
    top_k: int = 5,
    history: List[dict] = None,
) -> dict:
    """Build the LLM request payload shared by regular and streaming chat."""
    cleaned = strip_prompt_injections(question)

    if history:
        q_lower = cleaned.lower()
        is_blocked = (
            any(k in q_lower for k in NON_ACADEMIC_KEYWORDS)
            or any(re.search(ep, q_lower) for ep in _ENTERTAINMENT_SIGNALS)
        )
    else:
        is_blocked = not is_academic_question(cleaned)

    if is_blocked:
        return {
            'blocked_answer': (
                "Hmm, that one's a bit outside what I can help with! "
                "I'm here for studies, subjects, and general knowledge, "
                "so ask me anything along those lines."
            ),
            'sources': [],
            'tokens_used': 0,
        }

    try:
        q_emb = compute_embeddings([cleaned])[0]
    except Exception:
        q_emb = None

    hits = []
    if q_emb is not None:
        try:
            hits = query_chunks(q_emb, top_k=top_k)
        except Exception:
            hits = []

    token_limit = min(getattr(settings, 'AI_MAX_RESPONSE_TOKENS', 1024), 2048)

    if _has_relevant_kb_hits(hits):
        context_parts = []
        sources = []
        for hit in hits:
            if hit.get('distance', 1.0) > KB_RELEVANCE_THRESHOLD:
                continue
            meta = hit.get('metadata') or {}
            source = (
                meta.get('title') or
                meta.get('source') or
                meta.get('document_id') or
                'Alpha Knowledge Base'
            )
            sources.append(source)
            snippet = hit.get('chunk_text', '')
            if len(snippet) > 1500:
                snippet = snippet[:1500] + '...'
            context_parts.append(f"[{source}]:\n{snippet}")

        context = "\n\n---\n\n".join(context_parts)
        if len(context) > 4000:
            context = context[:4000] + '\n...'

        system_prompt = (
            "You are Alpha AI - a knowledgeable, warm tutor who helps students learn. "
            "Use the provided knowledge-base material to answer the question. "
            "Start with the core idea in plain language, then add helpful explanation. "
            "If the material only partly covers the question, say that briefly. "
            "Do not make up facts that are not in the material. "
            "Do not mention OpenAI, ChatGPT, knowledge cutoffs, last updates, or any other AI system."
        )
        user_message = (
            f"KNOWLEDGE BASE CONTEXT:\n{context}\n\n"
            f"STUDENT QUESTION:\n{cleaned}\n\n"
            f"ANSWER:"
        )
        sources = list(dict.fromkeys(sources))
    else:
        system_prompt = (
            "You are Alpha AI - a knowledgeable, warm tutor who helps students learn. "
            "Answer from your general academic knowledge because the question was not found "
            "in the uploaded documents. Keep the response educational and useful. "
            "You can cover school subjects, academic topics, general knowledge, and entrance exams. "
            "Do not help with cinema, celebrity gossip, shopping, travel booking, dating advice, memes, "
            "or other non-academic topics. Do not mention OpenAI, ChatGPT, knowledge cutoffs, "
            "last updates, or any other AI system. "
            "End every valid answer with: '(Source: Alpha Academic Knowledge Base)'"
        )
        user_message = f"STUDENT QUESTION:\n{cleaned}\n\nANSWER:"
        sources = ['General Academic Knowledge']

    messages = [{'role': 'system', 'content': system_prompt}]
    if history:
        messages.extend(history)
    messages.append({'role': 'user', 'content': user_message})

    return {
        'client': get_openai_client(),
        'messages': messages,
        'max_tokens': token_limit,
        'sources': sources,
    }


def stream_retrieve_and_answer(
    question: str,
    top_k: int = 5,
    history: List[dict] = None,
):
    """Yield chat response events as soon as OpenAI streams tokens."""
    request_data = _prepare_chat_request(
        question,
        top_k=top_k,
        history=history,
    )

    if 'blocked_answer' in request_data:
        answer = request_data['blocked_answer']
        yield {'type': 'delta', 'text': answer}
        yield {
            'type': 'done',
            'answer': answer,
            'sources': request_data['sources'],
            'tokens_used': request_data['tokens_used'],
        }
        return

    full_answer = []
    tokens_used = 0

    try:
        stream = request_data['client'].chat.completions.create(
            model=getattr(settings, 'AI_CHAT_MODEL', 'gpt-4o-mini'),
            messages=request_data['messages'],
            temperature=0.7,
            max_tokens=request_data['max_tokens'],
            stream=True,
            stream_options={'include_usage': True},
        )

        for chunk in stream:
            if getattr(chunk, 'usage', None):
                tokens_used = chunk.usage.total_tokens or tokens_used
            if not chunk.choices:
                continue
            delta = chunk.choices[0].delta
            text = getattr(delta, 'content', None)
            if not text:
                continue
            full_answer.append(text)
            yield {'type': 'delta', 'text': text}

    except Exception:
        yield {'type': 'error', 'error': "I'm having trouble answering right now. Please try again shortly."}
        return

    answer = sanitize_response(''.join(full_answer).strip())
    if not answer:
        answer = "I couldn't generate an answer right now."

    yield {
        'type': 'done',
        'answer': answer,
        'sources': request_data['sources'],
        'tokens_used': tokens_used,
    }


def retrieve_and_answer(
    question: str,
    top_k: int = 5,
    history: List[dict] = None,
) -> Tuple[str, List[str], int]:
    """
    Two-path RAG pipeline with optional conversation history.

    Path A — Knowledge Base:
        If the uploaded knowledge-base documents contain relevant context,
        answer grounded exclusively in those documents.

    Path B — General Academic / GK Fallback:
        If the knowledge-base has no sufficiently relevant content,
        fall back to OpenAI general knowledge, scoped to academics and GK.

    Non-academic / entertainment questions are rejected in both paths.

    Args:
        question: The current student question.
        top_k:    Number of KB chunks to retrieve.
        history:  Prior conversation turns as a list of OpenAI-format message dicts
                  [{'role': 'user', 'content': '...'}, {'role': 'assistant', 'content': '...'}, ...].
                  When provided, the LLM receives the full conversation context so it can
                  refer back to earlier questions, clarify follow-ups, and maintain coherence.

    Returns: (answer_text, [source_labels], tokens_used)
    """
    # ── 1. Sanitise & scope-check ──────────────────────────────────────────
    cleaned = strip_prompt_injections(question)

    # When there's active conversation history, only block explicit non-academic
    # content — follow-up messages like "tell me more" / "I want more detail"
    # don't contain academic keywords but are clearly continuations.
    if history:
        _q = cleaned.lower()
        is_blocked = (
            any(k in _q for k in NON_ACADEMIC_KEYWORDS)
            or any(re.search(ep, _q) for ep in _ENTERTAINMENT_SIGNALS)
        )
    else:
        is_blocked = not is_academic_question(cleaned)

    if is_blocked:
        return (
            "Hmm, that one's a bit outside what I can help with! "
            "I'm here for studies, subjects, and general knowledge — "
            "so feel free to ask me anything along those lines and I'll do my best.",
            [], 0
        )

    # ── 2. Compute query embedding ─────────────────────────────────────────
    try:
        q_emb = compute_embeddings([cleaned])[0]
    except Exception:
        q_emb = None

    hits = []
    if q_emb is not None:
        try:
            hits = query_chunks(q_emb, top_k=top_k)
        except Exception:
            hits = []

    client = get_openai_client()
    max_tokens = min(getattr(settings, 'AI_MAX_RESPONSE_TOKENS', 1024), 2048)

    # ── 3. PATH A: Knowledge-Base answer ──────────────────────────────────
    if _has_relevant_kb_hits(hits):
        context_parts = []
        sources = []
        for h in hits:
            # skip low-relevance hits even within a partially relevant result set
            if h.get('distance', 1.0) > KB_RELEVANCE_THRESHOLD:
                continue
            meta   = h.get('metadata') or {}
            source = (
                meta.get('title') or
                meta.get('source') or
                meta.get('document_id') or
                'Alpha Knowledge Base'
            )
            sources.append(source)
            snippet = h.get('chunk_text', '')
            if len(snippet) > 1500:
                snippet = snippet[:1500] + '...'
            context_parts.append(f"[{source}]:\n{snippet}")

        context = "\n\n---\n\n".join(context_parts)
        if len(context) > 4000:
            context = context[:4000] + '\n...'

        system_prompt = (
            "You are Alpha AI — a knowledgeable, warm tutor who genuinely loves helping students learn. "
            "You have access to specific study material from Alpha's knowledge base, and you'll use it to answer the question below.\n\n"

            "Personality & tone:\n"
            "Talk like a real person, not a textbook. Be encouraging, natural, and clear. "
            "Vary your sentence structure — sometimes short and punchy, sometimes a fuller explanation. "
            "It's fine to say things like 'Great question!', 'So here's the thing...', 'Think of it this way...' or 'Honestly, a lot of students trip up on this part.' "
            "Never sound robotic or like you're reading from a list of rules.\n\n"

            "If a student spells something wrong or asks vaguely, quietly figure out what they mean and answer — don't point out the mistake.\n\n"

            "Special requests to handle naturally:\n"
            "- If someone asks for 'study materials', 'notes', or 'learning material': get a little excited about it! "
            "Say something like 'Oh nice, let me show you some solid starting points!' then suggest 3–4 useful topics with brief descriptions, "
            "and ask which subject they'd like to go deeper into.\n"
            "- If someone asks about 'research notes', 'research topics', or 'thesis help': step into mentor mode. "
            "Share 4–5 genuinely interesting research directions with a line about each, "
            "then ask what subject and specific angle they're exploring so you can give focused guidance.\n"
            "- If someone asks for 'q&a', 'questions & answers', 'mcq', or 'practice questions': be ready and warm. "
            "Say you're all set to help, ask them to share their question, and mention you can do MCQ, descriptive, or both. "
            "By default give both — MCQ version first, then a proper explanation.\n\n"

            "In an ongoing conversation, always pick up exactly where things left off. "
            "If someone says 'tell me more', 'explain further', or 'I want more detail' — just continue from the previous topic naturally. "
            "Use phrases like 'Building on what we just covered...' or 'Right, so going deeper into that...' "
            "Never ask them to repeat themselves.\n\n"

            "When answering from the knowledge-base material:\n"
            "Start with the core idea in plain language, then build up. Explain WHY and HOW, not just WHAT. "
            "Bring in a real-world example or analogy that makes it click. "
            "If there's a common mistake students make here, gently flag it. "
            "If the material only partly covers the question, answer what you can and honestly say something like "
            "'Beyond this, your textbook or teacher would have the full picture.'\n\n"

            "Do NOT make up facts that aren't in the material below. Do NOT mention OpenAI, ChatGPT, knowledge cutoffs, last updates, or any other AI system."
        )
        user_message = (
            f"KNOWLEDGE BASE CONTEXT:\n{context}\n\n"
            f"STUDENT QUESTION:\n{cleaned}\n\n"
            f"ANSWER:"
        )

        try:
            answer, tokens_used = _call_llm(client, system_prompt, user_message, max_tokens, history=history)
        except Exception:
            answer, tokens_used = "", 0

        answer = sanitize_response(answer)
        if answer:
            return (answer, list(dict.fromkeys(sources)), tokens_used)

    # ── 4. PATH B: General Academic Fallback (OpenAI knowledge) ───────────
    # Knowledge base had no relevant content — answer from general
    # academic knowledge, strictly limited to syllabus / educational topics.
    system_prompt = (
        "You are Alpha AI — a knowledgeable, warm tutor who genuinely enjoys helping students learn. "
        "Think of yourself as that one really helpful senior student or teacher who explains things in a way that actually makes sense.\n\n"

        "Personality & tone:\n"
        "Talk naturally, like a real person. Be encouraging and enthusiastic about the subject. "
        "Vary how you say things — sometimes a quick snappy line, sometimes a richer explanation. "
        "Feel free to say things like 'Okay so here's what's really going on here...', 'Think of it like this...', "
        "'This one trips up a lot of students, so let me be clear about it.' "
        "Never sound like a corporate FAQ or a robot listing instructions.\n\n"

        "If someone spells something wrong or asks vaguely, just figure out what they mean and answer — "
        "don't mention the spelling mistake or ask for clarification unless it's truly ambiguous.\n\n"

        "Special requests to handle warmly and naturally:\n"
        "- 'Study materials' / 'notes' / 'learning material': get enthusiastic! Say something like "
        "'Oh, great — let me point you to some solid starting points!' then suggest 3–4 useful topics "
        "with a short description of each, and ask which subject they'd like to go deeper into.\n"
        "- 'Research notes' / 'research topics' / 'thesis help': step into research-mentor mode. "
        "Offer 4–5 genuinely interesting research directions with a line on why each is worth exploring, "
        "then ask what subject and specific angle they're working on.\n"
        "- 'Q&A' / 'questions & answers' / 'MCQ' / 'practice questions': be ready and welcoming. "
        "Tell them you're set to help, invite them to share the question, and mention you can do MCQ, "
        "descriptive, or both. By default, give both — MCQ first, then a proper explanation.\n\n"

        "In an ongoing conversation, always pick up right where things left off. "
        "If someone says 'tell me more', 'explain further', or 'I want more detail' — just keep going from the previous topic. "
        "Use natural phrases like 'Right, building on that...', 'So going deeper...' "
        "Never make them repeat themselves.\n\n"

        "This question wasn't found in the uploaded documents, so answer from your general academic knowledge. "
        "You can cover: Maths, Physics, Chemistry, Biology, Computer Science, English Literature, Grammar, "
        "Environmental Science, History, Geography, Civics, Political Science, Economics, Business, "
        "Accounting, Philosophy, Psychology, Sociology, General Knowledge (capitals, currencies, inventions, "
        "Nobel prizes, space, constitutions, organisations), and entrance exams (JEE, NEET, UPSC, CAT, GRE, GATE, IELTS, etc.).\n\n"

        "For every answer:\n"
        "Start with the core idea in plain language, then build depth. "
        "Always explain WHY and HOW — not just WHAT. "
        "Use a real-world example or analogy that makes it click. "
        "If there's a common misconception, flag it naturally: 'A lot of people think X, but actually...' "
        "For history/geography/GK: give context, significance, and connections, not just dry facts. "
        "For maths/science: show step-by-step working with brief explanations at each step. "
        "Use formatting (numbered steps, bullet points, short sections) when it genuinely helps — "
        "but don't structure everything into rigid sections if a flowing explanation reads better.\n\n"

        "What you won't help with: Bollywood/Hollywood/cinema, film reviews, box office, OTT/web series, "
        "celebrity gossip, TV shows, food recipes, online shopping, travel booking, dating advice, memes. "
        "If something like that comes up, just say warmly: "
        "'Hmm, that one's outside my zone — I'm all about studies and learning! "
        "Got anything educational you'd like help with?'\n\n"

        "Do NOT mention OpenAI, ChatGPT, knowledge cutoffs, last updates, or any other AI system.\n"
        "End every valid answer with: '(Source: Alpha Academic Knowledge Base)'"
    )
    user_message = f"STUDENT QUESTION:\n{cleaned}\n\nANSWER:"

    try:
        answer, tokens_used = _call_llm(client, system_prompt, user_message, max_tokens, history=history)
    except Exception:
        return ("I'm having trouble answering right now. Please try again shortly.", [], 0)

    answer = sanitize_response(answer)
    if not answer:
        return (
            "I couldn't find anything in Alpha's knowledge base and couldn't generate a general answer.",
            [], 0
        )

    return (answer, ['General Academic Knowledge'], tokens_used)


# ─────────────────────────────────────────────────────────────────────────────
#  RESEARCH / THESIS ASSISTANT
# ─────────────────────────────────────────────────────────────────────────────

RESEARCH_STRUCTURES = {
    'overview':       "Provide a comprehensive academic overview of the topic.",
    'thesis':         "Help structure a thesis for this topic with: Introduction, Literature Review, Methodology, Analysis, and Conclusion sections.",
    'literature':     "Summarise key concepts, theories, and existing knowledge on this topic as a Literature Review.",
    'methodology':    "Suggest appropriate research methodologies and data-collection techniques for studying this topic.",
    'analysis':       "Analyse the topic critically, discussing multiple perspectives, evidence, and counter-arguments.",
    'conclusion':     "Write a well-reasoned academic conclusion for this research topic.",
    'bibliography':   "List key academic concepts and suggest reference categories (books, journals, articles) relevant to this topic.",
}


def research_and_answer(
    query: str,
    topic: str = '',
    research_type: str = 'overview',
) -> Tuple[str, List[str], int]:
    """
    Research / thesis assistant pipeline.

    1. Searches the knowledge base for relevant content.
    2. Augments the answer with general academic knowledge.
    3. Returns a detailed, structured academic response.

    Args:
        query        – The student's research question.
        topic        – Optional topic label (e.g. "Climate Change").
        research_type– One of: overview, thesis, literature, methodology,
                       analysis, conclusion, bibliography.

    Returns: (answer_text, [sources], tokens_used)
    """
    cleaned = strip_prompt_injections(query)
    if not is_academic_question(cleaned):
        return (
            "Research assistance is available for academic and educational topics only.",
            [], 0
        )

    # ── 1. Embed & search KB ───────────────────────────────────────────────
    kb_context = ""
    sources: List[str] = []
    try:
        q_emb = compute_embeddings([cleaned])[0]
        hits = query_chunks(q_emb, top_k=8)
        relevant = [h for h in hits if h.get('distance', 1.0) <= KB_RELEVANCE_THRESHOLD]
        for h in relevant:
            meta = h.get('metadata') or {}
            src = meta.get('title') or meta.get('source') or 'Alpha Knowledge Base'
            sources.append(src)
            snippet = h.get('chunk_text', '')[:2000]
            kb_context += f"\n[{src}]:\n{snippet}\n"
    except Exception:
        pass

    research_instruction = RESEARCH_STRUCTURES.get(research_type, RESEARCH_STRUCTURES['overview'])
    topic_label = topic.strip() if topic else cleaned[:80]
    max_tokens = min(getattr(settings, 'AI_MAX_RESPONSE_TOKENS', 512), 1024) * 2  # allow longer for research
    max_tokens = min(max_tokens, 2048)

    system_prompt = (
        "You are Alpha AI Research Assistant — an expert academic tutor helping students "
        "with research papers, thesis writing, and in-depth subject study.\n\n"
        "RULES:\n"
        "1. Provide academically rigorous, well-structured responses.\n"
        "2. Use headings, bullet points, and numbered lists where appropriate.\n"
        "3. Cite reasoning and, where relevant, suggest academic sources (author, year style).\n"
        "4. Restrict your response to educational and academic content only.\n"
        "5. Do NOT discuss entertainment, politics, personal advice, or commercial topics.\n"
        "6. Do NOT reference OpenAI, ChatGPT, or any external AI system by name.\n"
        f"7. TASK: {research_instruction}"
    )

    kb_section = (
        f"\n\nKNOWLEDGE BASE CONTEXT (use this first):\n{kb_context.strip()}"
        if kb_context else
        "\n\n(No specific documents found in the knowledge base for this topic — use your academic knowledge.)"
    )

    user_message = (
        f"RESEARCH TOPIC: {topic_label}\n\n"
        f"STUDENT QUERY: {cleaned}"
        f"{kb_section}\n\n"
        f"Please provide a detailed, structured academic response."
    )

    client = get_openai_client()
    try:
        answer, tokens_used = _call_llm(client, system_prompt, user_message, max_tokens)
    except Exception as e:
        return (f"Unable to generate research response at this time. ({e})", [], 0)

    answer = sanitize_response(answer)
    if not sources:
        sources = ['General Academic Knowledge']

    return (answer, list(dict.fromkeys(sources)), tokens_used)


# ─────────────────────────────────────────────────────────────────────────────
#  MOCK EXAM GENERATOR
# ─────────────────────────────────────────────────────────────────────────────

import json as _json


def generate_mock_exam(
    subject: str,
    topic: str,
    difficulty: str = 'medium',
    question_type: str = 'mcq',
    num_questions: int = 10,
) -> Tuple[List[dict], int]:
    """
    Generate a mock exam using OpenAI and the knowledge base.

    Args:
        subject       – e.g. "Physics", "Mathematics"
        topic         – e.g. "Newton's Laws of Motion"
        difficulty    – easy | medium | hard | mixed
        question_type – mcq | short_answer | true_false | mixed
        num_questions – number of questions to generate (1-30)

    Returns: (questions_list, tokens_used)
        questions_list is a list of dicts, each containing:
            {
              "question_number": int,
              "question_type":   str,
              "question_text":   str,
              "options":         list[str],  # MCQ options, else []
              "correct_answer":  str,
              "explanation":     str,
              "marks":           int,
            }
    """
    # ── Validate ──────────────────────────────────────────────────────────
    num_questions = max(1, min(int(num_questions), 30))
    if not subject or not topic:
        return [], 0

    # ── 1. Search KB for context ──────────────────────────────────────────
    kb_context = ""
    try:
        q_emb = compute_embeddings([f"{subject} {topic}"])[0]
        hits = query_chunks(q_emb, top_k=6)
        relevant = [h for h in hits if h.get('distance', 1.0) <= KB_RELEVANCE_THRESHOLD]
        for h in relevant:
            kb_context += h.get('chunk_text', '')[:600] + "\n"
    except Exception:
        pass

    # ── 2. Build question-type instructions ───────────────────────────────
    if question_type == 'mcq':
        type_instruction = (
            "All questions must be Multiple Choice Questions (MCQ) with exactly 4 options "
            "labelled A, B, C, D. Indicate the correct option letter."
        )
    elif question_type == 'short_answer':
        type_instruction = (
            "All questions must be Short Answer questions requiring a 1-3 sentence response. "
            "Provide a model answer."
        )
    elif question_type == 'true_false':
        type_instruction = (
            "All questions must be True/False statements. "
            "State whether the answer is TRUE or FALSE with a brief explanation."
        )
    elif question_type == 'mixed':
        type_instruction = (
            f"Mix the question types: approximately {num_questions // 3 or 1} MCQ, "
            f"{num_questions // 3 or 1} Short Answer, and {num_questions - 2*(num_questions // 3) or 1} True/False."
        )
    else:
        type_instruction = "Use MCQ format."

    kb_section = (
        f"\n\nRELEVANT STUDY CONTENT FROM KNOWLEDGE BASE:\n{kb_context.strip()}"
        if kb_context
        else "\n\n(Use your academic knowledge for this subject and topic.)"
    )

    system_prompt = (
        "You are Alpha AI Exam Generator — an expert educational assessment creator.\n"
        "You generate high-quality mock exam questions for students.\n\n"
        "STRICT OUTPUT FORMAT — respond with ONLY a valid JSON array, no markdown, no extra text:\n"
        "[\n"
        "  {\n"
        '    "question_number": 1,\n'
        '    "question_type": "mcq",\n'
        '    "question_text": "...",\n'
        '    "options": ["A. ...", "B. ...", "C. ...", "D. ..."],\n'
        '    "correct_answer": "A",\n'
        '    "explanation": "...",\n'
        '    "marks": 1\n'
        "  }\n"
        "]\n\n"
        "For short_answer questions: options = [], correct_answer = model answer string.\n"
        "For true_false questions: options = ['True', 'False'], correct_answer = 'True' or 'False'.\n"
        "Marks: easy=1, medium=2, hard=3 per question."
    )

    user_message = (
        f"Generate exactly {num_questions} questions for the following mock exam.\n\n"
        f"SUBJECT: {subject}\n"
        f"TOPIC: {topic}\n"
        f"DIFFICULTY: {difficulty}\n"
        f"QUESTION TYPE: {type_instruction}"
        f"{kb_section}\n\n"
        f"Return ONLY the JSON array with {num_questions} question objects."
    )

    client = get_openai_client()
    max_tokens = min(300 * num_questions, 4096)

    try:
        resp = client.chat.completions.create(
            model=getattr(settings, 'AI_CHAT_MODEL', 'gpt-4o-mini'),
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user',   'content': user_message},
            ],
            temperature=0.5,
            max_tokens=max_tokens,
            response_format={"type": "json_object"},
        )
    except Exception as e:
        # Fallback: try without response_format (older models)
        try:
            resp = client.chat.completions.create(
                model=getattr(settings, 'AI_CHAT_MODEL', 'gpt-4o-mini'),
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user',   'content': user_message},
                ],
                temperature=0.5,
                max_tokens=max_tokens,
            )
        except Exception as e2:
            return [], 0

    tokens_used = resp.usage.total_tokens if resp.usage else 0
    raw = resp.choices[0].message.content.strip()

    # ── 3. Parse JSON ─────────────────────────────────────────────────────
    try:
        parsed = _json.loads(raw)
        # model may wrap in {"questions": [...]}
        if isinstance(parsed, dict):
            for key in ('questions', 'exam', 'items', 'data'):
                if key in parsed and isinstance(parsed[key], list):
                    parsed = parsed[key]
                    break
            else:
                # single-key dict
                parsed = list(parsed.values())[0] if parsed else []
        if not isinstance(parsed, list):
            return [], tokens_used
    except Exception:
        return [], tokens_used

    # ── 4. Normalise each question ────────────────────────────────────────
    questions: List[dict] = []
    for i, q in enumerate(parsed, start=1):
        if not isinstance(q, dict):
            continue
        qt = str(q.get('question_type', question_type if question_type != 'mixed' else 'mcq')).lower()
        if qt not in ('mcq', 'short_answer', 'true_false'):
            qt = 'mcq'
        questions.append({
            'question_number': q.get('question_number', i),
            'question_type':   qt,
            'question_text':   str(q.get('question_text', '')).strip(),
            'options':         q.get('options', []) if isinstance(q.get('options'), list) else [],
            'correct_answer':  str(q.get('correct_answer', '')).strip(),
            'explanation':     str(q.get('explanation', '')).strip(),
            'marks':           int(q.get('marks', 1)),
        })

    return questions, tokens_used

