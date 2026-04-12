# Database Schema Documentation

## Overview

This Django application shares a **MySQL database** with an existing **Node.js application**.  
Django does **NOT** own the database. It only creates and manages its own chatbot-related tables.

| Concern | Owner |
|---|---|
| Database schema (existing tables) | Node.js |
| User management / authentication | Node.js |
| Chatbot tables (`ai_*` prefix) | Django |
| Django system tables (`django_*`, `auth_*`) | Django |

---

## Connection Details

| Parameter | Value |
|---|---|
| Engine | `django.db.backends.mysql` (via PyMySQL) |
| Host | `194.164.148.150` |
| Port | `3306` |
| Database | `alpha-api` |
| Charset | `utf8mb4` |
| SQL Mode | `STRICT_TRANS_TABLES` |

Environment variables: `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST`, `DATABASE_PORT`

---

## Table Naming Convention

| Prefix | Owner | Managed by Django | Examples |
|---|---|---|---|
| `ai_` | Django chatbot | ✅ Yes | `ai_chat_session`, `ai_chat_message` |
| `django_` | Django framework | ✅ Yes | `django_migrations`, `django_content_type` |
| `auth_` | Django auth | ✅ Yes | `auth_user`, `auth_permission` |
| *(no prefix)* | Node.js | ❌ **Never** | `users`, `students`, `institutes` |

---

## Django Chatbot Tables

### `ai_chat_session`
| Column | Type | Notes |
|---|---|---|
| `id` | `CHAR(32)` UUID | Primary key |
| `user_id` | `INT` | Node.js user ID (no FK constraint) |
| `created_at` | `DATETIME(6)` | Auto-set on create |
| `updated_at` | `DATETIME(6)` | Auto-set on update |

### `ai_chat_message`
| Column | Type | Notes |
|---|---|---|
| `id` | `CHAR(32)` UUID | Primary key |
| `session_id` | `CHAR(32)` UUID | FK → `ai_chat_session.id` |
| `role` | `VARCHAR(16)` | `user` or `assistant` |
| `message` | `LONGTEXT` | User question |
| `response` | `LONGTEXT` | AI response (nullable) |
| `tokens_used` | `INT` | Token count (nullable) |
| `created_at` | `DATETIME(6)` | Auto-set on create |

### `ai_knowledge_document`
| Column | Type | Notes |
|---|---|---|
| `id` | `CHAR(32)` UUID | Primary key |
| `title` | `VARCHAR(512)` | Document title |
| `file` | `VARCHAR(100)` | File path in `knowledge_docs/` |
| `file_type` | `VARCHAR(16)` | `pdf`, `txt`, `json`, `docx` |
| `uploaded_by_id` | `INT` | Node.js user ID (no FK constraint) |
| `uploaded_at` | `DATETIME(6)` | Auto-set on create |
| `processed` | `BOOL` | Processing status |
| `metadata` | `JSON` | Arbitrary metadata |

### `ai_document_chunk`
| Column | Type | Notes |
|---|---|---|
| `id` | `CHAR(32)` UUID | Primary key |
| `document_id` | `CHAR(32)` UUID | FK → `ai_knowledge_document.id` |
| `chunk_text` | `LONGTEXT` | Text chunk |
| `embedding_vector` | `LONGBLOB` | Binary embedding (nullable) |
| `vector_id` | `VARCHAR(256)` | ChromaDB vector ID (nullable) |
| `created_at` | `DATETIME(6)` | Auto-set on create |

### `ai_research_query`
| Column | Type | Notes |
|---|---|---|
| `id` | `CHAR(32)` UUID | Primary key |
| `user_id` | `INT` | Node.js user ID (no FK constraint) |
| `topic` | `VARCHAR(512)` | Research topic |
| `query` | `LONGTEXT` | Full query text |
| `response` | `LONGTEXT` | AI response |
| `sources` | `JSON` | Source references |
| `tokens_used` | `INT` | Token count |
| `created_at` | `DATETIME(6)` | Auto-set on create |

### `ai_mock_exam`
| Column | Type | Notes |
|---|---|---|
| `id` | `CHAR(32)` UUID | Primary key |
| `user_id` | `INT` | Node.js user ID (no FK constraint) |
| `subject` | `VARCHAR(256)` | Exam subject |
| `topic` | `VARCHAR(512)` | Exam topic |
| `difficulty` | `VARCHAR(16)` | `easy`, `medium`, `hard`, `mixed` |
| `question_type` | `VARCHAR(16)` | `mcq`, `short_answer`, `true_false`, `mixed` |
| `num_questions` | `INT UNSIGNED` | Number of questions |
| `time_limit_minutes` | `INT UNSIGNED` | Time limit (nullable) |
| `instructions` | `LONGTEXT` | Exam instructions |
| `tokens_used` | `INT` | Token count |
| `created_at` | `DATETIME(6)` | Auto-set on create |

