import tweepy
from dotenv import load_dotenv
load_dotenv()
import os
import twitter

# Connect to Twitter
api = twitter.api()

# Create Friendship uwu (Follow followers)
for follower in tweepy.Cursor(api.followers).items():
    if not follower.following and not follower.protected:
      api.create_friendship(follower.id)
      print("Now " + follower.screen_name + " is my best friend.")

# Destroy frienships x.x (Unfollow unfollowers)
for friend in tweepy.Cursor(api.friends_ids).items():
    friendship = api.show_friendship(source_id=os.getenv("ACCOUNT_ID"), target_id=str(friend))
    if not friendship[0].followed_by:
      api.destroy_friendship(friend)
      print("Friendship ended with " + friendship[1].screen_name + ".")