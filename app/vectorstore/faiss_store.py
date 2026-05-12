import faiss
import numpy as np


class VectorStore:
    def __init__(self, dim=768):
        self.index = faiss.IndexFlatL2(dim)
        self.data = []

    def add(self, vectors, texts):
        self.index.add(np.array(vectors).astype("float32"))
        self.data.extend(texts)

    def search(self, query_vector, k=3):
        D, I = self.index.search(
            np.array([query_vector]).astype("float32"), k
        )
        return [self.data[i] for i in I[0]]