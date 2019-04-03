import table
import graph

edges = [("u", "v"),
				 ("v", "y"),
				 ("y", "x"),
				 ("u", "x"),
				 ("x", "v"),
				 ("w", "y"),
				 ("w", "z"),
				 ("z", "z")]

print 'Execution: python graph_test.py\n\n'
print 'Edges'
table.Table.print_table([["from", "to"]] + edges)
print
g = graph.Graph(edges)

g.bfs()
print
g.dfs()

