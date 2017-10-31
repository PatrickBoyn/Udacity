import media
import fresh_tomatoes

# This was done using Python 3.6, but should work fine in 2.7.
# These variables are movies names and info,
# along with images from their posters.
toy_story = media.Movie("Toy Story",
                        "A story of what toys do when you're not around.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

star_wars = media.Movie("Star Wars",
					   "A few good guys go after the evil guys", 
					   "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
					   "https://www.youtube.com/watch?v=vP_1T4ilm8M")

dark_knight = media.Movie("The Dark Knight",
                          "Batman vs the Joker",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

matrix = media.Movie("The Matrix",
                     "A guy finds out life isn't exactly what he thought",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

robin  =  media.Movie("Robin Hood Men in Tights",
                      "It's not your typical Robin Hood story.",
                      "https://upload.wikimedia.org/wikipedia/en/1/12/RobinHoodMeninTights_Poster.jpg",
                      "https://www.youtube.com/watch?v=K5q6U1cK3aU")

amelie = media.Movie("Amélie",
                     "C'est la vie. ",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=oWedygCWODY")

# This is a list of those variables so I can store them in fresh_tomatoes.
movies = [toy_story,
          star_wars,
          dark_knight,
          matrix,
          robin,
          amelie]

# This creates and opens up a website.
# I didn't name the fresh_tomatoes file.
# The try and except makes it so that
# I can more easily see what the actual error is.
try:
    fresh_tomatoes.open_movies_page(movies)
except Exception as e:
    print(e)
