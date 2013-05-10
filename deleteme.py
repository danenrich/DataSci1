import sys
import string
import collections

hashtagfrenzy = {"created_at":"Tue May 07 00:19:46 +0000 2013","id":331563975848386560,"id_str":"331563975848386560","text":"@KatherineGrum holy hell that sucks!","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":331547904982544384,"in_reply_to_status_id_str":"331547904982544384","in_reply_to_user_id":391176732,"in_reply_to_user_id_str":"391176732","in_reply_to_screen_name":"KatherineGrum","user":{"id":564757541,"id_str":"564757541","name":"Bren Bren","screen_name":"brenna_ambrozy","location":"","url":null,"description":"*place something inspirational here*","protected":false,"followers_count":341,"friends_count":288,"listed_count":0,"created_at":"Fri Apr 27 16:55:54 +0000 2012","favourites_count":2899,"utc_offset":-21600,"time_zone":"Central Time (US & Canada)","geo_enabled":true,"verified":false,"statuses_count":5162,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"070608","profile_background_image_url":"http:\/\/a0.twimg.com\/profile_background_images\/703657985\/0ab1ee88313332ba263dc50c9b5d0735.jpeg","profile_background_image_url_https":"https:\/\/si0.twimg.com\/profile_background_images\/703657985\/0ab1ee88313332ba263dc50c9b5d0735.jpeg","profile_background_tile":false,"profile_image_url":"http:\/\/a0.twimg.com\/profile_images\/3579096396\/7907778ace5c149aa6bcaea595916343_normal.jpeg","profile_image_url_https":"https:\/\/si0.twimg.com\/profile_images\/3579096396\/7907778ace5c149aa6bcaea595916343_normal.jpeg","profile_banner_url":"https:\/\/si0.twimg.com\/profile_banners\/564757541\/1366904767","profile_link_color":"6A16C9","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":false,"default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":{"type":"Point","coordinates":[41.70537464,-83.69776095]},"coordinates":{"type":"Point","coordinates":[-83.69776095,41.70537464]},"place":{"id":"7fdb4e2d9b715f29","url":"http:\/\/api.twitter.com\/1\/geo\/id\/7fdb4e2d9b715f29.json","place_type":"city","name":"Sylvania","full_name":"Sylvania, OH","country_code":"US","country":"United States","bounding_box":{"type":"Polygon","coordinates":[[[-83.744381,41.688975],[-83.744381,41.726622],[-83.665377,41.726622],[-83.665377,41.688975]]]},"attributes":{}},"contributors":null,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"symbols":[],"urls":[],"user_mentions":[{"screen_name":"KatherineGrum","name":"Katherine Grum","id":391176732,"id_str":"391176732","indices":[0,14]}]},"favorited":false,"retweeted":false,"filter_level":"medium","lang":"en"}



hashtagfrenzy = ['#SFGiants defeat the #Phillies 4-3 on #Mom Andres Torres 4th career walk-off hit','Great day for @BenefitBeauty #gifts at #SFGiants stadium! Bring #Mom and make #MothersDay a great one! #eBayNow']
hashlist = []
hashtemp = []
for hashy in hashtagfrenzy:
    hashtemp = list(set(part for part in hashy.split() if part.startswith('#')))
    hashlist = hashlist + hashtemp
print hashlist
"""
uniques = []
uniques = list(set(hashlist))
print uniques
"""
freqtable = collections.Counter(hashlist)
sorttable = sorted(freqtable.items(), key=lambda item: item[1], reverse=True)
print sorttable
smalltable = sorttable[:3]
print smalltable


spamfancy = {"place":{"country":"United States", "country_code":"US", "full_name":"Washington, DC"}}
#print spamfancy["place"]["country"]


sam = {'count': 1, 'word': u'\U0001f602&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;'}
s = sam["word"]
joe = filter(lambda x: x in string.printable, s)
control_chars = ''.join(map(unichr, range(0,32) + range(127,160)))
#print s.encode("utf-8")
#print sam["word"]

blah = []
string = 'blah'
blah = blah + [string]
#print blah

fp = 100
fp = fp / 8
#print fp

spam = [{ 'Hola':'1', 'Hoi':"2", 'noun':"3" },{ 'Hola':'5', 'Hoi':"7", 'cat':"10" }]
#print type(spam)
#print type(spam[0])
#print spam
new = []
new = [{'red':'6','blue':"10"}] 
spam = spam + new
#print spam[1]['Hola']

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

#joe = next((item for item in dict1 if item["word"] == "blah2"), None)
for i in dict1:
    if i["word"] == "blah":
        i["count"] = i["count"]+1
        #print i["count"]
#joe = dict1.get("word"'blah2')
 
#print dict1
#print temp
#print joe