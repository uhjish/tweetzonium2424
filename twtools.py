import tweepy
import pandas as pd
from collections import Counter
from ConfigParser import ConfigParser

class LocationWOE:
    World = 1
    USA = 23424977

#read in the twitter api credentials
config = ConfigParser()
config.read("credentials")
consumer_token = config.get("twitter","consumer_token") 
consumer_secret = config.get("twitter","consumer_secret")

#api-key authentication
auth = tweepy.OAuthHandler( consumer_token, consumer_secret )
#user authentication
#auth.set_access_token( access_token, access_secret )

twapi = tweepy.API(auth)

#cursor based search
#search can take result type "recent", "popular", by default is "mixed"
cxr = tweepy.Cursor(twapi.search, q="Bob Dole", result_type="recent").items(10)

cts = pd.DataFrame( [ (x.text, x.author.screen_name, x.author.followers_count, x.author.friends_count) for x in cxr] )

bag_of_words = " ".join(cts.ix[:,0].values.tolist())

print pd.DataFrame(Counter(bag_of_words.split()).most_common()[:10])

print cts


