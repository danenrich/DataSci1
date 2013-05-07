import sys
import urllib2 as urllib
import json
import csv

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
    
    #print scores.items() # Print every (term, score) pair in the dictionary     
    
    tweets = []
    clean_file = tweet_file #json.dumps(tweet_file)
    for line in clean_file:
        line = line.encode('utf-8')
        print line
        #tweets.append(json.loads(line))

    tweet_json = json.load(tweet_file)
 #   results = tweet_json['results']
#  print results
    """
    for t in results:
        print repr(t['text']),"\n"
    """
    
    sent_file.close
    tweet_file.close

if __name__ == '__main__':
    main()
