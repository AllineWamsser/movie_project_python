import json

def get_movies():
    with open("data.json","r") as file:
      return json.load(file)

def save_movies(movies):
    with open("data.json","w") as file:
      json.dump(movies, file)


def add_movie(title, year, rating):
   movies = get_movies()
   movies[title] = {"year": year, "rating":rating}
   save_movies(movies)


def delete_movie(title):
    movies = get_movies()
    if title in movies:
      del movies[title]
      save_movies(movies)


def update_movie(title, rating):
    movies = get_movies()
    if title in movies:
      movies[title]["rating"] = rating
      save_movies(movies)
  