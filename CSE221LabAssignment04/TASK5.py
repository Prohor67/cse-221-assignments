input_file = open('input5.txt','r')
first = input_file.readline().split(" ")
item = int(first[0])
size = int(first[1])
destination = int(first[2])
graph= {x:[] for x in range(1,item+1)}

output = open('output5.txt','w')

for i in range(size):
    line = input_file.readline().split(" ")
    key = int(line[0])
    value = int(line[1])
    
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]  



def bfs_shortest_path(graph, source, destination):
    queue = []
    queue.append((source, [source]))
    visited = [False] * (len(graph) + 1)
    visited[source] = True

    while queue:
        node, path = queue.pop(0)
        if node == destination:
            return len(path)-1, path

        for neighbor in graph[node]:
            if  visited[neighbor] == False:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))

source = 1
time, shortest_path = bfs_shortest_path(graph, source, destination)

str_out = ""
for i in shortest_path:
  str_out +=str(i)+" "

str_out = "Shortest Path:"+" "+str_out
str_out = "Time: "+str(time)+"\n"+str_out
output.write(str_out)