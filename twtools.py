import tweepy
import pandas as pd
from ConfigParser import ConfigParser

class LocationWOE:
    World = 1
    USA = 23424977

#read in the twitter api credentials
config = ConfigParser()
config.read("credentials")
consumer_token = config.get("twitter","consumer_token") 
consumer_secret = config.get("twitter","consumer_secret")
#access_token = config.get("twitter","access_token")
#access_secret = config.get("twitter","access_secret")

#api-key authentication
auth = tweepy.OAuthHandler( consumer_token, consumer_secret )
#user authentication
#auth.set_access_token( access_token, access_secret )

twapi = tweepy.API(auth)

#cursor based search
cxr = tweepy.Cursor(twapi.search, q="Bob Dole", result_type="recent").items(10)

cts = pd.DataFrame( [ (x.author.screen_name, x.author.followers_count, x.author.friends_count) for x in cxr] )
cts = cts.drop_duplicates()

print cts


