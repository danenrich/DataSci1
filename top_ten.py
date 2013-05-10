import sys
import json
import collections

def main():
    tweet_file = open(sys.argv[1])
      
    tweets = []
    with tweet_file as f:  #when this is open('output.txt') it works 5/8/13
        for x in f:
            tweets.append(json.loads(x)) 
    entities = [] #This is the final list of new terms
    hashtemp = []
    hashlist = []
    #for onetweet in tweets: 
    for onetweet in tweets: #REMOVE THIS XRANGE CONSTRAINT
        if onetweet.has_key('entities') == 1:
            entities = onetweet['entities']
            if entities.has_key('hashtags')==1:
                if entities["hashtags"] != None:
                    hashmash = entities["hashtags"]
                    for hashtemp in hashmash:
                        #print hashtemp["text"]
                        hashlist = hashlist + [hashtemp["text"]]

    #print hashlist
    freqtable = collections.Counter(hashlist)
    sorttable = sorted(freqtable.items(), key=lambda item: item[1], reverse=True)
    #print sorttable
    smalltable = sorttable[:10]
    #print smalltable

    #Print master list
    for item in smalltable:
        hashstring = item[0]
        hashstring = hashstring #.encode("utf-8")
        freq = str(float(item[1]))
        sys.stdout.write(str(hashstring) + " " + freq + "\n")
    
    tweet_file.close

if __name__ == '__main__':
    main()

