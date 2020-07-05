import json, flask
import random
import tweepy
from os import environ

#CUSTOMER_KEY = API_KEY
#CUSTOMER_SECRET = API_SECRET_KEY
#ACCESS_KEY = ACCESS_TOKEN
#ACCESS_SECRET = ACCESS_TOKEN_SECRET

CUSTOMER_KEY = environ['API_KEY']
CUSTOMER_SECRET = environ['API_SECRET_KEY']
ACCESS_KEY = environ['ACCESS_TOKEN']
ACCESS_SECRET = environ['ACCESS_TOKEN_SECRET']

with open('quotes.json') as json_file:
    data = json.load(json_file)

randquote = random.choice(data)

print("type = ",type(randquote))
print(randquote['author'], "-> " + randquote['text'])
tweet = "{} -> {}".format(randquote['author'], randquote['text'])

auth = tweepy.OAuthHandler(CUSTOMER_KEY, CUSTOMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(tweet)
