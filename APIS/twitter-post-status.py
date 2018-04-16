from twitter import *
import twitter_config as tc

oauth = OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret)
twitter = Twitter(auth = oauth)

new_status = "Hola mi amigo"
results = twitter.statuses.update(status = new_status)
print "updated status: %s" % new_status