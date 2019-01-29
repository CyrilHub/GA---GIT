class Band:

    number_of_bands = 0

    def __init__(self, band_name, albums_released = 0, genre = ""):

        self.band_name = band_name
        self.albums_released = albums_released
        self.genre = genre
        number_of_bands += 1

    def print_stats (self):
        print ("The rock band ", self.band_name, "has", self.albums_released, " albums")

queen = Band("Queen", 15, "rock")

queen.print_stats()
