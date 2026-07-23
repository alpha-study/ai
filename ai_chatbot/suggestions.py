import re
from typing import List


QUESTION_PREFIX_RE = re.compile(
    r'^(who|what|where|when|why|how|which|tell me|give me|explain|define)\s+',
    re.IGNORECASE,
)


def _title_case_topic(text: str) -> str:
    small_words = {'a', 'an', 'and', 'as', 'at', 'by', 'for', 'in', 'of', 'on', 'or', 'the', 'to'}
    words = re.findall(r"[A-Za-z0-9']+", text)
    if not words:
        return ''
    titled = []
    for index, word in enumerate(words):
        lower = word.lower()
        titled.append(lower if index and lower in small_words else lower.capitalize())
    return ' '.join(titled)


def _extract_question_topic(question: str) -> str:
    text = (question or '').strip().lower()
    text = re.sub(r'[?!.]+$', '', text)
    text = QUESTION_PREFIX_RE.sub('', text).strip()
    text = re.sub(r'^(is|are|was|were|the)\s+', '', text).strip()
    return _title_case_topic(text)


def _extract_named_entity(answer: str) -> str:
    text = re.sub(r'\(Source:[^)]+\)', '', answer or '')
    patterns = [
        r'\b(?:is|was|are|were)\s+([A-Z][A-Za-z.]+(?:\s+[A-Z][A-Za-z.]+){0,3})\b',
        r'\b([A-Z][A-Za-z.]+(?:\s+[A-Z][A-Za-z.]+){1,3})\s+(?:is|was|has|served)\b',
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            entity = match.group(1).strip()
            if entity.lower() not in {'alpha ai', 'source alpha'}:
                return entity
    return ''


def _is_political_topic(topic: str, question: str) -> bool:
    text = f'{topic} {question}'.lower()
    return any(word in text for word in (
        'prime minister', 'president', 'minister', 'politic', 'government',
        'parliament', 'party', 'election', 'leader'
    ))


def build_followup_suggestions(question: str, answer: str, sources: List[str] = None) -> List[str]:
    """Build lightweight follow-up prompts for interactive chat chips."""
    topic = _extract_question_topic(question)
    entity = _extract_named_entity(answer)
    focus = entity or topic or 'this topic'

    if _is_political_topic(topic, question):
        suggestions = [
            f"Want to know more about {focus}?",
            f"Want a timeline of {focus}'s political career?",
            f"Want to understand the role of {topic or 'this office'}?",
        ]
    else:
        suggestions = [
            f"Want a simpler explanation of {focus}?",
            f"Want to go deeper into {focus}?",
            f"Want examples or practice questions on {focus}?",
        ]

    return list(dict.fromkeys(suggestions))[:3]
