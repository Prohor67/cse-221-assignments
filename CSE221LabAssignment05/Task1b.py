with open("input1b_1.txt","r") as file:
    with open("output1b_1.txt","w") as file2:
        n = next(file)
        n = n.split(" ")
        vertices = int(n[0])

        graph = []

        for i in range(int(vertices)+1):
            graph.append([])

        for j in file:
            j = j.strip()
            count = 0
            list_position = ''
            for k in j:
                if k==" ":
                    break
                list_position+=k
                count+=1
            graph[int(list_position)].append(int(j[count+1:]))



        indegree = [0]*(vertices+1)
        queue = []
        topological_sort = []

        for i in graph:
            for j in i:
                indegree[j]+=1

        for i in range(1,len(indegree)):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            itm = queue.pop(0)
            topological_sort.append(itm)
            for i in graph[itm]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)

        topological_sort_output=""
        if len(topological_sort)==(len(graph)-1):
            for i in topological_sort:
                topological_sort_output+=str(i)+" "
            file2.write(topological_sort_output)
        else:
            file2.write("IMPOSSIBLE")