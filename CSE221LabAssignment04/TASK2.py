input_file = open('input2.txt','r')
first = input_file.readline().split(" ")
item = int(first[0])
size = int(first[1])
graph= {x:[] for x in range(1,item+1)}
print(size)
output = open('output2.txt','w')

for i in range(size):
    line = input_file.readline().split(" ")
    key = int(line[0])
    value = int(line[1])
    
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]    

def bfs( graph, node):
  visited = []
  queue = []
  queue.append(node)
  
  while queue:
    node = queue.pop(0)
    if node not in visited:
      visited.append(node)
      output.write(str(node)+" ")

    for connected in graph[node]:
      if connected not in visited:
        queue.append(connected)
  

source = 1
bfs(graph,source)
