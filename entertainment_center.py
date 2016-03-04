import datetime
import fresh_tomatoes
import media

# Create Movie instances of some of my favorite movies (6 instances created)
movie1 = media.Movie("Shawshank Redemption",
                     "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                     "https://www.youtube.com/watch?v=NmzuHjWmXOc",
                     datetime.datetime(1994, 9, 23))
movie2 = media.Movie("The Dark Knight",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                     datetime.datetime(2008, 7, 14))
movie3 = media.Movie("Inception",
                     "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                     "https://www.youtube.com/watch?v=YoHD9XEInc0",
                     datetime.datetime(2010, 7, 16))
movie4 = media.Movie("Inglorious Basterds",
                     "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                     "https://www.youtube.com/watch?v=KnrRy6kSFF0",
                     datetime.datetime(2009, 9, 21))
movie5 = media.Movie("Moneyball",
                     "https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg",
                     "https://www.youtube.com/watch?v=-4QPVo0UIzc",
                     datetime.datetime(2012, 2, 16))
movie6 = media.Movie("Jurassic Park",
                     "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                     "https://www.youtube.com/watch?v=lc0UehYemQA",
                     datetime.datetime(1993, 6, 11))

# Create array of Movie objects
movies = [movie1, movie2, movie3, movie4, movie5, movie6]

# Create html file and open in web browser
fresh_tomatoes.open_movies_page(movies)

