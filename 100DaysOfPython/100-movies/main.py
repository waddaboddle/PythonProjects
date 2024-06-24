import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

all_movies = [element.getText() for element in soup.find_all(class_="title", name="h3")]
print(all_movies)

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in reversed(all_movies):
        file.write(f"{movie}\n")
