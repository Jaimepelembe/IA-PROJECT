import matplotlib.pyplot as plt
import networkx as nx
import PySimpleGUI as sg
#Attributed graph
#Attributes of a social network

graph=nx.Graph()
#Adding nodes
graph.add_node("A",age=19,gender='M')
graph.add_node("B",age=18,gender='M')
graph.add_node("C",age=22,gender='M')
graph.add_node("D",age=18,gender='F')
graph.add_node("E",age=17,gender='F')
graph.add_node("F",age=20,gender='F')

#Adding using a list
#graph.add_edges_from([
    # ("A",{age=19,gender='M'}),
    # ("B", {age=18,gender='M'}),
    # ("C",{age=22,gender='F'}),
    # ("D",{age=19,gender='F'})])

#Adding graph edges with attributes
graph.add_edge("A","C",custo=1,distancia=20)
graph.add_edge("B","C",custo=0.5)
graph.add_edge("B","D",custo=0.6)
graph.add_edge("C","D",custo=0.8)
graph.add_edge("D","E",custo=1)
graph.add_edge("E","F",custo=0.7)

#Adding using a list
#graph.add_edges_from([("A","C",{"weight":1}),
# ("B","C",{"weight":0.1}),
# ("B","D",{"weight":0.4}),
# ("C","D",{"weight":0.5}),
# ("D","E",{"weight":1.2}),
# ("E","F",{"weight":2})])


#Getting the attributes of the nodes
#print(graph.nodes["A"])
#Attributes of the edge
#print(graph.edges[("A","C")])

#for vizinho,value in graph["A"].items():
    #print(vizinho, value)
#    print(graph.edges["A",vizinho]["distancia"])
    



print(graph.nodes["A"])
#print(graph.edges[("A","C")]["custo"])

#Proprieties of the graph
#graph.graph["Name"]="Semafros inteligentes"
#print(graph.graph)

position={
    "A":(0,5),
    "B":(4.5,6.6),
    "C":(3.6,1.4),
    "D":(5.8,3.5),
    "E":(7.9,3.6),
    "F":(6,9)
}

#loop throught all nodes
#for node in graph.nodes(data=True):#data gives us all the data of each node
#    print(node[1])
#    print(node[1]["age"])

#loop trhought all edges
#for edge in graph.edges(data=True):#data gives us all the data of each node
#    print(edge)
    
    
 #Number of nodes and edges
#print(f"The number of nodes is : {graph.number_of_nodes()}")   
#print(f"The number of edges is : {graph.number_of_edges()}")   

#Get the neighbors of each node
#for node in graph.nodes:
#    neighborList=[n for n in graph.neighbors(node)]
#    print(f"Neighbor of ({node})={neighborList}" )
    

#Priting attributes the labels
#First method: Hand typing
positionNodeAttributes={
    "A":(-0.2,5),
    "B":(4.5,7.5),
    "C":(2.4,1.4),
    "D":(5.8,2.5),
    "E":(9.1,3.6),
    "F":(8,4.6)
    }

#Creating the labels position using a for loop
positionNodeAttributes2={}

for node,(x,y) in position.items():
    positionNodeAttributes2[node]=(x+1.5,y-0.2)

#drawing the graph with costs
nx.draw(graph,pos=position,with_labels=True,node_color="red",node_size=3000,
        font_color="white",font_size=20,font_family="Times New Roman",font_weight="bold",edge_color="black",width=3)

#Nodes labels
nodesLabels={node:(dictionary["age"],dictionary["gender"]) for node,dictionary in graph.nodes(data=True)}
nx.draw_networkx_labels(graph,pos=positionNodeAttributes2,labels=nodesLabels, font_color="black",font_size=12,font_family="Times New Roman",font_weight="bold")


#edges labels
edgeLabels={(nodeA,nodeB):dictionary["custo"] for nodeA,nodeB,dictionary in graph.edges(data=True)}
nx.draw_networkx_edge_labels(graph,pos=position,edge_labels=edgeLabels,label_pos=0.5)#label_pos=0.5 puts the label in the middle of the arrow

#for node,dictionary in graph.nodes(data=True):
#    print(node)
#    print(dictionary)
#    print("+++++++++++")

plt.margins(0.2)
plt.show()