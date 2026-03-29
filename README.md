# Alpha AI Chatbot (backend)

This workspace contains a Django app `ai_chatbot` implementing a Retrieval-Augmented Generation (RAG) chatbot for the Alpha educational platform.

Quick setup (macOS / Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env to add secrets (OPENAI_API_KEY etc)
python manage.py migrate
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

**Get Chat History:**
```bash
curl http://localhost:8000/api/chatbot/history/550e8400-e29b-41d4-a716-446655440000/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Recommended next steps:
- Configure Redis and Celery for background processing
- Configure a vector DB (Chroma/Pinecone)
- Upload sample documents via admin or the upload endpoint

Running tests:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python manage.py test
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
