import tweepy
import keys
import random as r
import json
import time
from random_user import get_random_user

auth = tweepy.OAuth1UserHandler(
   keys.api_key, keys.api_secret, keys.access_token, keys.access_secret
)

api = tweepy.API(auth)
    
def get_tweet_id():
   auth = tweepy.OAuth1UserHandler(
   keys.api_key, keys.api_secret, keys.access_token, keys.access_secret
   )

   api = tweepy.API(auth)

   # Get tweets from a specific account

   while True:
      tweets = api.user_timeline(screen_name=get_random_user(), count=5)

      for tweet in tweets:
         if(not tweet.in_reply_to_status_id):
            return tweet.id_str if not hasattr(tweet, "retweeted_status") else tweet.retweeted_status.id_str
