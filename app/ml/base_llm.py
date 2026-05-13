from transformers import pipeline

model = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

def answer(question):
    return model(question, max_new_tokens=200)[0]["generated_text"]