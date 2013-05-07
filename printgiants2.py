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


qstring = "http://search.twitter.com/search.json?q=@hankschulman&count=20"
response = urllib.urlopen(qstring)
jsondata = json.load(response)
#print jsondata
results = jsondata['results']
text_file = open("giants_out.txt", "w")
for t in results:
    line = str(repr(t['text']))
    text_file.write("%s\n" % line)

text_file.close()