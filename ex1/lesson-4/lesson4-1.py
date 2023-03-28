import requests
from bs4 import BeautifulSoup

url = "https://dantri.com.vn/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
author = soup.find("meta", {"name": "author"})
title = soup.find("meta", {"property": "og:title"})
description = soup.find("meta", {"name": "description"})
url = soup.find("meta", {"property": "og:url"})
coppyright = soup.find("meta", {"name": "copyright"})

print("Author: ", author["content"])
print("Title: ", title["content"])
print("Description: ", description["content"])
print("URL: ", url["content"])
print("COPPY RIGHT: ", coppyright["content"])