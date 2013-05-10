import sys
import string

spamfancy = {"place":{"country":"United States", "country_code":"US", "full_name":"Washington, DC"}}
print spamfancy["place"]["country"]


sam = {'count': 1, 'word': u'\U0001f602&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;'}
s = sam["word"]
joe = filter(lambda x: x in string.printable, s)
control_chars = ''.join(map(unichr, range(0,32) + range(127,160)))
print s.encode("utf-8")
#print sam["word"]

blah = []
string = 'blah'
blah = blah + [string]
print blah

fp = 100
fp = fp / 8
print fp

spam = [{ 'Hola':'1', 'Hoi':"2", 'noun':"3" },{ 'Hola':'5', 'Hoi':"7", 'cat':"10" }]
#print type(spam)
#print type(spam[0])
#print spam
new = []
new = [{'red':'6','blue':"10"}] 
spam = spam + new
print spam[1]['Hola']

#print spam[0]['noun']

keylist = []
small = []
for i in spam:
    small= i.keys()
    keylist = keylist + small
print keylist

uniques = []
uniques = list(set(keylist))
#print uniques

"""
name_indexer = dict((p['noun'], i) for i, p in enumerate(spam))
name_indexer.get('3', -1)
"""
dict1 = []
temp = []
counter = 1 
temp = {
    "word":"blah",
    "score":4,
    "count":counter,
}
dict1.append(temp)
counter =counter + 1 
temp = {
    "word":"blah2",
    "score":-2,
    "count":counter,
}
dict1.append(temp)

#joe = next((item for item in dict1 if item["word"] == "blah2"), None)
for i in dict1:
    if i["word"] == "blah":
        i["count"] = i["count"]+1
        print i["count"]
#joe = dict1.get("word"'blah2')
 
print dict1
print temp
#print joe