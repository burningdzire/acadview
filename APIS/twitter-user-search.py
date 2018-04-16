from twitter import *
import twitter_config as tc

oauth = OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret)
twitter = Twitter(auth = oauth)

results = twitter.users.search(q = 'India')

for user in results:
	print("@%s\t(%s):\t%s" % (user["screen_name"], user["name"], user["location"]))
