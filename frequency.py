import sys
import json
import string

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main(): 
    tweet_file = open(sys.argv[1])
         
    tweets = []
    with tweet_file as f:  #when this is open('output.txt') it works 5/8/13
        for x in f:
            tweets.append(json.loads(x)) 

    myterms = [] #This is the final list of terms
    totalwords = 0
    #for onetweet in tweets: #REMOVE THIS XRANGE CONSTRAINT
    for onetweet in tweets:
        if onetweet.has_key('text') == 1:
            textdata = onetweet['text'] # **sentiment file is all lower case
            for word in textdata.split():
                totalwords = totalwords + 1
                cleanword = word.encode("utf-8")
                cleanerword = cleanword.rstrip('?:!.,;') #Removing punctuation
                cleanerword = cleanerword.replace("\n"," ") #Removing line breaks
                cleanerword = filter(lambda x: x in string.printable, cleanerword)
                #Check to see if it's already in my list
                checkvar = 0
                for term in myterms: #The word is already in my list, so update its count
                    if len(word) > 0:
                        if term["word"] == cleanerword:
                            current_count = term["count"]
                            term["count"] = current_count + 1 #Increment the number of instances                        
                            checkvar = 1
                    #The word isn't already in my list, add it
                if checkvar == 0 and len(word) > 0: 
                    myterms =  myterms + [{
                    "word":word,
                    "count":1,
                    }]

    #Print master list
    for term in myterms:
        if len(term["word"]) != 0:
            wordstring = term["word"]
            wordstring = wordstring.encode("utf-8")
            freq = str(float(float(term["count"])/totalwords))
            sys.stdout.write(str(wordstring) + " " + freq + "\n")

    tweet_file.close

if __name__ == '__main__':
    main()

