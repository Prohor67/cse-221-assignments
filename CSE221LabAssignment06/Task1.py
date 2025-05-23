with open("input1_1.txt","r") as file:
  with open("output1_1.txt","w") as file2:
    n = next(file)
    n = n.split(" ")
    nodes = int(n[0])
    edges = int(n[1])
    graph= []

    for i in range(int(nodes)+1):
        graph.append([])

    for i in range(edges):
       n = next(file)
       n = n.split(" ")
       graph[int(n[0])].append((int(n[1]),int(n[2].strip())))
    source = int(next(file))


    def dijkstra(graph,source):
        distance = [float('inf')]*(nodes+1)
        visited = [0]*(nodes+1)
        queue = []
        distance[source] = 0
        queue.append(source)
        flag = False
        while queue:
            itm = queue.pop(0)
            if visited[itm]==1:
                continue
            for i in graph[itm]:
                if distance[itm]+i[1]<distance[i[0]]:
                    distance[i[0]]=distance[itm]+i[1]

                    for j in range(len(queue)):
                        if distance[i[0]]<distance[queue[j]]:
                            queue.insert(j,i[0])
                            flag = True
                            break
                    if flag==False:
                        queue.append(i[0])
                    flag = False
            visited[itm]=1
        
        return distance

    write_obj = dijkstra(graph,source)
    inner_txt = ''
    for i in range(1,len(write_obj)):
        if write_obj[i]!=float('inf'):
            inner_txt+=str(write_obj[i])+" "
        else:
            inner_txt+="-1"+" "
    file2.write(inner_txt)
    