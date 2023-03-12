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


# undirected weighted
def add_edge_weighted(v1, v2, cost):
    if v1 not in graph:
        print("no node")
    elif v2 not in graph:
        print("no node")
    else:
        list1 = [v1, cost]
        list2 = [v2, cost]
        graph[v1].append(list1)
        graph[v2].append(list2)


# directed unweighted
def add_edge_dir(v1, v2):
    if v1 not in graph:
        print("no node")
    elif v2 not in graph:
        print("no node")
    else:
        graph[v1].append(v2)


# directed weighted
def add_edge_dirWgt(v1, v2, cost):
    if v1 not in graph:
        print("no node")
    elif v2 not in graph:
        print("no node")
    else:
        list1 = [v1, cost]
        graph[v1].append(list1)


# directed unweighted
def delete_node_dir(v):
    if v not in graph:
        print("no node")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)


# undirected weighted
def delete_node_weight(v):
    if v not in graph:
        print("no node")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v in j[0]:
                    list1.remove(v)
                    break


# unweighted undirected
def delete_edge(v1, v2):
    if v1 not in graph:
        print("no node")
    elif v2 not in graph:
        print("no node")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
        graph[v2].remove(v1)


# unweighted directed
def delete_edge_dir(v1, v2):
    if v1 not in graph:
        print("no node")
    elif v2 not in graph:
        print("no node")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)


# unweighted undirected
def delete_edge_wight(v1, v2, cost):
    if v1 not in graph:
        print("no node")
    elif v2 not in graph:
        print("no node")
    else:
        temp1 = [v1, cost]
        temp2 = [v2, cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp2)
            graph[v2].remove(temp1)


# weighted directed
def delete_edge_wd(v1, v2, cost):
    if v1 not in graph:
        print("no node")
    elif v2 not in graph:
        print("no node")
    else:
        temp = [v2, cost]
        if temp in graph[v1]:
            graph[v1].remove(temp)


def addnode(v):
    graph = {}

    if v in graph:
        print("already")
    else:
        graph[v] = []


def addedge(v1, v2):
    if v1 not in graph:
        print("fgjn")
    elif v2 not in graph:
        print("fdk")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def costedge(v1, v2, cost):
    if v1 not in graph:
        print("fgjn")
    elif v2 not in graph:
        print("fdk")
    else:
        list1 = [v2, cost]
        graph[v1].append(list1)


def nodeadd(v):
    graph = {}

    if v in graph:
        print("already")
    else:
        graph[v] = []


def addedgee(v1, v2):
    if v1 not in graph:
        print("djkf")
    elif v2 not in graph:
        print("hafdj")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def dfdfd(node, visited, graph):
    if node not in graph:
        print("node is not present")
        return
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            dfdfd(i, visited, graph)


def bfs(node, graph):
    visited = set()
    if node not in graph:
        print("node is not present")
        return
    queue = []
    queue.append(node)
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            print(curr, end=" ")
            visited.add(curr)
            for i in graph[curr]:
                queue.append(i)


graph = {}
visited = set()
add_node(43)
add_node(32)
add_node(56)
add_node(34)
add_edge(43, 32)
addedgee(56, 32)
addedgee(34, 43)

print(graph)
dfdfd(43, visited, graph)
print()
bfs(43, graph)
