import markovify
from random import randrange
import tweepy

# Get raw text as string.
with open("data.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)

# Print three randomly-generated sentences of no more than 280 characters
results = []
for i in range(100):
    results.append(text_model.make_short_sentence(120, 40))

rand = randrange(99)

ln_title = results[rand]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(ln_title)
