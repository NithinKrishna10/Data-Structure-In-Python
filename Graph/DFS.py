def add_node(v):
    if v in graph:
        print("not all ready in the graph")
    else:
        graph[v] = []

# undirectde unweighted
def add_edge(v1, v2):
    if v1 not in graph:
        print("no node")
    elif v2 not in graph:
        print("no node")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


# DFS Recursive
def DFS(node,visited,graph):
    if node not in graph:
        print("node is not present")
        return
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)





def Dfs(node,visited,graph):
    if node not in graph:
        print("node is not present")
        return
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for i in graph:
            Dfs(i,visited,graph)


# DFS Iterative

def DFSiterative(node,graph):
    visited = set()
    if node not in graph:
        print("node is not present")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current,end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

def BFSiterative(node, graph):
    visited = set()
    if node not in graph:
        print("node is not present")
        return
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)






visited = set()
graph = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_edge("A", "D")
add_edge("A", "C")
add_edge("A", "B")
add_edge("B", "E")
add_edge("E", "F")

# add_edge(56, 43)
# add_edge(34, 32)
# add_edge(56, 34)
# DFS(43,visited,graph)
Dfs(32,visited,graph)
print()
# BFSiterative(43,graph)
print()
print(graph)
