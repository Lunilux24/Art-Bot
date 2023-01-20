import tweepy
import keys

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_secret)
    
    return tweepy.API(auth)

