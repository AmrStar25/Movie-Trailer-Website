class Movie():
    """
    This class help in initiating movie objects
    Args:
        title(str): This is the title of the movie
        poster_image_url(str): This is the url of the movie poster image
        trailer_youtube_url(str): This is the url of the movie trailer video
    """
    def __init__(self, movie_title, poster_url, movie_trailer):
        self.title = movie_title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = movie_trailer
