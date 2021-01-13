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
character_ranges = [(20, 1), (40, 10), (60, 25), (70, 30), (80, 35), (90, 40), (120, 80), (140, 100)]
character_range = character_ranges[randrange(len(character_ranges))]
for i in range(400):
    title = text_model.make_short_sentence(character_range[0], character_range[1])
    results.append(title)

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
