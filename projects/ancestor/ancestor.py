import sys
sys.path.append('../graph')
from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    pass
    # Build the Graph
    graph = Graph()
    # Add the number of vertices (range 1 to 11 because that's how many exist in the test)
    for i in range(1, 12):
        graph.add_vertex(i)
    # Create linkages from the ancestors list
    for link in ancestors:
        graph.add_edge(link[0], link[1])
    
    print('----------- GRAPH -----------')
    print(graph.vertices)
    print('----------- GRAPH -----------')

    


    # Conduct a breadth-first-search


    # If the input individual has no parents, return
        # Return -1
    # If there is more than one ancestor tied to the earliest
        # Return the one with the lowest numeric ID

    # Return earliest ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
