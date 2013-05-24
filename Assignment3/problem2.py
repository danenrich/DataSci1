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
    vals = []
    key = record[1]
    table = record[0]
    for i in range(2,len(record)):
        vals = vals + [record[i]]
    vals = [table] +[vals]
    mr.emit_intermediate(key, vals)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    output = []
    ordertext = ""
    for v in list_of_values:
        if v[0] == 'order':
            ordertext = [v[0]] + [str(key)] + v[1]
    #print ordertext
    for x in list_of_values:
        if x[0] == 'line_item': 
            output = ordertext + [x[0]] + [str(key)] + x[1]
            mr.emit(output)
                    
          
    #mr.emit((key, cleanlist))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
