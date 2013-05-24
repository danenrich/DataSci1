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
    #tupper = sort() #If you sort the tuple... 
    tupper = tuple(record)
    #tuppy = tuple(reversed(record))
    mr.emit_intermediate(tupper,record)
    mr.emit_intermediate(tuple(reversed(record)),tupper)
    #mr.emit_intermediate(tuppy,tupper)
    #mr.emit_intermediate(friend,record)
    
    #mr.emit_intermediate(key,mr.emit_intermediate(key, friend))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    goset = {}
    #goset = map(tuple,list_of_values)
    #goset = [list(x) for x in set(tuple(x) for x in list_of_values)]
    #[i for i in set(a) if a.count(i)<2]
    mr.emit((key,list_of_values))
                    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
