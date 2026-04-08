# Alpha AI Chatbot — Frontend Developer Guide

> **Platform:** Alpha Educational AI Chatbot  
> **Backend:** Django 6 + Django REST Framework  
> **Auth:** JWT (SimpleJWT)  
> **Base URL (dev):** `http://localhost:8000`  
> **Base URL (prod):** `https://your-production-domain.com`

---

## Table of Contents

1. [Authentication Flow](#1-authentication-flow)
2. [API Base URL & Headers](#2-api-base-url--headers)
3. [Token Management](#3-token-management)
4. [Complete API Reference](#4-complete-api-reference)
   - [Auth Endpoints](#41-auth-endpoints)
   - [Chat](#42-chat)
   - [Research & Thesis](#43-research--thesis)
   - [Mock Exam](#44-mock-exam)
   - [Admin — Documents](#45-admin--document-management)
5. [Data Models (TypeScript Types)](#5-data-models-typescript-types)
6. [Error Handling](#6-error-handling)
7. [Feature Implementation Guides](#7-feature-implementation-guides)
   - [Chat with Conversation History](#71-chat-with-conversation-history)
   - [Session Sidebar](#72-session-sidebar)
   - [Research Assistant](#73-research-assistant)
   - [Mock Exam Builder & Viewer](#74-mock-exam-builder--viewer)
8. [Rendering AI Responses (Markdown)](#8-rendering-ai-responses-markdown)
9. [File Upload (Admin)](#9-file-upload-admin)
10. [Suggested Screen Architecture](#10-suggested-screen-architecture)
11. [Edge Cases & UX Notes](#11-edge-cases--ux-notes)

---

## 1. Authentication Flow

The backend uses **JWT (JSON Web Token)** authentication — no session cookies.

### Flow Diagram

```
User submits login form
        │
        ▼
POST /api/token/  {username, password}
        │
        ▼
Server returns { access, refresh }
        │
        ├── Store access token  (memory or sessionStorage — expires in 1 hour)
        └── Store refresh token (localStorage — expires in 7 days)
        │
        ▼
Attach to every API call:
  Authorization: Bearer <access_token>
        │
        ▼
On 401 response → POST /api/token/refresh/ → get new access token
        │
        ▼
If refresh also fails → redirect to login
```

### Token Lifetimes

| Token   | Lifetime | Storage recommendation |
|---------|----------|------------------------|
| access  | 1 hour   | Memory / sessionStorage |
| refresh | 7 days   | localStorage (encrypted if possible) |

---

## 2. API Base URL & Headers

```js
// config/api.js
export const BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Every authenticated request must include:
const authHeaders = (token) => ({
  'Content-Type': 'application/json',
  'Authorization': `Bearer ${token}`,
});
```

> **CORS:** The backend has `CORS_ALLOW_ALL_ORIGINS = True` — all frontend origins are accepted. No additional backend configuration needed during development or initial deployment.

---

## 3. Token Management

### Recommended Axios Interceptor Setup

```js
// api/axiosInstance.js
import axios from 'axios';

const api = axios.create({ baseURL: BASE_URL });

// Attach access token to every request
api.interceptors.request.use((config) => {
  const token = sessionStorage.getItem('access_token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Auto-refresh on 401
api.interceptors.response.use(
  (res) => res,
  async (error) => {
    const original = error.config;
    if (error.response?.status === 401 && !original._retry) {
      original._retry = true;
      try {
        const refresh = localStorage.getItem('refresh_token');
        const { data } = await axios.post(`${BASE_URL}/api/token/refresh/`, { refresh });
        sessionStorage.setItem('access_token', data.access);
        original.headers.Authorization = `Bearer ${data.access}`;
        return api(original);
      } catch {
        // Refresh failed — force logout
        localStorage.clear();
        sessionStorage.clear();
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export default api;
```

---

## 4. Complete API Reference

### 4.1 Auth Endpoints

#### `POST /api/token/` — Login

```
Body:
  username  string  required
  password  string  required

Response 200:
  access   string   JWT access token (1 hour)
  refresh  string   JWT refresh token (7 days)

Response 401:
  detail   "No active account found with the given credentials"
```

#### `POST /api/token/refresh/` — Refresh

```
Body:
  refresh  string  required  (the refresh token)

Response 200:
  access   string   new JWT access token

Response 401:
  detail   "Token is invalid or expired"
```

#### `POST /api/token/verify/` — Verify

```
Body:
  token   string  required  (any JWT token to validate)

Response 200:  {}  (empty — token is valid)
Response 401:  { detail, code: "token_not_valid" }
```

---

### 4.2 Chat

#### `POST /api/chatbot/ask/` — Send a message  
**Auth required:** ✅ Bearer token

```
Body:
  session_id  UUID/string  required
              → Generate a UUID v4 on the frontend. Reuse the same
                ID for all messages in one conversation.
  question    string       required
              → The student's question.

Response 200:
  answer       string   AI answer (Markdown formatted)
  sources      string[] Source labels (document titles or "Alpha Academic Knowledge Base")
  tokens_used  number   Tokens consumed by this request

Response 200 (rejected — non-academic):
  answer       "I can only help with academic and study-related questions..."
  sources      []
  tokens_used  0
```

> **Conversation Memory:** The backend automatically includes the last 6 exchanges from `session_id` as context. No extra work needed from the frontend — just use a consistent `session_id`.

---

#### `GET /api/chatbot/chat/sessions/` — List sessions  
**Auth required:** ✅

```
Response 200:
  count     number
  sessions  ChatSession[]

ChatSession:
  id             string (UUID)
  created_at     ISO 8601 datetime
  updated_at     ISO 8601 datetime
  message_count  number  (count of AI responses)
  last_message   string | null  (first 120 chars of last user message)
```

---

#### `GET /api/chatbot/history/{session_id}/` — Full session history  
**Auth required:** ✅

```
URL param:
  session_id  UUID

Response 200:
  session_id     string
  created_at     ISO 8601 datetime
  updated_at     ISO 8601 datetime
  message_count  number
  messages       ChatMessage[]

ChatMessage:
  id           string (UUID)
  role         "user" | "assistant"
  message      string   (the question — present on both roles)
  response     string | null  (AI answer — only on role="assistant")
  tokens_used  number | null  (only on role="assistant")
  created_at   ISO 8601 datetime

Response 404:
  { detail: "No ChatSession matches the given query." }
```

> **Note:** Both `user` and `assistant` messages are stored. When rendering a conversation, filter by role: show `message` for user bubbles, and `response` for assistant bubbles.

---

### 4.3 Research & Thesis

#### `POST /api/chatbot/research/` — Research query  
**Auth required:** ✅

```
Body:
  topic          string  optional  (e.g. "Climate Change" — max 512 chars)
  query          string  required  (detailed question)
  research_type  string  optional  default: "overview"
                 choices: overview | thesis | literature |
                          methodology | analysis | conclusion | bibliography

Response 200:
  id           string (UUID)  saved record ID
  topic        string
  answer       string   (Markdown formatted, long-form academic response)
  sources      string[]
  tokens_used  number
  created_at   ISO 8601 datetime
```

**research_type descriptions for UI labels:**

| Value         | UI Label                       | Use case                         |
|---------------|--------------------------------|----------------------------------|
| `overview`    | Overview / Introduction        | General topic introduction       |
| `thesis`      | Thesis Statement & Structure   | Thesis writing help              |
| `literature`  | Literature Review              | Survey of existing research      |
| `methodology` | Research Methodology           | Methods section                  |
| `analysis`    | Data Analysis & Findings       | Analysis writing                 |
| `conclusion`  | Conclusion & Recommendations   | Closing section writing          |
| `bibliography`| Bibliography / References      | Source suggestions               |

---

#### `GET /api/chatbot/research/history/` — Research history  
**Auth required:** ✅

```
Response 200:  ResearchQuery[]  (last 50, newest first)

ResearchQuery:
  id           string (UUID)
  topic        string
  query        string
  response     string (full AI answer)
  sources      string[]
  tokens_used  number
  created_at   ISO 8601 datetime
```

---

### 4.4 Mock Exam

#### `POST /api/chatbot/mock-exam/generate/` — Generate exam  
**Auth required:** ✅

```
Body:
  subject             string  required   (e.g. "Physics")
  topic               string  required   (e.g. "Newton's Laws of Motion")
  difficulty          string  optional   default: "medium"
                      choices: easy | medium | hard | mixed
  question_type       string  optional   default: "mcq"
                      choices: mcq | short_answer | true_false | mixed
  num_questions       number  optional   default: 10  (min: 1, max: 30)
  time_limit_minutes  number  optional   null if not provided

Response 201:
  id                  string (UUID)
  subject             string
  topic               string
  difficulty          string
  question_type       string
  num_questions       number
  time_limit_minutes  number | null
  instructions        string  (may be empty)
  tokens_used         number
  created_at          ISO 8601 datetime
  message             string  (e.g. "Mock exam created with 10 questions.")
  questions           MockExamQuestion[]

Response 502:
  { error: "Could not generate exam questions. Please try again." }
```

**MockExamQuestion:**

```
id               string (UUID)
question_number  number        (1-indexed)
question_type    "mcq" | "short_answer" | "true_false"
question_text    string
options          string[]      (4 items for MCQ, e.g. ["A. ...", "B. ...", ...]
                               empty array for short_answer / true_false)
correct_answer   string        (e.g. "A. Newton's First Law")
explanation      string        (why the answer is correct)
marks            number        (usually 1)
```

---

#### `GET /api/chatbot/mock-exam/` — List exams  
**Auth required:** ✅

```
Response 200:  MockExamListItem[]  (newest first)

MockExamListItem:
  id                  string (UUID)
  subject             string
  topic               string
  difficulty          string
  question_type       string
  num_questions       number
  time_limit_minutes  number | null
  created_at          ISO 8601 datetime
  question_count      number  (actual saved question count)
```

---

#### `GET /api/chatbot/mock-exam/{exam_id}/` — Exam detail with questions  
**Auth required:** ✅

```
URL param: exam_id (UUID)
Response 200:  MockExam + questions[]   (same schema as generate response, minus `message`)
Response 404:  { detail: "No MockExam matches the given query." }
```

---

#### `DELETE /api/chatbot/mock-exam/{exam_id}/` — Delete exam  
**Auth required:** ✅

```
Response 204:  (empty body)
Response 404:  { detail: "No MockExam matches the given query." }
```

---

### 4.5 Admin — Document Management

> ⚠️ These endpoints require a **Django admin/staff account** (`is_staff=True`). Do NOT expose them to regular students.

#### `POST /api/chatbot/upload-document/` — Upload knowledge doc

```
Content-Type: multipart/form-data
Body (form fields):
  title      string   required  (document display name)
  file_type  string   required  choices: pdf | txt | json | docx
  file       File     required  (the actual file, max 50MB)

Response 201:
  id      string (UUID)
  status  "processing"

Response 400:
  Validation errors (file too large, type mismatch, etc.)
```

#### `POST /api/chatbot/admin/reprocess/{doc_id}/` — Reprocess document

```
URL param: doc_id (UUID)
Response 200:
  status  "reprocessing enqueued"
  id      string (UUID)
Response 404:  { error: "document not found" }
```

---

## 5. Data Models (TypeScript Types)

```typescript
// types/api.ts

export interface AuthTokens {
  access: string;
  refresh: string;
}

export interface ChatSession {
  id: string;
  created_at: string;
  updated_at: string;
  message_count: number;
  last_message: string | null;
}

export interface ChatSessionList {
  count: number;
  sessions: ChatSession[];
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  message: string;
  response: string | null;
  tokens_used: number | null;
  created_at: string;
}

export interface ChatHistoryResponse {
  session_id: string;
  created_at: string;
  updated_at: string;
  message_count: number;
  messages: ChatMessage[];
}

export interface AskResponse {
  answer: string;
  sources: string[];
  tokens_used: number;
}

export type ResearchType =
  | 'overview' | 'thesis' | 'literature'
  | 'methodology' | 'analysis' | 'conclusion' | 'bibliography';

export interface ResearchQuery {
  id: string;
  topic: string;
  query: string;
  response: string;
  sources: string[];
  tokens_used: number;
  created_at: string;
}

export type Difficulty = 'easy' | 'medium' | 'hard' | 'mixed';
export type QuestionType = 'mcq' | 'short_answer' | 'true_false' | 'mixed';

export interface MockExamQuestion {
  id: string;
  question_number: number;
  question_type: 'mcq' | 'short_answer' | 'true_false';
  question_text: string;
  options: string[];
  correct_answer: string;
  explanation: string;
  marks: number;
}

export interface MockExam {
  id: string;
  subject: string;
  topic: string;
  difficulty: Difficulty;
  question_type: QuestionType;
  num_questions: number;
  time_limit_minutes: number | null;
  instructions: string;
  tokens_used: number;
  created_at: string;
  questions: MockExamQuestion[];
  message?: string;
}

export interface MockExamListItem {
  id: string;
  subject: string;
  topic: string;
  difficulty: Difficulty;
  question_type: QuestionType;
  num_questions: number;
  time_limit_minutes: number | null;
  created_at: string;
  question_count: number;
}

export interface ApiError {
  detail?: string;
  error?: string;
  [field: string]: string | string[] | undefined;
}
```

---

## 6. Error Handling

### HTTP Status Codes

| Code | Meaning                            | Frontend action                              |
|------|------------------------------------|----------------------------------------------|
| 200  | Success                            | Render response                              |
| 201  | Created (exam, document, etc.)     | Show success + navigate to new resource      |
| 204  | Deleted successfully               | Remove item from UI list                     |
| 400  | Validation error                   | Show field-level errors from response body   |
| 401  | Unauthenticated / token expired    | Auto-refresh → if fails, redirect to login   |
| 403  | Forbidden (not admin or wrong user)| Show "You don't have permission" message     |
| 404  | Resource not found                 | Show "Not found" message or redirect          |
| 502  | AI generation failed               | Show retry button with user-friendly message |
| 500  | Server error                       | Show generic error + retry                   |

### Error Response Body Shape

```json
// 400 Validation
{
  "question": ["This field may not be blank."],
  "num_questions": ["Ensure this value is less than or equal to 30."]
}

// 401 / 403
{
  "detail": "Authentication credentials were not provided."
}

// 404
{
  "detail": "No MockExam matches the given query."
}

// 502
{
  "error": "Could not generate exam questions. Please try again."
}
```

### Recommended Error Utility

```typescript
// utils/apiError.ts
export function extractErrorMessage(err: unknown): string {
  const data = (err as any)?.response?.data;
  if (!data) return 'Something went wrong. Please try again.';
  if (typeof data === 'string') return data;
  if (data.detail) return data.detail;
  if (data.error) return data.error;
  // Flatten DRF field errors
  return Object.entries(data)
    .map(([field, msgs]) => `${field}: ${(msgs as string[]).join(', ')}`)
    .join('\n');
}
```

---

## 7. Feature Implementation Guides

### 7.1 Chat with Conversation History

```typescript
// hooks/useChat.ts
import { v4 as uuidv4 } from 'uuid';
import api from '../api/axiosInstance';

export function useChat() {
  // Generate once per conversation and persist in component state
  const [sessionId] = useState(() => uuidv4());
  const [messages, setMessages] = useState<DisplayMessage[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (question: string) => {
    // Optimistically add user message
    setMessages(prev => [...prev, { role: 'user', content: question }]);
    setLoading(true);

    try {
      const { data } = await api.post('/api/chatbot/ask/', {
        session_id: sessionId,
        question,
      });

      setMessages(prev => [...prev, {
        role: 'assistant',
        content: data.answer,
        sources: data.sources,
        tokens: data.tokens_used,
      }]);
    } catch (err) {
      setMessages(prev => [...prev, {
        role: 'error',
        content: extractErrorMessage(err),
      }]);
    } finally {
      setLoading(false);
    }
  };

  return { sessionId, messages, loading, sendMessage };
}
```

> **Important:** Generate the `session_id` once per conversation using `uuidv4()`. Pass the same ID for all messages in that thread. The backend uses it to retrieve history automatically.

---

### 7.2 Session Sidebar

```typescript
// Load all past sessions
const { data } = await api.get<ChatSessionList>('/api/chatbot/chat/sessions/');
// data.sessions is ordered newest-first

// When user clicks a session, load its full history
const { data: history } = await api.get<ChatHistoryResponse>(
  `/api/chatbot/history/${sessionId}/`
);

// Render messages:
history.messages.forEach(msg => {
  if (msg.role === 'user') {
    renderUserBubble(msg.message);
  } else {
    renderAssistantBubble(msg.response!);  // response is the AI answer
  }
});
```

**Sidebar item display:**
- Title: `last_message` (truncated to 120 chars)
- Subtitle: `updated_at` formatted as relative time ("2 hours ago")
- Badge: `message_count` (number of Q-A exchanges)

---

### 7.3 Research Assistant

```typescript
// api/research.ts
export async function submitResearch(params: {
  topic?: string;
  query: string;
  research_type?: ResearchType;
}): Promise<ResearchQuery> {
  const { data } = await api.post('/api/chatbot/research/', params);
  return data;
}

export async function getResearchHistory(): Promise<ResearchQuery[]> {
  const { data } = await api.get('/api/chatbot/research/history/');
  return data;
}
```

**UI Dropdown for research_type:**

```jsx
const RESEARCH_TYPES = [
  { value: 'overview',     label: 'Overview / Introduction' },
  { value: 'thesis',       label: 'Thesis Statement & Structure' },
  { value: 'literature',   label: 'Literature Review' },
  { value: 'methodology',  label: 'Research Methodology' },
  { value: 'analysis',     label: 'Data Analysis & Findings' },
  { value: 'conclusion',   label: 'Conclusion & Recommendations' },
  { value: 'bibliography', label: 'Bibliography / References' },
];
```

---

### 7.4 Mock Exam Builder & Viewer

#### Generating an Exam

```typescript
// api/mockExam.ts
export async function generateExam(params: {
  subject: string;
  topic: string;
  difficulty: Difficulty;
  question_type: QuestionType;
  num_questions: number;
  time_limit_minutes?: number;
}): Promise<MockExam> {
  const { data } = await api.post('/api/chatbot/mock-exam/generate/', params);
  return data;
}
```

> ⚠️ This call can take **10–30 seconds** (AI generation). Always show a loading spinner/skeleton and disable the submit button.

#### Fetching & Taking an Exam

```typescript
// Get all exams (list)
const { data } = await api.get<MockExamListItem[]>('/api/chatbot/mock-exam/');

// Get one exam with all questions
const { data: exam } = await api.get<MockExam>(`/api/chatbot/mock-exam/${examId}/`);
```

#### Rendering Questions by Type

```typescript
// MCQ: render options as radio buttons
if (question.question_type === 'mcq') {
  return question.options.map(opt => <RadioOption key={opt} label={opt} />);
}

// Short answer: render a text input
if (question.question_type === 'short_answer') {
  return <TextInput placeholder="Type your answer..." />;
}

// True/False: render two buttons
if (question.question_type === 'true_false') {
  return (
    <>
      <Button label="True"  onClick={() => selectAnswer('True')} />
      <Button label="False" onClick={() => selectAnswer('False')} />
    </>
  );
}
```

#### Scoring on Frontend

The backend does **not** score exams — scoring logic must be implemented on the frontend:

```typescript
function scoreExam(
  questions: MockExamQuestion[],
  answers: Record<string, string>  // { [question_id]: userAnswer }
): { score: number; total: number; results: QuestionResult[] } {
  let score = 0;
  const total = questions.reduce((sum, q) => sum + q.marks, 0);

  const results = questions.map(q => {
    // Normalize case for comparison
    const userAns = (answers[q.id] || '').trim().toLowerCase();
    const correct = q.correct_answer.trim().toLowerCase();
    const isCorrect = userAns === correct ||
      // For MCQ, also accept just the letter (e.g. "c" matches "c. first law")
      correct.startsWith(userAns + '.');

    if (isCorrect) score += q.marks;

    return {
      question_id: q.id,
      question_text: q.question_text,
      user_answer: answers[q.id],
      correct_answer: q.correct_answer,
      explanation: q.explanation,
      is_correct: isCorrect,
      marks_earned: isCorrect ? q.marks : 0,
    };
  });

  return { score, total, results };
}
```

#### Delete an Exam

```typescript
await api.delete(`/api/chatbot/mock-exam/${examId}/`);
// 204 = success, remove from UI list
```

---

## 8. Rendering AI Responses (Markdown)

All `answer` / `response` fields from the AI are **Markdown formatted**. Render them with a Markdown parser to display headings, bold text, bullet lists, and code blocks properly.

### Recommended library: `react-markdown`

```bash
npm install react-markdown remark-gfm
```

```jsx
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

function AIAnswer({ content }: { content: string }) {
  return (
    <div className="ai-answer prose max-w-none">
      <ReactMarkdown remarkPlugins={[remarkGfm]}>
        {content}
      </ReactMarkdown>
    </div>
  );
}
```

### For Math / Formulas (LaTeX)

AI answers may include LaTeX (e.g. `F = ma`, `∫`, `√`). Add KaTeX support:

```bash
npm install rehype-katex remark-math katex
```

```jsx
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css';

<ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[rehypeKatex]}>
  {content}
</ReactMarkdown>
```

---

## 9. File Upload (Admin)

Document upload uses `multipart/form-data`, not JSON:

```typescript
async function uploadDocument(file: File, title: string, fileType: string) {
  const formData = new FormData();
  formData.append('title', title);
  formData.append('file_type', fileType);
  formData.append('file', file);

  const { data } = await api.post('/api/chatbot/upload-document/', formData, {
    headers: {
      // Do NOT set Content-Type manually — let the browser set it with boundary
      'Authorization': `Bearer ${token}`,
    },
  });
  return data; // { id, status: "processing" }
}
```

**Important:** After upload, document processing is async (Celery). Status is not pushed to the frontend — if you need a processed status, poll the Django Admin panel or implement a separate status endpoint.

---

## 10. Suggested Screen Architecture

```
App
├── /login                  → LoginPage
│
├── /chat                   → ChatLayout
│   ├── Sidebar             → SessionList (GET /chat/sessions/)
│   └── ChatWindow          → ActiveConversation
│       ├── MessageList     → (renders history on session switch)
│       └── MessageInput    → (POST /ask/ with session_id)
│
├── /research               → ResearchPage
│   ├── ResearchForm        → (topic, query, research_type selector)
│   ├── ResearchResult      → (Markdown rendered response)
│   └── ResearchHistory     → (GET /research/history/)
│
├── /exams                  → ExamsPage
│   ├── ExamList            → (GET /mock-exam/)
│   └── /exams/new          → GenerateExamForm
│       └── ExamViewer      → (questions, timer, scoring)
│
└── /admin                  → AdminPage (staff only)
    └── DocumentUploadForm  → (POST /upload-document/)
```

---

## 11. Edge Cases & UX Notes

### Chat

| Scenario | Backend behaviour | Frontend recommendation |
|----------|-------------------|------------------------|
| Non-academic question | Returns 200 with rejection message (not an error) | Detect by checking `tokens_used === 0` or show the message as-is |
| New session | First message — no history available | Normal — backend handles gracefully |
| Same session across page reload | History is reloaded from DB via `/history/<id>/` | Store `session_id` in `sessionStorage` to persist within tab |
| Very long answer | Answers can be 2000+ chars (Markdown) | Use a scrollable container, never truncate AI responses |

### Mock Exam

| Scenario | Notes |
|----------|-------|
| Generation can be slow | Show skeleton/spinner; disable button; typical latency 10–30s |
| `options` is empty for short_answer / true_false | Always check `question_type` before rendering options |
| `correct_answer` for MCQ | Format: `"A. some answer text"` — match against user selection |
| `time_limit_minutes` is null | Do not show a timer; the exam has no time constraint |
| Mixed question types | Each question has its own `question_type` — render dynamically per question |

### Research

| Scenario | Notes |
|----------|-------|
| Long response | Research answers can be 1000–2000 tokens. Use a `<details>` or expandable section for history items |
| `topic` is optional | If not provided, the backend uses the first 80 chars of `query` as the topic |

### Auth

| Scenario | Notes |
|----------|-------|
| Access token expires during session | The axios interceptor auto-refreshes silently with no UX disruption |
| Refresh token expires | User must log in again — show login page |
| Admin-only routes | Hide upload UI from non-admin users; check user role on login response if customised |

### UUID Generation (session_id)

The frontend must generate valid **UUID v4** strings for `session_id`. Use:

```bash
npm install uuid
```

```typescript
import { v4 as uuidv4 } from 'uuid';
const sessionId = uuidv4(); // "550e8400-e29b-41d4-a716-446655440000"
```

Never use random strings — the backend validates UUID format strictly and returns 400 if invalid.

---

*Alpha AI Chatbot — Frontend Developer Guide v1.1*  
*Updated: April 8, 2026*
