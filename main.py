import tweepy
import keys
import random as r
import json
import time
import Users_and_access_time

auth = tweepy.OAuth1UserHandler(
   keys.api_key, keys.api_secret, keys.access_token, keys.access_secret
)

api = tweepy.API(auth)
    
def request():
   auth = tweepy.OAuth1UserHandler(
   keys.api_key, keys.api_secret, keys.access_token, keys.access_secret
   )

   api = tweepy.API(auth)
   
   #x = Users_and_access_time.random_user()
   # Get tweets from a specific account
   tweets = api.user_timeline(screen_name= "zutsuuyaku1", count=1)
    
   return tweets[0].extended_entities['media'][0]['expanded_url']
