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
    """
    for n in sent_file:
        results = json.loads(n)
    """
    """
    with sent_file as file_object:
    # skip the first two lines
        results = list(csv.DictReader(file_object, dialect='excel-tab'))
    """
    with sent_file as infile:
        reader = csv.reader(infile)
        
    text_file = open("sent_out.txt", "w")
    with text_file as outfile:
        #writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
        for n in mydict:
            text_file.write("%s\n" % n)
    text_file.close()
     
"""    
    text_file = open("sent_out.txt", "w")
    for t in results:
        text_file.write("%s\n" % t)
        #line = str(repr(t['text']))
        #text_file.write("%s\n" % line)
"""
    

if __name__ == '__main__':
    main()
