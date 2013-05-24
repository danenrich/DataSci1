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
    dict1 = []
    key = record[0]
    friend = record[1]
    #tupper = tuple(reversed(record))
    mr.emit_intermediate(key,record)
    mr.emit_intermediate(friend,record)
    
    #mr.emit_intermediate(key,mr.emit_intermediate(key, friend))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print key, list_of_values
    #blah = 1
    mr.emit((key,list_of_values))
                    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
