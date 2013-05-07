import oauth2 as oauth
import urllib2 as urllib

#twitter app: dgsmith73_dsassign1 https://dev.twitter.com/apps/4370674/show

# See Assginment 6 instructions or README for how to get these credentials
access_token_key = "491972754-q4z0xldbz8F4Mw2c1Z1V3PKtkfWovHdDwGEdtslc"
access_token_secret = "W2bjnSsaNNDv8Hfam9ZpfgW2oIKcEtf5TpaWGIlNZKE"

consumer_key = "nnX1NF3Ph9dLyS5sq4c0g"
consumer_secret = "49lB6Uw3O2zNEcm2OZtxuCL0bKqQeJSSytp5JTijU"

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
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()
