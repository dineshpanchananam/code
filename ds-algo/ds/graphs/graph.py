import table
import operator
from copy import copy
from collections import deque

'''
TODO
Topological Sort
Dijkstra SSSP
Prim's / Kruskal's MST
Strongly Connected components

DONE
DFS and its analysis
BFS and its analysis
'''

class Graph:
	def __init__(self, edges, vertices=-1, directed=True):
		self.edges = edges
		self.vertices = set()
		for u, v in edges:
			self.vertices.add(u)
			self.vertices.add(v)
		self.n = len(self.vertices)
		if vertices != -1:
			assert vertices == self.n
		self.num_to_names = dict(enumerate(self.vertices))
		self.name_to_nums = {x: y for (y, x) in self.num_to_names.iteritems()}
		self.named_edges = self.edges
		self.edges = [(self.name_to_nums[u],
									 self.name_to_nums[v]) for (u, v) in self.edges]
		self.graph = [[] for _ in range(self.n)]
		for u, v in self.edges:
			self.graph[u].append(v)
			if not directed:
				self.graph[v].append(u)

	def bfs(self, source=0):
		# returns the bfs-tree of the graph
		# while printing the source-destination-distance table.
		n = self.n
		queue = deque()
		pred = [None for _ in range(n)]
		dist = ['infinity' for _ in range(n)]
		discovered = [False for _ in range(n)]
		visited = copy(discovered)
		dist[source] = 0
		discovered[source] = True
		queue.append(source)

		bfs_tree = []
		while queue:
			node = queue.popleft()
			if not visited[node]:
				for v in self.graph[node]:
					if not discovered[v]:
						if dist[v] == 'infinity' or dist[v] > dist[node] + 1:
							dist[v] = dist[node] + 1
							pred[v] = node
						bfs_tree.append((self.num_to_names[node], self.num_to_names[v]))
						discovered[v] = True
						queue.append(v)
				visited[node] = True
		print 'BFS Results'
		table.Table.print_table([['Source', 'Destination', 'Distance', 'Predecessor']] + 
														[(self.num_to_names[source], self.num_to_names[x], str(dist[x]), str(pred[x]) 
															if pred[x] is None else self.num_to_names[pred[x]]) 
														 for x in range(n)])
		print "BFS Tree:", ", ".join('->'.join(edge) for edge in bfs_tree) 
		return bfs_tree

	def dfs(self):
		# return the depth-first-forest
		# while printing the analysis
		print "DFS Results"
		n = self.n
		discovery_time = [None for _ in range(n)]
		finish_time = [None for _ in range(n)]
		discovered = [False for _ in range(n)]
		visited = [False for _ in range(n)]
		self.clock = 1

		tree_edges = []
		back_edges = []
		forward_edges = []
		cross_edges = []

		def dfs_visit(self, u):
			discovered[u] = True
			discovery_time[u] = self.clock
			self.clock += 1
			for v in self.graph[u]:
				if visited[v]:
					if discovery_time[u] < discovery_time[v]:
						forward_edges.append((u, v))
					else:
						cross_edges.append((u, v))
				elif discovered[v]:
					back_edges.append((u, v))
				else:
					tree_edges.append((u, v))
					dfs_visit(self, v)
			finish_time[u] = self.clock
			visited[u] = True
			self.clock += 1

		for v in range(n):
			if not visited[v]:
				dfs_visit(self, v)

		h1 = ["Vertex", "Discovery Time", "Finishing Time"]
		records = sorted([[self.num_to_names[i],
											 discovery_time[i],
											 finish_time[i]] for i in range(n)]
										 ,key=operator.itemgetter(1))
		table.Table.print_table([h1] + map(lambda r: map(str, r), records))

		f = lambda edges: ", ".join(map(lambda (u, v): 
																		'%s->%s'%(self.num_to_names[u], 
																							self.num_to_names[v]), edges))

		h2 = ["Edge Classification", "Edges"]
		table.Table.print_table([h2] + [['Tree Edges', f(tree_edges)],
		 ['Back Edges', f(back_edges)],
		 ['Forward Edges', f(forward_edges)],
		 ['Cross Edges', f(cross_edges)]])

		starting_times = { self.num_to_names[y]: discovery_time[y] for y in range(n)}
		ending_times = { self.num_to_names[y]: finish_time[y] for y in range(n)}

		return { 'discovery_times': starting_times,
						 'finish_times': ending_times,
						 }.update({ edgetype: [[self.num_to_names[u] for u in edge] for edge in edges]
											 for (edgetype, edges) in [("tree_edges", tree_edges),
																								 ("back_edges", back_edges),
																								 ("forward_edges", forward_edges),
																								 ("cross_edges", cross_edges)] })
