import sys

blah = []
spam = [{ 'Hola':'1', 'Hoi':"2", 'noun':"3" },{ 'Hola':'5', 'Hoi':"7", 'cat':"10" }]
print type(spam)
print type(spam[0])
print spam
new = []
new = [{'red':'6','blue':"10"}] 
spam = spam + new
print spam

print spam[0]['noun']

keylist = []
small = []
for i in spam:
    small= i.keys()
    keylist = keylist + small
print keylist

uniques = []
uniques = list(set(keylist))
print uniques

"""
name_indexer = dict((p['noun'], i) for i, p in enumerate(spam))
name_indexer.get('3', -1)
"""

#y = {x['noun'] for x in spam}