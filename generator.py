import markovify
from random import randrange
import twitter

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
ln_title = results[rand] + ' #LN_title_bot'

# Post tweet
api = twitter.api()
api.update_status(ln_title)
print("Just tweeted: " + ln_title + ".")
