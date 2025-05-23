def graph(arr):
    total = {}
    for i in range(len(arr)):
        node1, node2, weight = arr[i]
        if node1 not in total:
            total[node1] = {node2: weight}
        else:
            total[node1][node2] = weight
        if node2 not in total:
            total[node2] = {}
    return total

def finder(node,parents):
    if parents[node] != node:
        parents[node] = finder(parents[node])
    return parents[node]

def union(u, v,parents):
    parent_u = finder(u,parents)
    parent_v = finder(v,parents)
    if parent_u != parent_v:
        parents[parent_u] = parent_v

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((u, v, weight))
            
    edges.sort(key = get_weight)
    parents = {} 
    for node in graph:
        parents[node] = node

    minimum_spanning_tree = []
            
    for edge in edges:
        u, v, weight = edge
        if finder(u) != finder(v):
            minimum_spanning_tree.append(edge)
            union(u, v,parents)

    return minimum_spanning_tree

def get_weight(edge): 
    return edge[2] 

def maintenance_cost(edges):
    return sum(edge[2] for edge in edges)

input_object = open("input2.txt", "r")
output_object = open("output2.txt", "w")

V, E = map(int, input_object.readline().split())
Main = []
for _ in range(E):
    edge = list(map(int, input_object.readline().split()))
    Main.append(edge)

total_items = graph(Main)
minimum_spanning_tree = kruskal(total_items)

total_maintenance_cost = maintenance_cost(minimum_spanning_tree)

minimum_cost = float('inf')
for i in range(len(minimum_spanning_tree)):
    remaining_maintenance_cost = maintenance_cost(minimum_spanning_tree)
    minimum_cost = min(minimum_cost, remaining_maintenance_cost)

output_object.write(str(minimum_cost))
