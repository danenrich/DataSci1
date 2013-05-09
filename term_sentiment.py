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
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary         
 
    tweets = []
    with tweet_file as f:  #when this is open('output.txt') it works 5/8/13
        for x in f:
            tweets.append(json.loads(x))

    #tweets = data #['results'] #this is a list 

    for onetweet in tweets:
        totalscore = 0
        if onetweet.has_key('text') == 1:
            textdata = onetweet['text'].lower() # **sentiment file is all lower case
            for word in textdata.split():
                cleanword = word.encode('utf-8')
                #print cleanword 
                cleanerword = cleanword.rstrip('?:!.,;') #Removing punctuation
                #print cleanerword
                wordscore = scores.get(cleanerword)
                if wordscore == None:
                    wordscore = 0
                totalscore = totalscore + wordscore
        sys.stdout.write(str(totalscore)+"\n")

        #look here to see how to iterate through key/values http://dan.lecocq.us/wordpress/2011/09/14/python-and-arbitrary-function-arguments-kwargs/

    sent_file.close
    tweet_file.close

if __name__ == '__main__':
    main()

