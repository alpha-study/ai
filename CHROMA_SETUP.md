# Chroma Vector Database Setup Guide

## ✅ Is Chroma Free?

**YES!** Chroma is **completely free** and open-source for local use. No API keys, no subscriptions, no limits.

- **License**: Apache 2.0
- **Cost**: $0 (fully free)
- **Storage**: Local file system
- **GitHub**: https://github.com/chroma-core/chroma

## 📦 What's Already Configured

Your Alpha AI Chatbot is already set up with Chroma:

1. **Installed**: `chromadb>=0.3.0` in requirements.txt
2. **Storage Location**: `./chroma_db/` (local directory)
3. **Client Type**: PersistentClient (auto-saves data)
4. **Collection**: `alpha_knowledge` (holds all document embeddings)

## 🧪 Verify Setup

Run the test script:

```bash
source .venv/bin/activate
python test_chroma.py
```

**Expected Output:**
```
============================================================
Testing Chroma Vector Database Setup
============================================================

1. Testing Chroma client connection...
   ✅ Chroma client initialized successfully
   📁 Persist directory: ./chroma_db

2. Testing OpenAI API configuration...
   ✅ OpenAI API key configured (length: 164)

3. Testing embedding generation...
   ✅ Generated 3 embeddings
   📊 Embedding dimension: 1536

4. Testing vector DB upsert...
   ✅ Upserted 3 vectors
   🆔 Sample vector ID: abc123...

5. Testing semantic search...
   ✅ Retrieved 3 results
   📝 Top result: ...

6. Checking Chroma collection stats...
   ✅ Collection 'alpha_knowledge' exists
   📊 Total vectors stored: 3

============================================================
✅ All tests passed! Chroma is working properly.
============================================================
```

## 📂 Where is Data Stored?

```
/Users/maddyb_007/Documents/dev/rohit/
├── chroma_db/               ← All vector embeddings stored here
│   ├── chroma.sqlite3       ← Vector metadata
│   └── [data files]         ← Actual embeddings
└── media/
    └── knowledge_docs/      ← Original uploaded documents
```

## 🔧 How It Works

### 1. Document Upload
```python
# User uploads PDF via API
POST /api/chatbot/upload-document/
```

### 2. Background Processing (Celery)
```python
# Process document (extract → chunk → embed → store)
- Extract text from PDF/DOCX/TXT/JSON
- Split into 1200-char chunks (200 overlap)
- Generate embeddings (OpenAI text-embedding-3-small)
- Store in Chroma with metadata
```

### 3. Semantic Search
```python
# User asks question
POST /api/chatbot/ask/
{
  "question": "What is the quadratic formula?"
}

# System:
- Compute question embedding
- Query Chroma for top 5 similar chunks
- Build context from retrieved chunks
- Pass to GPT-4o-mini for answer
- Return response with sources
```

## 📊 Chroma Features Used

### Collection Management
```python
from ai_chatbot.vector_db import get_client

client = get_client()
collection = client.get_collection("alpha_knowledge")

# Check stats
count = collection.count()  # Total vectors
print(f"Stored {count} chunks")
```

### Query by Similarity
```python
from ai_chatbot.vector_db import query_chunks
from ai_chatbot.embeddings import compute_embeddings

# Get embedding for question
question = "Explain photosynthesis"
embedding = compute_embeddings([question])[0]

# Find similar chunks
results = query_chunks(embedding, top_k=5)
for r in results:
    print(f"Source: {r['metadata']['source']}")
    print(f"Text: {r['chunk_text'][:100]}...")
    print(f"Distance: {r['distance']}")
```

## 🚀 Production Alternatives

While Chroma is perfect for local development, for production you might consider:

### Option 1: **Chroma Cloud** (Managed Chroma)
- Hosted Chroma service
- First 1M embeddings free
- Auto-scaling
- Website: https://www.trychroma.com/

### Option 2: **Pinecone**
- Fully managed vector DB
- Free tier: 1 index, 5M vectors
- Better for high-scale
- Website: https://www.pinecone.io/

### Option 3: **Weaviate**
- Open-source + cloud options
- Free tier available
- GraphQL API
- Website: https://weaviate.io/

### Option 4: **FAISS** (Local)
- Facebook's vector search library
- Extremely fast for large datasets
- No network required
- GitHub: https://github.com/facebookresearch/faiss

## 🔍 Troubleshooting

### Issue: "Chroma client failed to initialize"
**Solution**: Ensure `./chroma_db` directory is writable
```bash
mkdir -p ./chroma_db
chmod 755 ./chroma_db
```

### Issue: Embeddings not persisting
**Solution**: Check disk space and permissions
```bash
du -sh ./chroma_db
ls -la ./chroma_db
```

### Issue: Slow queries
**Solutions**:
1. Reduce `top_k` parameter (e.g., from 10 to 5)
2. Add index optimization (handled automatically by Chroma)
3. Consider upgrading to production vector DB

### Issue: Collection not found
**Solution**: Upload and process at least one document first
```bash
# Check collections
python -c "from ai_chatbot.vector_db import get_client; print(get_client().list_collections())"
```

## 📈 Performance Metrics

**Local Chroma (typical):**
- Insert: ~50-100 vectors/sec
- Query: ~10-20ms per query
- Storage: ~1KB per vector (1536 dims)
- Max recommended: ~1M vectors

**Memory Usage:**
- Baseline: ~50MB
- Per 10K vectors: +~15MB

## 🧹 Maintenance

### Clear all vectors (reset database)
```bash
rm -rf ./chroma_db
# Will be recreated on next upload
```

### Backup vectors
```bash
tar -czf chroma_backup_$(date +%Y%m%d).tar.gz ./chroma_db
```

### Restore vectors
```bash
tar -xzf chroma_backup_20260308.tar.gz
```

## ✅ Summary

- ✅ **Free**: No cost for local use
- ✅ **Easy**: Already configured and ready
- ✅ **Fast**: Good performance for most use cases
- ✅ **Persistent**: Data saved automatically
- ✅ **No API keys needed**: Runs entirely locally

**You're all set! Chroma is working perfectly for your Alpha AI Chatbot.** 🎉
