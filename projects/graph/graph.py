"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # Creates a set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # If both vertices are in the graph
        if v1 in self.vertices and v2 in self.vertices:
            # Add a one-way link for vertex one to vertex two
	        self.vertices[v1].add(v2)
        #Otherwise, provide an error explaining the vertex does not exist
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Add the starting_vertex to the queue
        q = Queue()
        q.enqueue(starting_vertex)

        # Keep track of the visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:
            # Dequeue first vertex
            v = q.dequeue()
            # If the vertex is not visited
            if v not in visited:
                # Print the vertex in breadth-first order
                print(v)
                # Mark the vertex as visited
                visited.add(v)

                # For the next vertex with linkages, add it to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Add the starting_vertex to the stack
        s = Stack()
        s.push(starting_vertex)

        # Keep track of the visited nodes
        visited = set()

        # Repeat until stack is empty
        while s.size() > 0:
            # Remove the last vertex in the stack
            v = s.pop()
            # If the vertex is not visited
            if v not in visited:
                # Print the vertex in depth-first order
                print(v)
                # Mark the vertex as visited
                visited.add(v)

                # For the next vertex with linkages, add it to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # If visited is empty, set it to an empty set object
        if visited is None:
            visited = set()

        # If our starting vertex is not in the visted set
        if starting_vertex not in visited:
            # Print the vertex in depth-first order
            print(starting_vertex)
            # Mark the vertex as visited
            visited.add(starting_vertex)

            # For the next vertex with linkages, add it to the stack
            for next_vert in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_vert, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                # IF SO, RETURN PATH
                    return path
                else:
                    # Mark it as visited...
                    visited.add(v)
                    # Then add A PATH TO its neighbors to the back of the queue
                    for next_vert in self.get_neighbors(v):
                        # _COPY_ THE PATH
                        p_copy = path.copy()
                        # APPEND THE NEIGHOR TO THE BACK
                        p_copy.append(next_vert)
                        q.enqueue(p_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # Check if it's the target
                if v == destination_vertex:
                # If so, return PATH
                    return path
                # Otherwise, 
                else:
                    # Mark it as visited
                    visited.add(v)
                    # Then add A PATH TO its neighbors to the top of the stack
                    for next_vert in self.get_neighbors(v):
                        # _COPY_ THE PATH
                        p_copy = path.copy()
                        # APPEND THE NEIGHOR TO THE BACK
                        p_copy.append(next_vert)
                        s.push(p_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    # print(graph.get_neighbors(4))

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
