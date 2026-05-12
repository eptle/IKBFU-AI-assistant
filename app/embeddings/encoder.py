from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/multilingual-e5-base")


def get_embedding(text: str):
    return model.encode(text)