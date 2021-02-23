import tweepy
import praw

API_KEY
API_SECRET_KEY
ACCESS_TOKEN
ACCESS_SECRET

REDDIT_SECRET
REDDIT_PERSONAL


auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

reddit = praw.Reddit(client_id = REDDIT_PERSONAL, client_secret = REDDIT_SECRET, user_agent = '<console:harriBot:1.0')

try:
    api.verify_credentials()
except:
    print("Error during authentication")

#obtain LPT subreddit and top post of the day as a string

def obtainTweet():
    subreddit = reddit.subreddit("LifeProTips")
    for submission in subreddit.top("day", limit = 1):
        post = submission.title
        credit = submission.author
        parsed_post = post.split(' ', 1)
        content = parsed_post[1]
        tweet = content + "\n\nCredit: " + credit.name + "\n\nhttps://www.reddit.com" + submission.permalink
        return tweet

api.update_status(obtainTweet())



