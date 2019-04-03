class Node:
  def __init__(self, idty, data):
    self.label = idty
    self.data = data

class Edge:
  def __init__(self, src, dest):
    self.src, self.dest = src, dest

class Graph:
  def __init__(self, nodes, edges):
    self.nodes = nodes
    self.edges = edges

def dfs_rec(graph, node, visited):
  if not visited[node]:
    visited[node] = True
    print node,
    for neighbour in graph[node]:
      if not visited[neighbour]:
        dfs_rec(graph, neighbour, visited)

def dfs_iter(graph, node, visited):
  stack = [node]
  while stack:
    node = stack.pop()
    if not visited[node]:
      visited[node] = True
      print node,
      for neighbour in graph[node]:
        if not visited[neighbour]:
          stack.append(neighbour)
          
def bfs_rec(graph, queue, visited):
  tmp = []
  for node in queue:
    print node,
    visited[node] = True
    tmp.extend(graph[node])
  unvisited = [n for n in tmp if not visited[n]]
  if unvisited:
    bfs_rec(graph, unvisited, visited)    

def bfs_iter(graph, queue, visited):
  tmp = []
  while queue:
    node = queue.pop()
    print node,
    visited[node] = True
    for neighbour in graph[node]:
      if not visited[neighbour]:
        tmp.insert(0, neighbour)
    queue = [n for n in tmp 
            if not visited[n]]
    

def traverse(graph, f):
  print "-- %s --" % f.func_name
  n, comps = len(graph), 0
  visited = [False] * n
  for i in xrange(n):
    if not visited[i]:
      comps += 1
      f(graph, i if f.func_name.startswith("dfs") else [i] , visited)
  print "-" * 14
  print comps

labels = [4, 5, 6, 8, 9]
id_to_node = dict(enumerate(labels))
nodes = [Node(i, value) for (i, value) in id_to_node.items()]
edges = [Edge(nodes[0], nodes[1]),
         Edge(nodes[1], nodes[3]),
         Edge(nodes[0], nodes[2]),
         Edge(nodes[1], nodes[2])]
graph = Graph(nodes, edges)

n = 10
adj_list = [[] for _ in xrange(n)]

edges = [ [2, 0, 2],
          [2, 3, 1],
          
          [4, 7, 10],
          [6, 5, 4],
          [5, 4, 1],
          [1, 4, 0],
          [8, 1, 0],
          [4, 6, 10],
          [8, 9, 15]]

for u, v, _ in edges:
  adj_list[u].append(v)
  adj_list[v].append(u)
  
for i, row in enumerate(adj_list):
  print str(i) + " | " +  " ".join(map(str, row))
print

traverse(adj_list, dfs_rec)
traverse(adj_list, bfs_rec)
traverse(adj_list, dfs_iter)
traverse(adj_list, bfs_iter)