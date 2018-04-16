from twitter import *
import twitter_config as tc

oauth = OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret)
twitter = Twitter(auth = oauth)

user = "Google"

results = twitter.statuses.user_timeline(screen_name = user)

for status in results:
	print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))