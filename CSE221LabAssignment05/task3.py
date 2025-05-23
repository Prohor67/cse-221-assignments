with open("input3_1.txt","r") as file:
    with open("output3_1.txt","w") as file2:

    
        n = next(file)
        n = n.split(" ")
        vertices = int(n[0])

        reverse_graph = [[],[],[],[],[],[],[],[]]
        graph= []
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


        def connected_graph(graph,source):

        # Append in stack
            visited = [0]*(vertices+1)
            stack = []
            def Dfs(graph,source):
                visited[source]=1
                for i in range(len(graph[source])):
                    if visited[graph[source][i]] == 0:
                        Dfs(graph,graph[source][i])
                stack.append(source)

            Dfs(graph,1)

        # reverse_graph
            for k in range(len(graph)):
                for l in graph[k]:
                    reverse_graph[l].append(k)


        # Connected Component part
            component_flag = [0]*(vertices+1)
            while stack:
                con_str = ''
                pop_itm = stack.pop()
                def component(itm):
                    nonlocal con_str
                    if component_flag[itm]!=1:
                        con_str+=str(itm)+" "
                    component_flag[itm]=1
                    for i in range(len(reverse_graph[itm])):
                        if component_flag[reverse_graph[itm][i]] == 0:
                            con_str+=str(reverse_graph[itm][i])+" "
                            component_flag[reverse_graph[itm][i]]=1
                            component(reverse_graph[itm][i])
                    if con_str!="":
                        file2.write(f"{con_str}\n")
                        con_str=""
                component(pop_itm)
        


        connected_graph(graph,1)