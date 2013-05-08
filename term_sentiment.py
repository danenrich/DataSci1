import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #parse the sentiment scores file
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
  
    """
    Theory: If a word is in the reference dictionary ("ref"), use it to calc the tweet's totalscore. 
    Once you've finished parsing the tweet, if a word is not in ref assign each missing word the tweet total score and stick that result in work.
    The working dictionary will have the word, the score, and the number of times we've found that word. {"word":"blah","score":"1.23","instances":"4"}
    The next time we find the word we can simply
    multiply the word's score times the number of times we've found the word, add to it the new score, and divide by instances + 1. We then increment
    the instances count.
    Once you're done parsing all of the tweets, average all the words across the dictionary.
    """  
    
    #create the sentiment dictionary
    output = []
    for something in somethingelse:
        output.append(dict([(x, x**3) for x in xrange(1, 3)]))
    blah = json.dumps(output)
    
    #load the tweet file
    results = json.load(tweet_file) #['results']  #this is a dictionary
    tweets = results['results'] #this is a list 
    for onetweet in tweets:
        textdata = onetweet['text'].lower() #.upper() **sentiment file is all lower case
        totalscore = 0
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

    
    sent_file.close
    tweet_file.close




if __name__ == '__main__':
    main()
