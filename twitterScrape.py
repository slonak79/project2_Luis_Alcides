import oauth2 as oauth
import urllib2 as urllib
import re
import io
import time
import datetime

access_token_key = "277176492-nWAWzJ4XcLjbCDZycv1dGr9xYGAeq0dWr3hQoTrE"
access_token_secret = "Jv7RS0Rk0EhlhVVSNQLEDAa883Fa9LgEFtM5w3qu6yoPI"

consumer_key = "A1ZvJ87SDhGXO4T0dCHBw"
consumer_secret = "iYOonEQm2KwsVAOYeHR3p700OU69pfLLp9QO6acMs"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  ts = time.time()
  stringTime = datetime.datetime.fromtimestamp(ts).strftime("%Y-%d_%H:%M:%S")
  tweetFile = open("/Users/sorto/Desktop/project2_Luis_Alcides/tweets/" + stringTime + ".txt", "a")

  url = "https://stream.twitter.com/1/statuses/filter.json?locations=-180,-90,180,90"

  parameters = []
  response = twitterreq(url, "POST", parameters)
  for line in response:
      tweetFile.write(line.strip()+'\n')
    
#print(line.strip())


if __name__ == '__main__':
  fetchsamples()























