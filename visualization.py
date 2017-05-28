import networkx as nx
import matplotlib.pyplot as plt
import Ullmann

matrix=Ullmann.read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1")
g=nx.Graph()
for i in range(len(matrix)):
    g.add_node(i)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]==0:
            g.add_edge(i,j)
#g=nx.dodecahedral_graph()
nx.draw(g,)
plt.draw()
plt.show()
