import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    
    #a is a 5x5 matrix, starting at 0 and ending at 4
    #b is a 5x5 matrix, starting at 0 and ending at 4
    maxkey = 5 
    matrixid = record[0]
    rownum = record[1]
    colnum = record[2]
    val = record[3]
    
    vallist = []
    
    ["a", 2, 3, 60]
    
    if matrixid == "a":
    #a:every val in a gets multiplied in each col of b. row in a is its row in c. for a, we need to know its original column and its value. need to gen keys for each col of c.
        for i in range(0,maxkey):
            key = (rownum,i)
            vallist = [matrixid,colnum,val]
            mr.emit_intermediate(key, vallist)

    if matrixid == "b":
    #a:every val in a gets multiplied in each col of b. row in a is its row in c. for a, we need to know its original column and its value. need to gen keys for each col of c.
        for i in range(0,maxkey):
            key = (i,colnum)
            vallist = [matrixid,rownum,val]
            mr.emit_intermediate(key, vallist)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    #numfriends =  len(list_of_values)
    mr.emit((key,list_of_values))
                    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
