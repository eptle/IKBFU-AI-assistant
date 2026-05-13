import json
import random
import re

with open("pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

question_templates = [
    "Расскажи про {}",
    "Что такое {}?",
    "Объясни простыми словами {}",
    "Какая информация есть про {}?",
    "Опиши {}",
    "Для чего используется {}?",
]

def clean_text(text):
    text = re.sub(r"<[^>]+>", "", text)  # HTML
    text = re.sub(r"\s+", " ", text)     # пробелы
    return text.strip()

dataset = []

for page in pages:
    title = page.get("title", "").strip()
    content = page.get("content", "")

    if not title or not content:
        continue

    content = clean_text(content)

    if len(content) < 300:
        continue

    # разбиваем на логические куски
    chunks = [content[i:i+800] for i in range(0, min(len(content), 3000), 800)]

    for chunk in chunks[:2]:  # максимум 2 QA на страницу

        question = random.choice(question_templates).format(title)

        answer = f"Вот информация про {title}:\n\n{chunk}"

        dataset.append({
            "instruction": question,
            "response": answer
        })

with open("app/ml/lora/dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)

print(f"Создано {len(dataset)} QA pairs")