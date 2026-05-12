def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    
    i = 0
    while i < len(text):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
        i += chunk_size - overlap

    return chunks

from app.processing.chunking import chunk_text

text = "Очень длинный текст..." * 100

chunks = chunk_text(text)

print(len(chunks))
print(chunks[0])