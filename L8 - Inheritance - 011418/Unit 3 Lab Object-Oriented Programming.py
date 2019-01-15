movie_title = "Back to the Future"
movie_rating = "8"
search_or_ratings = 1
default_movie_list = ["Back to the Future", "Blade", "Spirited Away", "She's the Man", "Rush Hour 2"]


def print_movie_title():
  print(movie_title)

def print_movie_rating():
  print(movie_rating)

def print_single_movie_rating():
  print("The rating for " + movie_title + " is " + movie_rating)

def print_all_ratings(movie_list):
  for movie in movie_list:
    print("The movie", movie, "has a great rating!")

def list_search_results(movie_titles):
  for movie in movie_titles:
    print("    "+movie)

def main():
  if search_or_ratings == 1:
    list_search_results(default_movie_list)
  elif search_or_ratings == 2:
    print_movie_rating()
  else:
    print_single_movie_rating()

  print_all_ratings(default_movie_list)



if __name__ == "__main__":
  main()
