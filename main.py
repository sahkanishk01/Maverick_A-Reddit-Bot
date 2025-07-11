import configparser as config
import praw
import time
from instances import replying_jokes,news
from reddit_connection import init_reddit_connection
import reddit_connection

functions = [replying_jokes,news]

if __name__ == '__main__':
    init_reddit_connection()
    reddit = reddit_connection.reddit
    # now get some posts and try to reply as well as possible
    while True:
        subreddit = reddit.subreddit('iliekcomputers')
        posts = []
        for submission in subreddit.hot(limit=10):
                posts.append(submission)
        for f in functions:
            f(posts, reddit)
        time.sleep(7)


