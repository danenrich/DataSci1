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
    
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    print scores.items() # Print every (term, score) pair in the dictionary     
        
        

if __name__ == '__main__':
    main()
