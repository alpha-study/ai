# Alpha AI Chatbot (backend)

This workspace contains a Django app `ai_chatbot` implementing a Retrieval-Augmented Generation (RAG) chatbot for the Alpha educational platform.

> **Database:** Shared MySQL (`alpha-api`) with the Node.js application.
> Django exclusively owns tables prefixed with `ai_` and Django internal tables.
> Node.js-owned tables are never touched by Django migrations.

Quick setup (macOS / Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env — set DATABASE_PASSWORD, OPENAI_API_KEY, DJANGO_SECRET_KEY

# ✅ Safe migrations — chatbot tables only
python manage.py migrate ai_chatbot
python manage.py migrate contenttypes
python manage.py migrate auth
python manage.py migrate admin
python manage.py migrate sessions

# Create a Django admin account for testing (separate from Node.js users)
python manage.py createsuperuser

python manage.py runserver
```

## Authentication (JWT Tokens)

**Get Access Token:**
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1Q...",
  "refresh": "eyJ0eXAiOiJKV1Q..."
}
```

**Refresh Token:**
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "eyJ0eXAiOiJKV1Q..."}'
```

**Verify Token:**
```bash
curl -X POST http://localhost:8000/api/token/verify/ \
  -H "Content-Type: application/json" \
  -d '{"token": "eyJ0eXAiOiJKV1Q..."}'
```

## API Usage

**Upload Document (Admin only):**
```bash
curl -X POST http://localhost:8000/api/chatbot/upload-document/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "title=Algebra Basics" \
  -F "file=@/path/to/document.pdf" \
  -F "file_type=pdf"
```

**Ask Question:**
```bash
curl -X POST http://localhost:8000/api/chatbot/ask/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "550e8400-e29b-41d4-a716-446655440000",
    "question": "What is the quadratic formula?"
  }'
```

**Ask Question (Streaming):**
```bash
curl -N -X POST http://localhost:8000/api/chatbot/ask/stream/ \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "session_id": "550e8400-e29b-41d4-a716-446655440000",
    "question": "Give me information on India",
    "answer_style": "fast",
    "use_kb": false,
    "max_tokens": 160
  }'
```

**Get Chat History:**
```bash
curl http://localhost:8000/api/chatbot/history/550e8400-e29b-41d4-a716-446655440000/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Recommended next steps:
- Configure Redis and Celery for background processing
- Configure a vector DB (Chroma/Pinecone)
- Upload sample documents via admin or the upload endpoint

> **Schema export:** Run `python export_schema.py` to generate a full Markdown schema document for all 100+ tables in the shared MySQL database.

Running tests:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python manage.py test ai_chatbot
```

Docker / local deploy (dev):

```bash
docker compose up --build
```

Deployment suggestions:
- Use S3 for file storage in production (configure `DEFAULT_FILE_STORAGE`).
- Use a managed vector DB (Pinecone/Weaviate) for scale; Chroma/FAISS for dev.
- Run Celery workers with autoscaling for ingestion and embedding workloads.
- Store secrets in a secrets manager and set `OPENAI_API_KEY` and other keys securely.
- Use monitoring (Prometheus) and logging (ELK) to track costs and requests.
