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

    myterms = [] #This is the final list of new terms
    #for onetweet in tweets: #REMOVE THIS XRANGE CONSTRAINT
    for onetweet in tweets[:5]:
        totalscore = 0
        if onetweet.has_key('text') == 1:
            textdata = onetweet['text'].lower() # **sentiment file is all lower case
            update_list = [] #List of words in the tweet that exist in my dictionary already, so their values need updating. Initialize it for each tweet. 
            new_list = [] #List of words that do not exist so need to be created.
            myterms_temp = [] #List of dictionary entries for each new word
            for word in textdata.split():
                cleanword = word.encode('utf-8')
                cleanerword = cleanword.rstrip('?:!.,;') #Removing punctuation
                #print cleanerword
                wordscore = scores.get(cleanerword)
                if wordscore == None: #The word isn't in Nielsen's sentiment dictionary
                    #Check to see if it's already in my list
                    checkvar = 0
                    for word in myterms:
                        if word["word"] == cleanerword:
                            checkvar = 1
                    if checkvar == 0: #The word isn't already in my list
                        #Add word to my temp dictionary
                        new_list = new_list + [cleanerword] #Add new word to the list of terms that will be added to my list
                    else: #The word is already in my dictionary
                        #Add the word to the list of words that need their scores updated
                        update_list = update_list + [cleanerword]
                else: #The word is in Neilsen's library
                    #The word exists in the library, so we should assign it a score and update the total
                    totalscore = totalscore + wordscore
            #Once we're done with all the words in the tweet, go back and add/edit words that weren't in Nielsen's dictionary
            update_list = list(set(update_list)) #dedupe the update_list
            for word in update_list: #any word that exists, average in the totalscore with the word's score
                for term in myterms:
                    if term["word"] == word:
                        current_score = term["score"]
                        current_count = term["count"]
                        term["score"] = ((current_score*current_count)+totalscore)/(current_count+1) #Average in the new score
                        term["count"] = current_count + 1 #Increment the number of instances
            new_list = list(set(new_list)) #dedupe the update_list
            for word in new_list: #add new words, assign them totalscore
                myterms_temp =  myterms_temp + [{
                                "word":word,
                                "score":totalscore,
                                "count":1,
                        }]
            myterms = myterms + myterms_temp #Append master list with list of new words in this tweet
    #Print master list
    for term in myterms:
        sys.stdout.write(str(term["word"])+ " Score: " + str(term["score"])+" Count: " + str(term["count"])+"\n")

    sent_file.close
    tweet_file.close

if __name__ == '__main__':
    main()

