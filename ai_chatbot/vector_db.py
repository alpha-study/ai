import uuid
from functools import lru_cache
from typing import List, Dict
import chromadb


@lru_cache(maxsize=1)
def get_client():
    """Get Chroma client with persistent storage."""
    # Use the newer client initialization (v0.4+)
    return chromadb.PersistentClient(path="./chroma_db")


@lru_cache(maxsize=1)
def get_query_collection():
    return get_client().get_collection(name='alpha_knowledge')

def upsert_chunks(chunks: List[str], metadatas: List[Dict], embeddings: List[List[float]] = None) -> List[str]:
    """Upsert chunks into Chroma collection and return list of vector ids."""
    client = get_client()
    
    # Try to get or create collection with NO embedding function (we provide our own embeddings)
    try:
        collection = client.get_or_create_collection(
            name='alpha_knowledge',
            metadata={"hnsw:space": "cosine"},
            embedding_function=None  # Critical: We provide our own 1536-dim embeddings
        )
    except Exception as e:
        # If collection exists with wrong config, delete and recreate
        get_query_collection.cache_clear()
        try:
            client.delete_collection(name='alpha_knowledge')
        except:
            pass
        collection = client.create_collection(
            name='alpha_knowledge',
            metadata={"hnsw:space": "cosine"},
            embedding_function=None  # Critical: We provide our own 1536-dim embeddings
        )
        get_query_collection.cache_clear()

    ids = [str(uuid.uuid4()) for _ in chunks]
    
    # We must always provide embeddings (1536-dim from OpenAI)
    if not embeddings or len(embeddings) != len(chunks):
        raise ValueError(f"Embeddings required for all {len(chunks)} chunks but got {len(embeddings) if embeddings else 0}")
    
    collection.add(
        ids=ids, 
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadatas
    )
    
    return ids


def query_chunks(query_embedding: List[float], top_k: int = 5):
    """Query the Chroma collection with a query embedding and return top_k results.

    Returns a list of dicts: {'id','document_id','chunk_text','metadata','distance'}
    """
    try:
        collection = get_query_collection()
    except Exception:
        return []

    results = collection.query(query_embeddings=[query_embedding], n_results=top_k, include=['documents', 'metadatas', 'distances'])
    out = []
    # results format: {'ids': [[...]], 'documents': [[...]], 'metadatas': [[...]], 'distances': [[...]]}
    if not results:
        return out
    # ids are always returned by default, even if not in include
    ids = results.get('ids', [[]])[0] if 'ids' in results else []
    docs = results.get('documents', [[]])[0]
    metadatas = results.get('metadatas', [[]])[0]
    distances = results.get('distances', [[]])[0]
    
    # Handle case where ids might not be present
    if ids:
        for _id, doc_text, meta, dist in zip(ids, docs, metadatas, distances):
            out.append({
                'id': _id,
                'document_id': meta.get('document_id') if isinstance(meta, dict) else None,
                'chunk_text': doc_text,
                'metadata': meta,
                'distance': dist,
            })
    else:
        # Fallback if no ids returned
        for i, (doc_text, meta, dist) in enumerate(zip(docs, metadatas, distances)):
            out.append({
                'id': f'chunk_{i}',
                'document_id': meta.get('document_id') if isinstance(meta, dict) else None,
                'chunk_text': doc_text,
                'metadata': meta,
                'distance': dist,
            })
    return out
