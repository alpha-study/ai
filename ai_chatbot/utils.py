import json
import io
import pdfplumber
import docx
from typing import List

def extract_text_from_file(path: str, file_type: str) -> str:
    """Extract text from supported file types."""
    file_type = file_type.lower()
    if file_type == 'pdf':
        texts = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                texts.append(page.extract_text() or '')
        return '\n'.join(texts)
    elif file_type == 'docx':
        doc = docx.Document(path)
        paragraphs = [p.text for p in doc.paragraphs]
        return '\n'.join(paragraphs)
    elif file_type == 'txt':
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    elif file_type == 'json':
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # naive: stringify top-level values
        if isinstance(data, dict):
            parts = []
            for k, v in data.items():
                parts.append(f"{k}: {v}")
            return '\n'.join(parts)
        return str(data)
    else:
        return ''


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Split text into overlapping chunks (character-based)."""
    if not text:
        return []
    text = text.replace('\r\n', '\n')
    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start = end - overlap
        if start < 0:
            start = 0
    return [c for c in chunks if c]
