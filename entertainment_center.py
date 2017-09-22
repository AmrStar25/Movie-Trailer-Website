import media                    # the module that contain Movie class
import fresh_tomatoes           # the module that contain open_movies_page

# create six different movie instances from Movie class

toy_story = media.Movie("Toy Story",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                   "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                           "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

bat_man = media.Movie("Batman Begins",
                       "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

hunger_games = media.Movie("Hunger Games",
                         "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=4S9a5V9ODuY")

lord_of_rings = media.Movie("Lord of the Rings",
                          "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=Pki6jbSbXIY")

# adding the created movies to one array
movies = [toy_story, avatar, school_of_rock, bat_man, hunger_games, lord_of_rings]

# call this method with movies array to render
# the movie trialer page with our movies
fresh_tomatoes.open_movies_page(movies)
