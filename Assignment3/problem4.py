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
    mr.emit_intermediate(tuple(reversed(record)),tupper)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    newlist = []
    newlist = [s for s in list_of_values if len(s) == 2] 
    mr.emit(newlist)
                    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
