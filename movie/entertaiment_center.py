import index
import media

toy_story = media.Movie("Toy Story", "Some description of the movie here",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "Some description of the movie here",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

predator = media.Movie("Predator", "Some description of the movie here",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Predator_%281987%29_-_The_Predator.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

the_edge_of_tomorrow = media.Movie("The Edge of Tomorrow", "Some description of the movie here",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

independence_day = media.Movie("Indepence Day", "Some description of the movie here",
                        "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

fury = media.Movie("Fury", "Some description of the movie here",
                        "https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

movies = [toy_story, avatar, predator, the_edge_of_tomorrow, independence_day, fury]
index.open_movies_page(movies)
