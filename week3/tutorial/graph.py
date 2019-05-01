def graph_create():
    return []

def graph_add_node(g, connections=[]):
    i = len(g)
    g.append([])
    for c in connections:
        graph_connect(g, i, c);
    return i

def graph_connect(g, n1, n2):
    g[n1].append(n2)
    g[n2].append(n1)

def graph_disconnect(g, n1, n2):
    g[n1].remove(n2)
    g[n2].remove(n1)

def graph_degree(g, n):
    return len(g[n])

def graph_connected(g, n1, n2):
    return n2 in g[n1] and n1 in g[n2]

g = graph_create()
node0 = graph_add_node(g)
node1 = graph_add_node(g, [node0])
node2 = graph_add_node(g, [node0, node1])
node3 = graph_add_node(g, [node0])

print("node1 connected to node2? " + str(graph_connected(g, node1, node2)))

for i in range(len(g)):
    print("node " + str(i) + " has " + str(graph_degree(g, i)) + " connections (" + str(g[i]) + ")")
