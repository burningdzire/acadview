from twitter import *
import twitter_config as tc

oauth = OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret)
twitter = Twitter(auth = oauth)

source = "_burningdzire"
target = "chetan_bhagat"

result = twitter.friendships.show(source_screen_name = source,target_screen_name = target)

following = result["relationship"]["target"]["following"]
follows   = result["relationship"]["target"]["followed_by"]

print("%s following %s: %s" % (source, target, follows))
print("%s following %s: %s" % (target, source, following))