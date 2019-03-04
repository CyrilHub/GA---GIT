import requests
from flask import Flask, render_template, request


search_or_ratings = 2
default_movie_list = ["Back to the Future", "Blade", "Spirited Away", "She's the Man", "Rush Hour 2"]


class OMDBApi:

    def list_search_result_request(self,search_string):
        response = requests.get("http://www.omdbapi.com/",{"apikey":get_api_key(), "s":search_string})
        result = []
        if response.json()["Response"] == "False":
          return []

        for movie in response.json()["Search"]:
          # return a movie object into the result list
          result.append(Movie(movie))
        return result

    def fetch_single_movie_by_id(self,movie_id):
        # requests formats the URL for you, order of parameters doesn't matter because passing in via dictionary
        response = requests.get("http://www.omdbapi.com/",{"apikey":get_api_key(), "i":movie_id})
        return Movie(response.json())

    def fetch_single_movie_by_title(self,movie_title):
        response = requests.get("http://www.omdbapi.com/",{"apikey":get_api_key(), "t":movie_title})
        x = response.json()
        return Movie(x)


# Movie object has the following keys:
# imdbID
# Title
# Ratings
class Movie:
  def __init__(self, movie_data):
    self.movie_data = movie_data

  def get_movie_id(self):
    return self.movie_data["imdbID"]

  def get_movie_title(self):
    return self.movie_data["Title"]

  def get_movie_year(self):
    return self.movie_data["Year"]

  def get_movie_poster(self):
    return self.movie_data["Poster"]

  def get_movie_rating(self, source="hard_coded"):

    for x in self.movie_data["Ratings"]:
        if x["Source"] == source:
            return x["Value"]

    print("Error: Movie source {} was not found".format(source))
    return None


# def print_single_movie_rating(movie_query):
#   movie = return_single_movie_object(movie_query, -1)
#   print("The rating for" + movie.get_movie_title() + " is " + str(movie.get_movie_rating()))

def print_all_ratings(movie_list):
  for movie in movie_list:
    print("The movie" + movie + "has a great rating!")

def list_search_results(movie_titles):
  for movie in movie_titles:
    print("    "+movie)

def get_api_key():
    fo = open("secrets.txt")
    return fo.read().strip()

def main():
  search_or_ratings = input("enter 1 or 2:: ").strip()
  api = OMDBApi()
  while True:
    if search_or_ratings == "1":
        search_string = input("Enter a search term: ")
        movies = api.list_search_result_request(search_string)
        for x in movies:
          print(x.get_movie_title())
        print("End of list")
        break
    elif search_or_ratings == "2":
        movie = api.fetch_single_movie_by_title(input("Enter a movie title: "))
        print("The rating for {} is {}".format(movie.get_movie_title(), movie.get_movie_rating("Rotten Tomatoes")))
        break
    else:
        search_or_ratings = input("Error:: Enter a 1 or a 2:: ")

app = Flask(__name__)
@app.route("/")
def home():
    user = "Cyril"
    return render_template("index.html", name=user)

if __name__ == "__main__":
    app.run(debug=True)

#Code to test if API is reponding
  # x = OMDBApi()
  # movie = x.fetch_single_movie_by_title("star")
  # print(movie.get_movie_title(), movie.get_movie_id())