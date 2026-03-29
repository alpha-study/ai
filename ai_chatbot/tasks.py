from celery import shared_task
from .models import KnowledgeDocument, DocumentChunk
from .utils import extract_text_from_file, chunk_text
from .embeddings import compute_embeddings
from .vector_db import upsert_chunks
import pickle


@shared_task
def process_document(document_id: str):
    """
    Background task to extract text, chunk, embed and upsert to vector DB.
    """
    try:
        doc = KnowledgeDocument.objects.get(id=document_id)
    except KnowledgeDocument.DoesNotExist:
        return

    path = doc.file.path
    text = extract_text_from_file(path, doc.file_type)
    if not text:
        doc.processed = True
        doc.save()
        return

    # chunk
    chunks = chunk_text(text, chunk_size=1200, overlap=200)

    # persist chunk records
    chunk_objs = []
    metadatas = []
    chunk_texts = []
    for i, c in enumerate(chunks):
        ch = DocumentChunk.objects.create(document=doc, chunk_text=c)
        chunk_objs.append(ch)
        chunk_texts.append(c)
        metadatas.append({'document_id': str(doc.id), 'chunk_index': i, 'title': doc.title, 'source': doc.file.name})

    # compute embeddings
    try:
        embeddings = compute_embeddings(chunk_texts)
    except Exception as e:
        print(f"Error computing embeddings: {e}")
        doc.processed = False
        doc.save()
        return

    # upsert to vector DB (Chroma) with embeddings
    try:
        vector_ids = upsert_chunks(chunk_texts, metadatas, embeddings)
    except Exception as e:
        print(f"Error upserting to vector DB: {e}")
        doc.processed = False
        doc.save()
        return

    # store embedding blobs and vector ids on DocumentChunk
    for ch, emb, vid in zip(chunk_objs, embeddings, vector_ids):
        ch.embedding_vector = pickle.dumps(emb)
        ch.vector_id = vid
        ch.save()

    doc.processed = True
    doc.save()
