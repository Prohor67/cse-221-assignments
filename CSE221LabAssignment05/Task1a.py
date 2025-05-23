with open("input1a_3.txt","r") as file:
   with open("output1a_3.txt","w") as file2:
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

        root_node_checker = [0]*(vertices+1)
        root_node = []
        for i in range(len(graph)):
            for j in graph[i]:
                if root_node_checker[i]!=1:
                    root_node_checker[j]=1

        for k in range(1,len(root_node_checker)):
            if root_node_checker[k]==0:
                root_node.append(k)

        topological_order = [0]*(vertices)
        top_len = len(topological_order)-1
        visited = [0]*(vertices+1)
        start = [0]*(vertices+1)
        end = [0]*(vertices+1)
        count = 1
        flag = False
        def dfs_top(graph,source):
            global count,top_len,start,end,count,visited,topological_order,flag
            if visited[source]!=1:
                visited[source]=1
                start[source]=count
                count+=1
                for i in range(len(graph[source])):
                    if end[graph[source][i]]==0 and start[graph[source][i]]!=0:
                        file2.write("IMPOSSIBLE")
                        flag = True
                        return
                    elif visited[graph[source][i]] == 0:
                        dfs_top(graph,graph[source][i])
                    
                end[source]=count
                topological_order[top_len]= source
                top_len-=1

        while root_node:
            itm = root_node.pop(0)
            dfs_top(graph,itm)

        topological_order_output=""
        if flag==False:
            for i in topological_order:
                topological_order_output+=str(i)+" "
            file2.write(topological_order_output)