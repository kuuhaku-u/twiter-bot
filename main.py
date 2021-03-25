###########--library---##############

import tweepy
import os

#######-key_sec--###########
auth = tweepy.OAuthHandler(os.getenv('consumer_key'),
                           os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('key'), os.getenv('secret'))


api = tweepy.API(auth)
api.update_status('I am Alive')