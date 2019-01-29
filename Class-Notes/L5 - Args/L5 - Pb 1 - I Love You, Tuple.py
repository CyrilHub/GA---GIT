# My favorite romance movies
# title, release year, runtime, tagline, main characters
romantic_movie1 = ("The Princess Bride", 1987, 98,
"The story of a man and a woman who lived happily ever after.",
["Buttercup", "Westley", "Fezzik", "Inigo Montoya", "Vizzini"])
romantic_movie2 = ("Groundhog Day", 1993, 101,
"He's having the day of his life… over and over again.",
["Phil Connors"])
romantic_movie3 = ("Amélie", 2001, 122,
"One person can change your life forever.",
["Amélie Poulain", "Nino Quincampoix", "The Garden Gnome"])


print ("Here are my favorite romance movies:")

def print_movie_info (movie):
    print (movie[0], " (", movie [1], "): ", movie [3], sep="")

print_movie_info(romantic_movie1)
print_movie_info(romantic_movie2)
print_movie_info(romantic_movie3)
# Groundhog Day (1993): He's having the day of his life...over and over again.
# Amélie (2001): One person can change your life forever.
