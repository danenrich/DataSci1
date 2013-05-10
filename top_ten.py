import sys
import json
import collections

def main():
    tweet_file = open(sys.argv[1])
      
    tweets = []
    with tweet_file as f:  #when this is open('output.txt') it works 5/8/13
        for x in f:
            tweets.append(json.loads(x)) 

    textdata = [] #This is the final list of new terms
    for onetweet in tweets: 
    #for onetweet in tweets[:2000]: #REMOVE THIS XRANGE CONSTRAINT
        if onetweet.has_key('text') == 1:
            textual = onetweet['text']
            cleantext = textual.encode('utf-8')
            cleanertext = cleantext.rstrip('?:!.,;') #Removing punctuation
            cleanertext = cleanertext.replace("\n"," ")
            textdata = textdata + [cleanertext] #list of text strings

    hashlist = []
    hashtemp = []
    for hashy in textdata:
        hashtemp = list(set(part for part in hashy.split() if part.startswith('#')))
        hashlist = hashlist + hashtemp
    #print hashlist
    freqtable = collections.Counter(hashlist)
    sorttable = sorted(freqtable.items(), key=lambda item: item[1], reverse=True)
    #print sorttable
    smalltable = sorttable[:10]
    #print smalltable

    #Print master list
    for item in smalltable:
        hashstring = item[0]
        hashstring = hashstring.encode("utf-8")
        freq = str(float(item[1]))
        sys.stdout.write(str(hashstring) + " " + freq + "\n")
    
    tweet_file.close

if __name__ == '__main__':
    main()

