import tweepy
from dotenv import load_dotenv
load_dotenv()
import os

# Connect to Twitter
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

# Create Friendship uwu (Follow followers)
# Find followers
follower_ids = []
for follower in tweepy.Cursor(api.followers).items():
    if follower.following == False:
      follower_ids.append(follower.id)
# Create friendship
for follower_id in follower_ids:
  api.create_friendship(follower_id)

# Destroy frienships x.x (Unfollow unfollowers)
for friend in tweepy.Cursor(api.friends_ids).items():
    friendship = api.show_friendship(source_id=os.getenv("ACCOUNT_ID"), target_id=str(friend))
    if friendship[0].followed_by == False:
      api.destroy_friendship(friend)