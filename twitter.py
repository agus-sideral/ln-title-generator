import tweepy
from dotenv import load_dotenv
load_dotenv()
import os

# Connect with Twitter API

def api():
  auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
  auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
  return tweepy.API(auth)