### `ai_mock_exam_question`
| Column | Type | Notes |
|---|---|---|
| `id` | `CHAR(32)` UUID | Primary key |
| `exam_id` | `CHAR(32)` UUID | FK → `ai_mock_exam.id` |
| `question_number` | `INT UNSIGNED` | Sequence number |
| `question_type` | `VARCHAR(16)` | `mcq`, `short_answer`, `true_false` |
| `question_text` | `LONGTEXT` | Question body |
| `options` | `JSON` | MCQ options list |
| `correct_answer` | `LONGTEXT` | Correct answer |
| `explanation` | `LONGTEXT` | Answer explanation |
| `marks` | `INT UNSIGNED` | Points for question |

---

## Unmanaged Model (Example)

The `NodeUser` model in `ai_chatbot/models.py` is mapped to the existing `users` table with `managed = False`.  
Django will **never** create, alter, or drop this table. Use it only for **read-only SELECT queries**.

```python
class NodeUser(models.Model):
    class Meta:
        managed = False
        db_table = 'users'
```

Adjust the field names/types to match the real Node.js `users` table schema.

---

## Database Router

File: `ai_chatbot/db_router.py` → class `ChatbotRouter`

The router controls which apps are allowed to run migrations:

| App | Migrations Allowed |
|---|---|
| `ai_chatbot` | ✅ |
| `auth`, `contenttypes`, `sessions`, `admin`, `messages` | ✅ |
| Everything else | ❌ Blocked |

---

## Migration Safety Rules

### ✅ Safe Commands
```bash
# Create migrations for chatbot app ONLY
python manage.py makemigrations ai_chatbot

# Apply migrations for chatbot app ONLY
python manage.py migrate ai_chatbot

# Apply all allowed migrations (router blocks unsafe ones)
python manage.py migrate
```

### ❌ Never Run
```bash
# NEVER run makemigrations without specifying the app
python manage.py makemigrations  # DANGEROUS — may detect Node.js tables

# NEVER use --run-syncdb
python manage.py migrate --run-syncdb  # May attempt to create tables for unmanaged models

# NEVER use inspectdb and then migrate
python manage.py inspectdb  # Creates managed models for ALL tables
```

### Pre-Migration Checklist
1. Always specify `ai_chatbot` when running `makemigrations`
2. Review generated migration files before applying
3. Test migrations on a staging database first
4. Never add `managed = True` to any model mapped to a Node.js table
5. Never add ForeignKey constraints pointing to Node.js tables

---

## Concurrency & Safety (Node.js + Django)

| Concern | Strategy |
|---|---|
| Concurrent reads | Safe — MySQL handles concurrent SELECT natively |
| Concurrent writes to **different** tables | Safe — Django writes `ai_*`, Node.js writes its own |
| User ID references | `IntegerField` (no FK constraint) — avoids locking `users` table |
| Transactions | Django uses `AUTOCOMMIT` by default; wrap multi-table writes in `transaction.atomic()` |
| Connection pooling | Use `django-db-connection-pool` or `CONN_MAX_AGE` in production |

### Recommended `settings.py` addition for production:
```python
DATABASES['default']['CONN_MAX_AGE'] = 600  # reuse connections for 10 minutes
```

---

## Best Practices Checklist

- [x] All chatbot tables use `ai_` prefix
- [x] No ForeignKey constraints to Node.js-owned tables
- [x] `user_id` stored as plain `IntegerField` (no ORM relationship)
- [x] Database router blocks migrations on non-Django tables
- [x] `managed = False` for any model mapped to existing tables
- [x] `utf8mb4` charset for full Unicode support
- [x] `STRICT_TRANS_TABLES` SQL mode enabled
- [x] Credentials loaded from environment variables
- [x] Migrations scoped to `ai_chatbot` app only

---

## Common Mistakes to Avoid

| Mistake | Why It's Dangerous |
|---|---|
| Using `ForeignKey(User)` | Creates FK constraint to `auth_user`, not the Node.js `users` table |
| Running `makemigrations` without app name | May generate migrations for inspected Node.js tables |
| Setting `managed = True` on existing tables | Django will try to alter/drop the table |
| Using `--run-syncdb` | Bypasses migration safety and may create unwanted tables |
| Hardcoding DB credentials in `settings.py` | Security risk — always use environment variables |
| Using `select_related('user')` | Will fail — `user_id` is an IntegerField, not a ForeignKey |
| Deleting `django_migrations` rows | Breaks migration state tracking |
