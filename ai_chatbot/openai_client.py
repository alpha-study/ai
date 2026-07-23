from functools import lru_cache

from django.conf import settings
from openai import OpenAI


@lru_cache(maxsize=4)
def _client_for_key(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key)


def get_openai_client() -> OpenAI:
    """Return a process-local OpenAI client so HTTP connections can be reused."""
    api_key = settings.OPENAI_API_KEY
    if not api_key:
        raise RuntimeError('OPENAI_API_KEY not configured')
    return _client_for_key(api_key)
