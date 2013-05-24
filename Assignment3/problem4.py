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
 
    tupper = tuple(record)
    mr.emit_intermediate(tupper,record)
    mr.emit_intermediate(tuple(reversed(record)),list(tupper))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    newlist = []
    #newlist = [s for s in list_of_values if len(s) == 2] 
    bob = []
    out = []
    #print len(list_of_values)
    bob =[str(key)] + list_of_values
    #print len(bob)
    if len(bob) < 3:
        #print len(bob)
        newlist = out + bob[1] 
    """
    for i in list_of_values:
        #print i, len(i)
        if len(i) == 1:  
            print i
            newlist = newlist + i
    """
    if len(newlist) > 0:
        mr.emit(newlist)
                    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
