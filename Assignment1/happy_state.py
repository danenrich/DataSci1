import sys
import json

def main():
    sent_file = open(sys.argv[1])   
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary         
 
    tweets = []
    with tweet_file as f:  #when this is open('output.txt') it works 5/8/13
        for x in f:
            tweets.append(json.loads(x))
    
    highscore = -10000000
    
    for onetweet in tweets:
        if onetweet.has_key('text') == 1 and onetweet.has_key('place') == 1:
            placetweet = onetweet["place"]
            if placetweet != None:
                if placetweet.has_key('country') and placetweet.has_key('full_name'):
                    countrycode = placetweet['country_code']
                    if countrycode=='US':
                        fullname = placetweet['full_name']
                        if len(fullname) > 1:
                            textdata = onetweet['text'] # **sentiment file is all lower case
                            totalscore = 0
                            for word in textdata.split():
                                cleanword = word.encode('utf-8')
                                cleanerword = cleanword.rstrip('?:!.,;') #Removing punctuation
                                wordscore = scores.get(cleanerword)
                                if wordscore == None:
                                    wordscore = 0
                                totalscore = totalscore + wordscore
                                if totalscore > highscore:
                                    highscore = totalscore
                                    happystate = fullname[-2:]
    
    sys.stdout.write(str(happystate))

    sent_file.close
    tweet_file.close

if __name__ == '__main__':
    main()

