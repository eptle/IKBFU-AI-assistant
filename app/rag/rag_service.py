from app.embeddings.encoder import get_embedding
from app.vectorstore.faiss_store import VectorStore


class RAGService:
    def __init__(self):
        self.vs = VectorStore()

    def build_index(self, chunks):
        vectors = [get_embedding(c) for c in chunks]
        self.vs.add(vectors, chunks)

    def answer(self, question):
        q_vec = get_embedding(question)

        docs = self.vs.search(q_vec)

        context = "\n".join(docs)

        prompt = f"""
Контекст:
{context}

Вопрос:
{question}

Ответь только по контексту.
"""

        return prompt