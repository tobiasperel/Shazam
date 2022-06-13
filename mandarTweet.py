import tweepy
from keys import *
client = tweepy.Client(consumer_key= consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)

def escribirTweet(text):
    client.create_tweet(text=text)