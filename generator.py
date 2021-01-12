import markovify
from random import randrange

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
print(rand)
print(results[rand])