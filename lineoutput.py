with open("output.txt") as myfile:
    head = [myfile.next() for x in xrange(20)]
    #text_file = open("problem_1.txt", "w")
    spam = str(head)
    #text_file.write(spam)
    #text_file.close()
myfile.close

with open("spam.txt", "w") as newtext:
    for line in head:
        newtext.write(line) 
newtext.close