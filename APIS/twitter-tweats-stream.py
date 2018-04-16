import json
from twitter import *
import twitter_config as tc

oauth = OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret)
twitter = TwitterStream(auth = oauth)

iterator = twitter.statuses.sample()
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    print(json.dumps(tweet))    
    if tweet_count <= 0:
        break 
