def addnode(v):
    global node_count
    if v in nodes:
        print("the node alredy in graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

# undirected unweighted
def add_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not in the graph")
    elif v2 not in nodes:
        print(v2, "is not in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1


# weighted undirected
def add_edge_weight(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not in the graph")
    elif v2 not in nodes:
        print(v2, "is not in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost


#  directed weighted
def add_edge_dir(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not in the graph")
    elif v2 not in nodes:
        print(v2, "is not in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        # graph[index2][index1] =


# Delete node function
def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"not in node")
    else:
        index1 = nodes.index(v)
        node_count = node_count - 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)


# Delete Edge undirected
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1, "is not in the graph")
    elif v2 not in nodes:
        print(v2, "is not in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0


# Delete Edge directed
def delete_edge_dir(v1,v2):
    if v1 not in nodes:
        print(v1, "is not in the graph")
    elif v2 not in nodes:
        print(v2, "is not in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0

def printgraph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<5"), end="")
        print()


nodes = []
graph = []
node_count = 0
print("before")
print(nodes)
print(graph)
addnode("A")
addnode("B")
addnode("C")
add_edge("A", "B")
add_edge("C", "B")
add_edge_weight("C", "A", 8)
print("after")
delete_node("C")
print(nodes)
print(graph)

printgraph()
