from twitter import *
import twitter_config as tc

oauth = OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret)
twitter = Twitter(auth = oauth)

username = "_burningdzire"

query = twitter.friends.ids(screen_name = username)

print("found %d friends" % (len(query["ids"])))

for n in range(0, len(query["ids"]), 100):
	ids = query["ids"][n:n+100]
	subquery = twitter.users.lookup(user_id = ids)

	for user in subquery:
		print(" [%s] %s - %s" % ("*" if user["verified"] else " ", user["screen_name"], user["location"]))