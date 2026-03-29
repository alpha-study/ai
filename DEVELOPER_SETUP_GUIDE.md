# Alpha AI Chatbot - Developer Setup Guide

Complete step-by-step guide for setting up the Alpha AI Chatbot development environment.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [System Requirements](#system-requirements)
3. [Initial Setup](#initial-setup)
4. [Installation Steps](#installation-steps)
5. [Configuration](#configuration)
6. [Database Setup](#database-setup)
7. [Running the Application](#running-the-application)
8. [Testing](#testing)
9. [Troubleshooting](#troubleshooting)
10. [Development Workflow](#development-workflow)

---

## Prerequisites

### Required Software

1. **Python 3.11 or higher**
   ```bash
   # Check Python version
   python3 --version
   
   # macOS installation (using Homebrew)
   brew install python@3.11
   
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3.11 python3.11-venv python3.11-dev
   
   # Windows
   # Download from https://www.python.org/downloads/
   ```

2. **Redis Server**
   ```bash
   # macOS
   brew install redis
   brew services start redis
   
   # Ubuntu/Debian
   sudo apt install redis-server
   sudo systemctl start redis-server
   sudo systemctl enable redis-server
   
   # Windows
   # Download from https://github.com/microsoftarchive/redis/releases
   # Or use WSL
   ```

3. **Git**
   ```bash
   # macOS
   brew install git
   
   # Ubuntu/Debian
   sudo apt install git
   
   # Windows
   # Download from https://git-scm.com/downloads
   ```

4. **OpenAI API Account**
   - Sign up at https://platform.openai.com/
   - Generate an API key from https://platform.openai.com/api-keys
   - Store it securely (you'll need it for configuration)

---

## System Requirements

- **OS**: macOS 10.15+, Ubuntu 20.04+, Windows 10+ (with WSL recommended)
- **RAM**: Minimum 4GB, Recommended 8GB+
- **Storage**: Minimum 2GB free space
- **Network**: Internet connection for API calls and package installation

---

## Initial Setup

### 1. Clone the Repository

```bash
# Navigate to your projects directory
cd ~/Documents/dev

# Clone the repository (or create the directory if starting fresh)
mkdir -p rohit
cd rohit
```

### 2. Create Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# macOS/Linux:
source .venv/bin/activate

# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Windows (Command Prompt):
.venv\Scripts\activate.bat

# Verify activation (should show .venv in prompt)
which python  # macOS/Linux
where python  # Windows
```

### 3. Verify Redis is Running

```bash
# Test Redis connection
redis-cli ping
# Should return: PONG

# If not running:
# macOS:
brew services start redis

# Linux:
sudo systemctl start redis-server

# Check Redis status:
redis-cli info server
```

---

## Installation Steps

### 1. Install Python Dependencies

```bash
# Ensure virtual environment is activated
# Install all required packages
pip install --upgrade pip
pip install -r requirements.txt
```

**Requirements.txt** should contain:
```
Django==6.0.3
djangorestframework==3.16.1
djangorestframework-simplejwt==5.5.1
celery==5.6.2
redis==7.3.0
python-dotenv==1.0.1
openai==1.62.0
chromadb==1.5.2
langchain==1.2.10
pdfplumber==0.11.4
python-docx==1.1.2
pymupdf==1.25.3
python-magic==0.4.27
pillow==11.1.0
```

### 2. Verify Installation

```bash
# Check installed packages
pip list

# Verify key packages
python -c "import django; print(f'Django: {django.__version__}')"
python -c "import openai; print(f'OpenAI: {openai.__version__}')"
python -c "import chromadb; print(f'Chroma: {chromadb.__version__}')"
```

---

## Configuration

### 1. Create Environment File

Create a `.env` file in the project root directory:

```bash
touch .env
```

### 2. Configure Environment Variables

Edit `.env` and add the following:

```bash
# Django Settings
SECRET_KEY=your-super-secret-django-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite for development)
DATABASE_URL=sqlite:///db.sqlite3

# Redis Configuration
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# OpenAI Configuration
OPENAI_API_KEY=sk-proj-your-openai-api-key-here
AI_CHAT_MODEL=gpt-4o-mini
AI_EMBEDDING_MODEL=text-embedding-3-small
AI_MAX_RESPONSE_TOKENS=512

# Chroma Vector Database
CHROMA_DB_PATH=./chroma_db

# File Upload Settings
MAX_UPLOAD_SIZE=52428800  # 50MB in bytes
ALLOWED_DOCUMENT_TYPES=pdf,txt,json,docx
```

### 3. Generate Django Secret Key

```bash
# Generate a secure secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Copy the output and paste it as SECRET_KEY in .env file
```

### 4. Verify Configuration

```bash
# Test environment loading
python manage.py shell -c "from django.conf import settings; print(f'Debug: {settings.DEBUG}'); print(f'Secret Key: {settings.SECRET_KEY[:10]}...')"
```

---

## Database Setup

### 1. Run Initial Migrations

```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate

# You should see output like:
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   ...
#   Applying ai_chatbot.0001_initial... OK
```

### 2. Create Superuser

```bash
# Create admin account for Django admin panel
python manage.py createsuperuser

# Enter details when prompted:
# Username: admin
# Email: admin@example.com
# Password: (choose a strong password)
# Password (again): (confirm password)
```

### 3. Verify Database

```bash
# Check database tables
python manage.py dbshell
# SQLite will open, then run:
.tables
# Should show: auth_*, django_*, ai_chatbot_*
.exit

# Or use Python:
python manage.py shell -c "from django.contrib.auth.models import User; print(f'Users: {User.objects.count()}')"
```

---

## Running the Application

### 1. Start Redis (if not already running)

```bash
# macOS:
brew services start redis

# Linux:
sudo systemctl start redis-server

# Verify:
redis-cli ping  # Should return PONG
```

### 2. Start Celery Worker

Open a **new terminal window/tab** and run:

```bash
# Navigate to project directory
cd /Users/maddyb_007/Documents/dev/rohit

# Activate virtual environment
source .venv/bin/activate

# Start Celery worker
# macOS (requires --pool=solo due to fork() issues with Python 3.13):
celery -A alpha_project worker --pool=solo --loglevel=info

# Linux:
celery -A alpha_project worker --loglevel=info

# Windows:
celery -A alpha_project worker --pool=solo --loglevel=info
```

**Keep this terminal running!**

### 3. Start Django Development Server

Open **another new terminal window/tab** and run:

```bash
# Navigate to project directory
cd /Users/maddyb_007/Documents/dev/rohit

# Activate virtual environment
source .venv/bin/activate

# Start Django server
python manage.py runserver

# Server will start at: http://127.0.0.1:8000/
```

**Keep this terminal running!**

### 4. Verify Everything is Running

You should now have **3 terminals** running:
1. **Redis** (running as background service)
2. **Celery Worker** (processing background tasks)
3. **Django Server** (handling HTTP requests)

Test the setup:
```bash
# In a new terminal:
curl http://localhost:8000/admin/
# Should return HTML (Django admin page)
```

---

## Testing

### 1. Access Django Admin

1. Open browser: http://localhost:8000/admin/
2. Login with superuser credentials
3. You should see:
   - Users
   - Groups
   - Chat Sessions
   - Chat Messages
   - Knowledge Documents
   - Document Chunks

### 2. Get JWT Token

```bash
# Create a test token
python manage.py shell -c "
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

user = User.objects.first()
token = RefreshToken.for_user(user)
print(f'Access Token: {token.access_token}')
"
```

Copy the access token for API testing.

### 3. Test Document Upload API

Using **Postman** or **curl**:

```bash
# Replace YOUR_JWT_TOKEN with the token from step 2
curl -X POST http://localhost:8000/api/chatbot/upload-document/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "file=@/path/to/your/document.pdf" \
  -F "title=Test Document"

# Expected response:
# {"id": "uuid-here", "title": "Test Document", "file_type": "pdf", "processed": false}
```

### 4. Test Chat API

Wait 10-15 seconds for document processing, then:

```bash
curl -X POST http://localhost:8000/api/chatbot/ask/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "session_id": "12345678-1234-5678-1234-567812345678",
    "question": "What is this document about?"
  }'

# Expected response:
# {
#   "answer": "...",
#   "sources": ["your_document.pdf"],
#   "tokens_used": 123
# }
```

### 5. Run Unit Tests

```bash
# Run all tests
python manage.py test ai_chatbot

# Run specific test file
python manage.py test ai_chatbot.tests.test_utils

# Run with verbose output
python manage.py test ai_chatbot --verbosity=2
```

### 6. Test Chroma Vector Database

```bash
# Verify Chroma setup
python test_chroma.py

# Should output:
# ✓ Chroma client connection successful
# ✓ OpenAI configuration loaded
# ✓ Embeddings generated successfully
# ✓ Search results retrieved
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. **Celery Worker Crashes on macOS**

**Error**: `objc[xxxxx]: +[__NSCFConstantString initialize] may have been in progress...`

**Solution**: Use `--pool=solo` flag:
```bash
celery -A alpha_project worker --pool=solo --loglevel=info
```

#### 2. **Redis Connection Error**

**Error**: `redis.exceptions.ConnectionError: Error 61 connecting to localhost:6379`

**Solution**:
```bash
# Start Redis
brew services start redis  # macOS
sudo systemctl start redis-server  # Linux

# Verify
redis-cli ping
```

#### 3. **OpenAI API Error**

**Error**: `openai.error.AuthenticationError: Incorrect API key`

**Solution**:
- Verify API key in `.env` file
- Check key validity at https://platform.openai.com/api-keys
- Ensure `.env` is in project root
- Restart Django server after changing `.env`

#### 4. **Chroma Dimension Mismatch**

**Error**: `Collection expecting embedding with dimension of 384, got 1536`

**Solution**:
```bash
# Delete and recreate Chroma database
rm -rf ./chroma_db

# Reprocess documents
python manage.py shell -c "
from ai_chatbot.models import KnowledgeDocument
for doc in KnowledgeDocument.objects.all():
    doc.processed = False
    doc.chunks.all().delete()
    doc.save()
"

# Documents will be reprocessed automatically by Celery
```

#### 5. **Module Not Found Error**

**Error**: `ModuleNotFoundError: No module named 'xxx'`

**Solution**:
```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt

# Verify installation
pip list | grep xxx
```

#### 6. **Database Locked Error**

**Error**: `django.db.utils.OperationalError: database is locked`

**Solution**:
```bash
# SQLite doesn't handle concurrent writes well
# Option 1: Wait a moment and retry
# Option 2: Close all Django shells and management commands
# Option 3: For production, use PostgreSQL (see AWS deployment guide)
```

#### 7. **File Upload Error**

**Error**: `File size exceeds maximum allowed size`

**Solution**:
```bash
# Check .env configuration
# Increase MAX_UPLOAD_SIZE (in bytes)
MAX_UPLOAD_SIZE=104857600  # 100MB

# Restart Django server
```

---

## Development Workflow

### Daily Development Routine

1. **Start Development Session**
   ```bash
   cd /Users/maddyb_007/Documents/dev/rohit
   source .venv/bin/activate
   
   # Terminal 1: Start Redis (if not running)
   brew services start redis
   
   # Terminal 2: Start Celery
   celery -A alpha_project worker --pool=solo --loglevel=info
   
   # Terminal 3: Start Django
   python manage.py runserver
   ```

2. **Make Code Changes**
   - Edit files in IDE/editor
   - Django auto-reloads on file changes
   - Celery requires manual restart after code changes

3. **Test Changes**
   ```bash
   # Run tests
   python manage.py test
   
   # Test specific functionality
   curl -X POST http://localhost:8000/api/chatbot/ask/ ...
   ```

4. **Database Changes**
   ```bash
   # When models are modified:
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **End Development Session**
   ```bash
   # Stop servers: Ctrl+C in each terminal
   # Deactivate virtual environment
   deactivate
   ```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "Add: description of changes"

# Push to remote
git push origin feature/your-feature-name

# Create pull request for review
```

### Code Quality Checks

```bash
# Format code
pip install black
black .

# Lint code
pip install flake8
flake8 ai_chatbot/

# Type checking
pip install mypy
mypy ai_chatbot/
```

---

## Project Structure

```
rohit/
├── .env                          # Environment variables (DO NOT COMMIT)
├── .gitignore                    # Git ignore rules
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── db.sqlite3                    # SQLite database (development)
├── chroma_db/                    # Chroma vector database storage
├── media/                        # Uploaded documents
│   └── knowledge_docs/
├── alpha_project/                # Django project configuration
│   ├── __init__.py
│   ├── settings.py               # Django settings
│   ├── urls.py                   # URL routing
│   ├── wsgi.py                   # WSGI application
│   └── celery.py                 # Celery configuration
├── ai_chatbot/                   # Main application
│   ├── __init__.py
│   ├── models.py                 # Database models
│   ├── views.py                  # API views
│   ├── serializers.py            # DRF serializers
│   ├── urls.py                   # App URL routing
│   ├── admin.py                  # Django admin configuration
│   ├── tasks.py                  # Celery background tasks
│   ├── utils.py                  # Utility functions
│   ├── embeddings.py             # OpenAI embeddings
│   ├── vector_db.py              # Chroma operations
│   ├── rag.py                    # RAG pipeline
│   ├── migrations/               # Database migrations
│   └── tests/                    # Unit tests
├── test_chroma.py                # Chroma verification script
├── DEVELOPER_SETUP_GUIDE.md      # This file
├── AWS_DEPLOYMENT_GUIDE.md       # AWS deployment instructions
└── README.md                     # Project overview
```

---

## Key Files to Know

- **settings.py**: Django configuration, database, middleware, installed apps
- **models.py**: Database schema (ChatSession, ChatMessage, KnowledgeDocument, DocumentChunk)
- **views.py**: API endpoints (upload, ask, history)
- **tasks.py**: Background processing (document processing, embedding generation)
- **rag.py**: RAG implementation (retrieve and answer)
- **.env**: Sensitive configuration (API keys, secrets)

---

## Useful Management Commands

```bash
# Database operations
python manage.py makemigrations        # Create migration files
python manage.py migrate               # Apply migrations
python manage.py dbshell               # Open database shell

# User management
python manage.py createsuperuser       # Create admin user
python manage.py changepassword admin  # Change password

# Development
python manage.py runserver             # Start dev server
python manage.py runserver 0.0.0.0:8000  # Listen on all interfaces
python manage.py shell                 # Open Django shell

# Testing
python manage.py test                  # Run all tests
python manage.py test ai_chatbot       # Run app tests

# Custom commands (from ai_chatbot/management/commands/)
python manage.py reprocess_document --id <uuid>  # Reprocess a document

# Data management
python manage.py dumpdata > backup.json   # Backup data
python manage.py loaddata backup.json     # Restore data
```

---

## API Endpoints Reference

### 1. Authentication

**Obtain JWT Token**
```bash
POST /api/token/
Content-Type: application/json

{
  "username": "admin",
  "password": "your_password"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbG...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbG..."
}
```

**Refresh Token**
```bash
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbG..."
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbG..."
}
```

### 2. Document Upload

```bash
POST /api/chatbot/upload-document/
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

Form Data:
- file: (binary)
- title: "Document Title"

Response:
{
  "id": "uuid",
  "title": "Document Title",
  "file_type": "pdf",
  "processed": false
}
```

### 3. Chat Query

```bash
POST /api/chatbot/ask/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "session_id": "12345678-1234-5678-1234-567812345678",
  "question": "What is Alpha platform?"
}

Response:
{
  "answer": "Alpha is an integrated platform...",
  "sources": ["document.pdf"],
  "tokens_used": 425
}
```

### 4. Chat History

```bash
GET /api/chatbot/history/<session_id>/
Authorization: Bearer <access_token>

Response:
{
  "session": "uuid",
  "messages": [
    {
      "role": "user",
      "message": "What is Alpha?",
      "response": null,
      "tokens_used": null,
      "created_at": "2026-03-08T10:00:00Z"
    },
    {
      "role": "assistant",
      "message": "What is Alpha?",
      "response": "Alpha is...",
      "tokens_used": 425,
      "created_at": "2026-03-08T10:00:05Z"
    }
  ]
}
```

---

## Environment Variables Reference

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| SECRET_KEY | Django secret key | `django-insecure-xyz...` | Yes |
| DEBUG | Debug mode | `True` / `False` | Yes |
| ALLOWED_HOSTS | Allowed hostnames | `localhost,127.0.0.1` | Yes |
| OPENAI_API_KEY | OpenAI API key | `sk-proj-...` | Yes |
| AI_CHAT_MODEL | LLM model | `gpt-4o-mini` | Yes |
| AI_EMBEDDING_MODEL | Embedding model | `text-embedding-3-small` | Yes |
| AI_MAX_RESPONSE_TOKENS | Max response length | `512` | No |
| CELERY_BROKER_URL | Redis URL for Celery | `redis://localhost:6379/0` | Yes |
| MAX_UPLOAD_SIZE | Max file size (bytes) | `52428800` | No |

---

## Next Steps

1. ✅ Complete setup following this guide
2. 📚 Upload test documents via admin or API
3. 💬 Test chat functionality with educational questions
4. 🧪 Run unit tests to ensure everything works
5. 📖 Review [AWS_DEPLOYMENT_GUIDE.md](AWS_DEPLOYMENT_GUIDE.md) for production deployment
6. 🚀 Start developing new features!

---

## Support & Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **Celery Documentation**: https://docs.celeryq.dev/
- **Chroma Documentation**: https://docs.trychroma.com/
- **OpenAI API Reference**: https://platform.openai.com/docs/
- **LangChain Documentation**: https://python.langchain.com/

---

## Contributing

When contributing to this project:
1. Follow PEP 8 style guidelines
2. Write unit tests for new features
3. Update documentation for API changes
4. Test thoroughly before submitting PR
5. Keep commits atomic and well-described

---

**Happy Coding! 🚀**
