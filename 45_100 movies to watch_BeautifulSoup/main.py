import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movies = []
for movie in all_movies:
    movies.append(movie.getText())

asc_movies = movies[::-1]

for item in asc_movies:
    with open("movies_to_watch.txt", "a+") as file:
        file.write("\n")
        file.write(item)








