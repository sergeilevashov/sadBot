import sys
from urllib.request import urlopen
import urllib
import re
import tweepy

url = "http://twitter.com/realDonaldTrump"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
