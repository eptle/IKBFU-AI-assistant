#python -m app.parsers.parser

import requests
from bs4 import BeautifulSoup
from app.processing.clean_text import clean_text

url = "https://kantiana.ru/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

links = soup.find_all("a")

all_links = set()

for link in links:

    href = link.get("href")

    if href:

        if href.startswith("https://kantiana.ru"):

            all_links.add(href)

print(f"Найдено ссылок: {len(all_links)}")

for link in list(all_links)[:30]:
    print(link)

    import json

with open("links.json", "w", encoding="utf-8") as f:
    json.dump(list(all_links), f, ensure_ascii=False, indent=4)


def parse_page(url):

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    title = soup.title.text if soup.title else "No title"

    raw_text = soup.get_text(separator=" ", strip=True)

    text = clean_text(raw_text)

    return {
        "url": url,
        "title": title,
        "content": text
    }

pages = []

for link in list(all_links)[:20]:

    try:

        data = parse_page(link)

        pages.append(data)

        print(f"Спарсил: {link}")

    except Exception as e:

        print(f"Ошибка: {link}")
        print(e)

with open("pages.json", "w", encoding="utf-8") as f:

    json.dump(
        pages,
        f,
        ensure_ascii=False,
        indent=4
    )
