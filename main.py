import tweepy
import keys


#def api():
   # auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
   # auth.set_access_token(keys.access_token, keys.access_secret)
    
   # return tweepy.API(auth)

auth = tweepy.OAuth1UserHandler(
   keys.api_key, keys.api_secret, keys.access_token, keys.access_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
