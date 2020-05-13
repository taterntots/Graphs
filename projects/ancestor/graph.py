from util import Queue

class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, int):
    if not int in self.vertices:
      self.vertices[int] = set()

  def add_edge(self, int1, int2):
    if int1 in self.vertices and int2 in self.vertices:
      # IMPORTANT! HAD TO FLIP INT2 AND INT1
      self.vertices[int2].add(int1)
    else:
      raise KeyError("Key doesn't exist")

  def get_neighbors(self, vertex_id):
    return self.vertices[vertex_id]

  def bfs(self, starting_node):
    q = Queue()
    q.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    # print(q.queue)

    while q.size() > 0:
      # Dequeue the first path
      path = q.dequeue()
      # print(path)
      # Grab the last vertex from the path
      v = path[-1]
      # print(v)
      
      # If the path is longer or equal and the value is smaller, or if the path is longer
      if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
        # Set the earliest ancestor to the vert
        earliest_ancestor = v
        # Set the max path length to the length of the path
        max_path_length = len(path)
      
      # Loop over each neighbor in the graphs vertices
      for neighbor in self.get_neighbors(v):
        # _COPY_ THE PATH
        p_copy = path.copy()
        # APPEND THE NEIGHOR TO THE BACK
        p_copy.append(neighbor)
        q.enqueue(p_copy)

    return earliest_ancestor

# def earliest_ancestor(ancestors, starting_node):
#     # Build the Graph
#     graph = Graph()
#     # Add the vertices for the parent and child
#     for (parent, child) in ancestors:
#         graph.add_vertex(parent)
#         graph.add_vertex(child)
#         # Create linkages from the ancestors list
#         graph.add_edge(parent, child)

#     # print(graph.vertices)
#     return graph.bfs(starting_node)

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 6))