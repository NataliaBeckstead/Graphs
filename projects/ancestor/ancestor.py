
def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for i in ancestors:
        if i[1] not in graph:
            graph[i[1]] = []
        graph[i[1]].append(i[0])
    print(graph)
    if starting_node not in graph:
        return -1

    ancestor = starting_node
    
    while ancestor in graph:
       ancestor = graph[ancestor][0]
    print(ancestor)
    return(ancestor)

