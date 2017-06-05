import sys
from urllib.request import urlopen
import urllib
import re
import tweepy
import keys

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token= keys.access_token
access_token_secret= keys.access_token_secret
url = "http://twitter.com/realDonaldTrump"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
