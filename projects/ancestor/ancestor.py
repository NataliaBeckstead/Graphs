from util import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for i in ancestors:
        if i[1] not in graph:
            graph[i[1]] = []
        graph[i[1]].append(i[0])
    if starting_node not in graph:
        return -1
########## 1st solution ###############
    # ancestor = starting_node
    
    # while ancestor in graph:
    #    ancestor = graph[ancestor][0]
    # return(ancestor)

########## 2nd solution ###############
    q = Queue()
    visited = set()
    path = [starting_node]
    q.enqueue(path)

    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]
        if current_node not in graph:
            return current_path[-1]
        if current_node not in visited:
            visited.add(current_node)
            path_copy = list(current_path)
            path_copy.append(graph[current_node][0])
            q.enqueue(path_copy)

# Both solutions passing test
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6)