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

    #print scores.items() # Print every (term, score) pair in the dictionary         
 
    data = []
    with open('output.txt') as f:
        for x in f:
            data.append(json.loads(x))

    tweets = data #['results'] #this is a list 

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

