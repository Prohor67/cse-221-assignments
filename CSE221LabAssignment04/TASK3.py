input_file = open('input3.txt','r')
first = input_file.readline().split(" ")
item = int(first[0])
size = int(first[1])
graph= {x:[] for x in range(1,item+1)}

output = open('output3.txt','w')

for i in range(size):
    line = input_file.readline().split(" ")
    key = int(line[0])
    value = int(line[1])
    
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]  




def dfs(graph,source,visited = None):
  if visited == None:
    visited = []

  visited.append(source)
  output.write(str(source)+" ")

  for connected in graph[source]:
    if connected not in visited:
      dfs(graph, connected, visited)

source = 1
dfs(graph,source)