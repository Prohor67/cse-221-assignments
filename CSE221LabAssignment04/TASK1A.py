input_file = open('input1A.txt','r')
vertex = int(input_file.readline()[0])
nodes = input_file.readlines()
location = [x.rstrip("\n").split(" ") for x in nodes]

output = open('output1A.txt','w')

def data_format(nodes):
    for i in nodes:
        for j in range(len(i)):
            i[j] = int(i[j])
    return nodes

def graph_presenter(matrix): 
  for i in matrix:
    str_out = ""
    for j in i:
      str_out+=str(j)+" "
    str_out+="\n"  
    output.write(str_out)


def graph_maker(location,vertex):
  matrix = []
  for i in range(vertex+1):
    matrix.append([0]*(vertex+1))
  for i in location:
    row = i[0]
    column = i[1]
    weight = i[2]
    matrix[row][column] = weight
  return graph_presenter(matrix)

graph_maker(data_format(location), vertex)
print(location)