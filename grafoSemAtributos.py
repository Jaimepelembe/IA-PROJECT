import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random 

#seed=0
#random.seed(seed)
#np.random.seed(seed)#Usamos random seed para que a saida do grafo seja a mesma sempre


graph=nx.Graph()
#Adding nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
#Adding using a list
#graph.add_nodes_from(["A","B","C","D","E","F"]) 
#or we can use a string  
#graph.add_nodes_from("ABCDEF")

#Adding graph edges
graph.add_edge("A","C")
graph.add_edge("B","C")
graph.add_edge("B","D")
graph.add_edge("C","D")
graph.add_edge("D","E")
graph.add_edge("E","F")

#Adding using a list
#graph.add_edges_from([("A","C"),("B","C"),("B","D"),("C","D"),("D","E"),("E","F")])
#Or using strings
#graph.add_edges_from(["AC","BC","BD","CD","DE","EF"])

position={
    "A":(0,5),
    "B":(4.5,6.6),
    "C":(3.6,1.4),
    "D":(5.8,3.5),
    "E":(7.9,3.6),
    "F":(6,9)
}


#Attributed graph

#Attributes of a social network


#drawing the graph
nx.draw(graph,pos=position,with_labels=True,node_color="red",node_size=3000,
        font_color="white",font_size=20,font_family="Times New Roman",font_weight="bold",width=3)
plt.margins(0.2)
plt.show()
#print(graph)