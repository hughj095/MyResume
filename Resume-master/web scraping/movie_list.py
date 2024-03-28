from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movies_list = []

for movie in movies:
    check = movie.text
    if check[2] == ":":
        check = check.replace(":",")")
    row = check.split(") ")
    rank = int(row[0])
    mov = row[1]
    rank_mov = [rank,mov]
    movies_list.append(rank_mov)


movies_list.reverse()

with open("./web scraping/movies.txt", mode="w") as file:
    for movies in movies_list:
        movies = str(movies)
        movies = movies.strip("[]")
        file.write(f"{movies}\n")




