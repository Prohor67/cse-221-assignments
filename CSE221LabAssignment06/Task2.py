with open("input2_3.txt","r") as file:
  with open("output2_3.txt","w") as file2:
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
    source = next(file).split(" ")
    alice_source = int(source[0])
    bob_source = int(source[1])
    


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

    alice_distance = dijkstra(graph,alice_source)
    bob_distance = dijkstra(graph,bob_source)
    

    def max_dis(A,B):
        if A>B:
            return A
        else:
            return B

    dis_flag = False
    min_num = float('inf')
    for i in range(1,len(graph)):
        max_distance = max_dis(alice_distance[i],bob_distance[i])
        if max_distance<min_num:
            dis_flag = True
            Time = max_distance
            Node = i
            min_num = Time

    if dis_flag==True:
        file2.write(f"Time: {Time}\n")
        file2.write(f"Node: {Node}")
    else:
        file2.write("Impossible")
    