import datetime

class Movie(object):
    """
    Represents a movie

    __init__
    Args:
        title (str): Title of the movie.
        poster_image_url (str): The url where the movie poster image is located.
        trailer_youtube_url (str): The youtube url for the movie's trailer.
        release_date (Optional[datetime]): The movie's USA release date.  The default value is today's date.

    Attributes: (All Args can be retrieved using the same instance variable name)
    
        release_date_pretty_print (str): The release_date variable printed in a nice format.
        
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url, release_date=datetime.datetime.today()):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date
        self.release_date_pretty_print = release_date.strftime('%B %d, %Y')
