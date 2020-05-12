from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
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

    # Conduct a breadth-first-search
    q = Queue()
    q.enqueue(starting_node)

    # print('Queued Node', q.queue)

    # Define needed arrays
    popped_children = 0
    temp_array = []
    children = []

    # Looping through our graph
    for node in graph.vertices:
        # While our node has children
        while len(graph.vertices[node]) > 0:
            # Pop each of the children it points to
            popped_children = graph.vertices[node].pop()
            # Creates a list of only children with parents (ignores top level nodes)
            children.append(popped_children)
            # Creates a list of children with parents, passing the parent as a second argument
            temp_array.append((popped_children, node))

    print('---------- ARRAYS -----------')
    print('CHILDREN', children)
    print('TEMP', temp_array)
    print('-----------------------------')

    # For each instance in temp_array (list of children with parents)
    for x in temp_array:
        # If the first item exists (matches our starting_node)
        if x[0] == starting_node:
            print(f'yippeekayay, {x[1]} is the parent of {starting_node}')
            print('')
            # If the starting node's parent node is a child (meaning it also has a parent and is not at the top level)
            if x[1] in children:
                # Call recursion on that node to find the top
                return earliest_ancestor(ancestors, x[1])
            # Otherwise, if the parent is not a child, return the parent (you've reached the top)
            else:
                # Returns top level parent (the earliest ancestor)
                return x[1]
        
    # If none of this runs, then the starting_node either does not exist or has no parents
    return -1

    # NOTE
    # Since the temp list is already in order from lowest to highest,
    # If there is more than one ancestor tied to the earliest ancestor
        # We return the one with the lowest numeric ID

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
