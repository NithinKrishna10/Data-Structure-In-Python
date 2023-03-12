import collections


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


# BFS Iterative

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


def BFS(node, graph):
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
                # print(i)
                queue.append(i)

def bfss(node,graph):

    visited= set()
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


def dfs(node,graph):
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






visited = set()
graph = {}

add_node(43)
add_node(32)
add_node(56)
add_node(34)
add_node(45)
add_edge(45,56)
add_edge(43, 32)
add_edge(56, 32)
add_edge(34, 32)
add_edge(56, 34)
# DFS(43,visited,graph)
# DFSiterative(43, graph)
bfss(43, graph)
print()
# print(graph)
dfs(43,graph)
