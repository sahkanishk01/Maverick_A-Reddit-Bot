import config
import praw

reddit = None

def init_reddit_connection():
    global reddit
    reddit = praw.Reddit(
            client_id = config.CLIENT_ID,
            client_secret = config.CLIENT_SECRET,
            refresh_token = config.ACCESS_TOKEN,
            user_agent = config.USERAGENT,
            user_name = config.USERNAME,
            password = config.PASSWORD
        )


