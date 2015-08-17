import tweepy
import pandas as pd
import requests
from collections import Counter
from ConfigParser import ConfigParser
import urlparse
import httplib

# Recursively follow redirects until there isn't a location header
def resolve_http_redirect(url, depth=0):
    if not url:
        #cover the case when no url comes in from a batch/apply job
        return (None, None)
    if depth > 10:
        return (url, depth)
    o = urlparse.urlparse(url,allow_fragments=True)
    conn = httplib.HTTPConnection(o.netloc)
    path = o.path
    if o.query:
        path +='?'+o.query
    conn.request("HEAD", path)
    res = conn.getresponse()
    headers = dict(res.getheaders())
    if headers.has_key('location') and headers['location'] != url:
        return resolve_http_redirect(headers['location'], depth+1)
    else:
        return (url, depth)

def get_first_url( status ):
    urls = status.entities["urls"]
    if len(urls) > 0:
        return urls[0]["expanded_url"]
    return None

class LocationWOE:
    World = 1
    USA = 23424977

#def resolve_terminal_url(start_url):
#    resp = requests.get(start_url)
#    return resp

#retrieve upto 5000 friends for the given user
def get_friend_ids_for_user(  user ):
    assert isinstance(user, tweepy.User), "%r is not a tweepy.User" % user
    return twapi.friends_ids(user_id=user)


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
cxr = tweepy.Cursor(twapi.search, q="#TheStrain filter:links", result_type="recent").items(100)

res = [x for x in cxr]

cts = pd.DataFrame( [ (x.text, x.author.screen_name, x.author.followers_count, x.author.friends_count) for x in res] )

bag_of_words = " ".join(cts.ix[:,0].values.tolist())

url_hops = [ resolve_http_redirect( get_first_url(x) ) for x in res ]
url_hops = pd.DataFrame(url_hops)
url_hops.columns = ["url","hops"]
url_summ = url_hops.groupby("url").agg([np.max, len])

print pd.DataFrame(Counter(bag_of_words.split()).most_common()[:10])

print cts


