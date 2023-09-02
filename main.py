import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.select("h3")
titles.reverse()
with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles:
        file.write(str(title.text) + "\n")


