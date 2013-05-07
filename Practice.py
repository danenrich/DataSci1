'''
Created on May 6, 2013

@author: dan
'''
"""
import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
print (json.load(response))
"""

import urllib
import json

#response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")

for i in range(10):
    qstring = "http://search.twitter.com/search.json?q=microsoft@page=" + str(i+1)
    response = urllib.urlopen("http://search.twitter.com/search.json?q=@hankschulman")
    jsondata = json.load(response)
    print jsondata
    
    results = jsondata['results']
    for t in results:
        print t['text'],"\n"
