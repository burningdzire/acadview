from twitter import *
import twitter_config as tc

oauth = OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret)
twitter = Twitter(auth = oauth)

query = twitter.search.tweets(q = "india")

print("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"]))
for result in query["statuses"]:
	print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))