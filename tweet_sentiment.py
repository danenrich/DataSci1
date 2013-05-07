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
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        """ May need to do upper or lowercase comparison
        newscores = {} # initialize an empty dictionary
        newscores = scores((k.upper(), v) for k,v in scores.iteritems())
        """
    #print scores.items() # Print every (term, score) pair in the dictionary         
    
    results = json.load(tweet_file) #['results']  #this is a dictionary
    tweets = results['results'] #this is a list 
    for onetweet in tweets:
        textdata = onetweet['text']
        totalscore = 0
        for word in textdata.split():
            cleanword = word.encode('utf-8') #.upper() **not doing case comparison
            # strung = repr(cleanword) don't want to send as string  
            #Note: may need to remove punctuation
            #print cleanword
            wordscore = scores.get(cleanword)
            if wordscore == None:
                wordscore = 0
            totalscore = totalscore + wordscore
        sys.stdout.write(str(totalscore)+"\n")

    sent_file.close
    tweet_file.close

if __name__ == '__main__':
    main()

