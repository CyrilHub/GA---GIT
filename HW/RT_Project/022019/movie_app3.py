search_or_ratings = 2
default_movie_list = ["Back to the Future", "Blade", "Spirited Away", "She's the Man", "Rush Hour 2"]

class Movie:
  def __init__(self, movie_data):
    self.movie_data = movie_data


  def get_movie_title(self):
    return self.movie_data["title"]

  def get_movie_rating(self, source="hard_coded"):

    for x in self.movie_data["ratings"]:
        if x["source"] == source:
            return x["value"]

    print("Error: Movie source {} was not found".format(source))
    return None

    def get_api_key():
      api_key = open("secrets.txt","r")
      return
      


def return_single_movie_object(movie_title, movie_rating):
  """ factory method that creates movie objects """
  return Movie({"title": movie_title, "ratings": [{"source": "hard_coded", "value": movie_rating}]})


def print_single_movie_rating(movie_query):
  movie = return_single_movie_object(movie_query, -1)
  print("The rating for" + movie.get_movie_title() + " is " + str(movie.get_movie_rating()))

def print_all_ratings(movie_list):
  for movie in movie_list:
    print("The movie" + movie + "has a great rating!")

def list_search_results(movie_titles):
  for movie in movie_titles:
    print("    "+movie)

def main():
search_or_ratings = None
  while search_or_ratings != "1" and search_or_ratings != "2":
    search_or_ratings = input("Enter a 1 or 2")

  if search_or_ratings == "1":
      list_search_results(default_movie_list)
      break
  elif search_or_ratings == "2":
      print_single_movie_rating("She's the Man")
      break



if __name__ == "__main__":
  main()
