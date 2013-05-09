import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])   
    tweet_file = open(sys.argv[2])
    #sflines = lines(sent_file)
    #twlines = lines(tweet_file)
    
    """
    Theory: If a word is in the reference dictionary ("ref"), use it to calc the tweet's totalscore. 
    Once you've finished parsing the tweet, if a word is not in ref assign each missing word the tweet total score and stick that result in work.
    The working dictionary will have the word, the score, and the number of times we've found that word. {"word":"blah","score":"1.23","instances":"4"}
    The next time we find the word we can simply
    multiply the word's score times the number of times we've found the word, add to it the new score, and divide by instances + 1. We then increment
    the instances count.
    Once you're done parsing all of the tweets, average all the words across the dictionary.
    """  

    #print scores.items() # Print every (term, score) pair in the dictionary         
 
    tweets = []
    with tweet_file as f:  #when this is open('output.txt') it works 5/8/13
        for x in f:
            tweets.append(json.loads(x)) 

    myterms = [] #This is the final list of terms
    totalwords = 0
    #for onetweet in tweets: #REMOVE THIS XRANGE CONSTRAINT
    for onetweet in tweets[:20]:
        if onetweet.has_key('text') == 1:
            textdata = onetweet['text'].lower() # **sentiment file is all lower case
            for word in textdata.split():
                totalwords = totalwords + 1
                cleanword = word.encode('utf-8')
                cleanerword = cleanword.rstrip('?:!.,;') #Removing punctuation
                #Check to see if it's already in my list
                checkvar = 0
                for term in myterms: #The word is already in my list, so update its count
                    if term["word"] == cleanerword:
                        current_count = term["count"]
                        term["count"] = current_count + 1 #Increment the number of instances                        
                        checkvar = 1
                #The word isn't already in my list, add it
                if checkvar == 0: 
                    myterms =  myterms + [{
                    "word":word,
                    "count":1,
                    }]

    #Print master list
    for term in myterms:
        sys.stdout.write(str(term["word"])+ " " + str(float(term["count"]/totalwords))+"\n")

    sent_file.close
    tweet_file.close

if __name__ == '__main__':
    main()

