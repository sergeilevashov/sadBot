import sys
from urllib.request import urlopen
import urllib
import re
import tweepy
import keys

print('welcome to the Donald Trump Twitter sad! bot. feel free to search for sad!, or any other word...')

flag = False
user_input = ''
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token= keys.access_token
access_token_secret= keys.access_token_secret

def findSad(tweet):
    return re.compile(r'\b({0})\b'.format(tweet), flags=re.IGNORECASE).search

user_input = input('enter the word to search for:')

url = "http://twitter.com/realDonaldTrump"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
maxtweets = api.user_timeline(user_id = '25073877' ,count=200)
for status in maxtweets:
    if findSad(user_input)(status.text.lower()):
        print(status.text)
        flag = True
if not flag:
    print('he hasnt said that word... at least not on twitter')