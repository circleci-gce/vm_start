# coding:utf-8

import os
import sys
import tweepy

args = sys.argv

# Create twitter objects
auth = tweepy.OAuthHandler(args[1], args[2])
auth.set_access_token(args[3], args[4])
api = tweepy.API(auth)

# Create message body
URL = os.environ['CIRCLE_BUILD_URL']
INSTANCE_IP = os.environ['INSTANCE_IP']

message = 'CircleCI started an VM instance' + '\n\n' \
          + INSTANCE_IP + '\n\n' \
          + URL

api.send_direct_message(args[5], message)
