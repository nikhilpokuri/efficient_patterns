def add_node(node):
    nodes.add(node)
    for row in graph:
        row.append(0)
    col = []
    for _ in range(len(nodes)):
        col.append(0)
    graph.append(col)

def add_edge(node1, node2):
    if not node1 in nodes:
        print(f"{node1} not in graph")
        return
    if not node2 in nodes:
        print(f"{node2} not in graph")
        return
    graph[node1][node2] = 1

num_of_nodes = 6
nodes = set()
graph = []
adj_nodes = {}

#adding nodes from 0-5
for i in range(num_of_nodes):
    adj_nodes[i] = set() #to store it's neighbours later
    add_node(i)

#adding the directed edges
add_edge(5, 0)
add_edge(4, 0)
add_edge(5, 2)
add_edge(2, 3)
add_edge(3, 1)
add_edge(4, 1)

#group the neighbours to respective nodes 
for r in range(num_of_nodes):
    for c in range(num_of_nodes):
        if graph[r][c] == 1:
            adj_nodes[r].add(c)

#Topological sort
""" 
similar to dfs but reversing the stack
"""
def topological_sort(node, visited=set()):
    visited.add(node)
    for n in adj_nodes[node]:
        if n not in visited:
            topological_sort(n, visited)
    if node not in res:
        res.insert(0,node)

res = []
for i in nodes:
    topological_sort(i)
print(res)