
with open("output.txt") as myfile:
    head = [myfile.next() for x in xrange(20)]
    text_file = open("problem_1.txt", "w")
    text_file.write(str(head))
    text_file.close()
myfile.close


print head
