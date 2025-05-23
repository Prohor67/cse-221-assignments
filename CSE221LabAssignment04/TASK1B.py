input_file = open('input1B.txt','r')
first_line = input_file.readline()
vertex = int(first_line[0])
item = int(first_line[2])
nodes = input_file.readlines()
location = [x.rstrip("\n").split(" ") for x in nodes]

output = open('output1B.txt','w')

def data_format(nodes):
    for i in nodes:
        for j in range(len(i)):
            i[j] = int(i[j])
    return nodes



def graph(size,arr,item):
  total = []
  for i in range(size+1):
    total.append([])
  for i in range(size+1):
    for j in range(item):
      if i == arr[j][0]:
        total[i].append(tuple([arr[j][1],arr[j][2]]))
 
  str_out = ""
  for i in range(size+1):
    if len(total[i]) == 0:
      str_out+= f"{i} :\n"
    else:
      temp = ""
      for j in range(len(total[i])):
        temp+= str(total[i][j])+" "
      str_out+= f"{i} : {temp}\n"

  return str_out

output.write(graph(vertex,data_format(location),item))
