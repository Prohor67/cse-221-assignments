input_file = open('input6.txt','r')
first = input_file.readline().split(" ")
rows = int(first[0])
cols = int(first[1])
graph = []
for i in range(rows):
    graph.append(input_file.readline().rstrip("\n"))


def dfs(graph, rows, cols, visited):
    if rows < 0 or rows >= len(graph) or cols < 0 or cols >= len(graph[0]) or graph[rows][cols] == '#' or visited[rows][cols]:
        return 0
    visited[rows][cols] = True
    diamonds = 0
    if graph[rows][cols] == 'D':
      diamonds = 1
    diamonds += dfs(graph, rows + 1, cols, visited)
    diamonds += dfs(graph, rows - 1, cols, visited)
    diamonds += dfs(graph, rows, cols + 1, visited)
    diamonds += dfs(graph, rows, cols - 1, visited)
    return diamonds

def max_diamonds(graph,rows,cols):
    max_diamonds = 0
    visited = []
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] != '#':
                for k in range(rows):
                  visited.append([False]*cols)
                
                max_diamonds = max(max_diamonds, dfs(graph, i, j, visited))
    return max_diamonds


output = open('output6.txt','w')
output.write(str(max_diamonds(graph,rows,cols)))