from app.rag.rag_service import RAGService
from app.processing.chunking import chunk_text

text = "БФУ предоставляет общежитие..." * 50

chunks = chunk_text(text)

rag = RAGService()
rag.build_index(chunks)

print(rag.answer("Как получить общежитие?"))