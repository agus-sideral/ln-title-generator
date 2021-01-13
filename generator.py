import markovify
from random import randrange
import tweepy
from dotenv import load_dotenv
load_dotenv()
import os

# Get raw text as string.
with open("data.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)

# Generate results
results = []
for i in range(100):
    results.append(text_model.make_short_sentence(120, 40))

# Remove duplicates and null results

results = filter(lambda res: res != None, results)
results = list(set(results))

# Generate random number and select result
rand = randrange(len(results))
ln_title = results[rand]

# Post tweet
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)

api.update_status(ln_title)
