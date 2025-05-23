input_file = open('input4.txt','r')
first = input_file.readline().split(" ")
item = int(first[0])
size = int(first[1])
graph= {x:[] for x in range(1,item+1)}

output = open('output4.txt','w')

for i in range(size):
    line = input_file.readline().split(" ")
    key = int(line[0])
    value = int(line[1])
    
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]  

def dfs_cycle_check(graph,node):
    visited = {}
    in_stack = []
    visited[node] = True
    in_stack.append(node)

    for connected in graph[node]:
      if connected not in visited:
        if dfs_cycle_check(graph,connected):
          return True
      elif connected in in_stack:
        return True

    in_stack.remove(node)
    visited[node] = False
    return False

source = 1
final = dfs_cycle_check(graph,source)
if final == True:
  output.write("YES")
else:
   output.write("NO")


