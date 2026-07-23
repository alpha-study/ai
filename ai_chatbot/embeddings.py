from typing import List
from django.conf import settings
from .openai_client import get_openai_client

def compute_embeddings(texts: List[str]) -> List[List[float]]:
    """Compute embeddings for a list of texts using OpenAI embeddings.

    Raises if OPENAI_API_KEY not configured.
    """
    if not settings.OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY not configured')

    client = get_openai_client()
    
    # batch the embedding requests (OpenAI supports batching)
    resp = client.embeddings.create(input=texts, model='text-embedding-3-small')
    embeddings = [d.embedding for d in resp.data]
    return embeddings
