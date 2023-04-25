import requests
import os
from bs4 import BeautifulSoup

genre = "horror"

if genre == "sve":
    url = "https://books.toscrape.com/catalogue/category/books/"
else:
    url = f"https://books.toscrape.com/catalogue/category/books/{genre}_31/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

if genre == "sve":
    genres = [link.get("href").split("/")[-2] for link in soup.select("div.side_categories > ul > li > ul > li > a")]
    for genre in genres:
        os.makedirs(genre, exist_ok=True)
        for i in range(1, 51):
            url = f"https://books.toscrape.com/catalogue/category/books/{genre}_31/page-{i}.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            books = soup.select("article.product_pod")
            if not books:
                break
            for book in books:
                title = book.h3.a["title"].replace(":", "")
                img_url = book.img["src"].replace("../..", "https://books.toscrape.com")
                response = requests.get(img_url)
                with open(f"{genre}/{title}.jpg", "wb") as f:
                    f.write(response.content)
else:
    os.makedirs(genre, exist_ok=True)
    books = soup.select("article.product_pod")
    for book in books:
        title = book.h3.a["title"].replace(":", "")
        img_url = book.img["src"].replace("../..", "https://books.toscrape.com")
        response = requests.get(img_url)
        with open(f"{genre}/{title}.jpg", "wb") as f:
            f.write(response.content)
