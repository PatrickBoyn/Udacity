import webbrowser

# This was done using Python 3.6, however it should run in 2.7,


class Movie():
    """This class provides a way of storing movie information """

    # This initializes the various bits of information
    # used in naming the movies and other stats
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image_url,
                 trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # This will play the trailers for the various movies.

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
