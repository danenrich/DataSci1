import sys

blah = []
spam = [{ 'Hola':'1', 'Hoi':"2", 'noun':"3" },{ 'Hola':'5', 'Hoi':"7", 'cat':"10" }]
#print type(spam)
#print type(spam[0])
#print spam
new = []
new = [{'red':'6','blue':"10"}] 
spam = spam + new
#print spam

#print spam[0]['noun']

keylist = []
small = []
for i in spam:
    small= i.keys()
    keylist = keylist + small
#print keylist

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

joe = next((item for item in dict1 if item["word"] == "blah2"), None)
for i in dict1:
    if i["word"] == "blah":
        i["count"] = i["count"]+1
 
print dict1
print temp
print joe