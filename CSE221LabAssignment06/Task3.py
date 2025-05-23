with open("input3_2.txt","r") as file:
  with open("output3_2.txt","w") as file2:
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
   


    def max_dis(A,B):
        if A>B:
            return A
        else:
            return B

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
                max_distance = max_dis(distance[itm],i[1])
                if max_distance<distance[i[0]]:
                    distance[i[0]]=max_distance

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
    
    distance_arr = dijkstra(graph,1)
    
    if distance_arr[nodes]!= float("inf"):
        file2.write(f"{distance_arr[nodes]}")
    else:
        file2.write("Impossible")



    

    
    