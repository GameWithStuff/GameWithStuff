from newsapi import NewsApiClient
import requests
from bs4 import BeautifulSoup
from sys import exit


def get_all_text(element):
    text = ""
    if element.get_text():
        text += element.get_text().strip()
    return text
with open("API.txt", "r") as a:
    api = a.read()
try:
    api = NewsApiClient(api_key=api)
    news = api.get_top_headlines(country="in")
except:
    print('Invalid API Key in API.txt')
    exit()

try:
    while True:
        topic = input('What topic do you want the headlines about or leave empty for all types of headlines:\n')
        news = api.get_top_headlines(country="in",q=topic)
        if news["status"] == "ok":
            print("Top Headlines:")
            for article in list(news["articles"]):
                if article["content"]:
                    content = article["content"].strip()
                    if "[" in content:
                        url = article["url"]
                        soup = BeautifulSoup(requests.get(url=url).content, "html.parser")
                        articleTags = soup.find_all("article")
                        if article["content"]:
                            print("\n")
                        all_text = []
                        for tag in articleTags:
                            all_text.append(get_all_text(tag))
                        for text in all_text:
                            try:
                                start = content[: content.find("...")]
                                if content.startswith(start):
                                    content = text
                                    break
                            except:
                                pass
                        else:
                            content = ""
                        if content:
                            print("Title:\n", article["title"],sep='')
                            print("\n")
                            print("Article:")
                            print(content)
                            if article["description"]:
                                print("Description:\n", article["description"],sep='')
                            print(f"For more information go to:\n{url}")
                            print("-"*50)

        else:
            print("Error")

except Exception as e:
    print(e)
finally:
    while True:
        pass
