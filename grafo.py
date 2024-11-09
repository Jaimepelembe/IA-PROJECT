import matplotlib.pyplot as plt
import networkx as nx
from ficheiro import Ficheiro

class Grafo:
    
    def __init__(self):
        self.graph=nx.Graph()
    
    def receberNos(self):
        ficheiro=Ficheiro()
        listaNos=ficheiro.loadData("dadosNos.json")
        lista=[] 
        for node ,data in listaNos:
            if node not in lista:
                lista.append(node)
                self.graph.add_node(node,hn=data)
                print("No: ",node,"Heuristica: ",data)
            
          

    def receberVertices(self):
        ficheiro=Ficheiro()
        listaVertices=ficheiro.loadData("dadosVertices.json")
        for verticeA,VerticeB,custo in listaVertices:
            self.graph.add_edge(verticeA,VerticeB,gn=custo)
        
    
    def inicializarGrafo(self):
        self.receberNos()
        self.receberVertices()
        
        """print("-----Nos-----")
       # print(self.graph.nodes) # Nos do grafo
        for node in self.graph.nodes(data=True):
            print(node)
       
        print("-----Vertices-----")
        for vertice in self.graph.edges(data=True):
            print(vertice)
        """

    def retornarCustos(self):
        dicionarioCustos={}
        dicionarioCustos={(nodeA,nodeB):dictionary["gn"] for nodeA,nodeB,dictionary in self.graph.edges(data=True)}   
        return dicionarioCustos
    
    def desenharGrafo(self):
        #Grafo
        nx.draw(self.graph,with_labels=True,node_color="red",node_size=3000,
        font_color="white",font_size=8,font_family="Times New Roman",font_weight="bold",edge_color="black",width=3)

        #Nodes labels
        nodesLabels={node:(dictionary) for node,dictionary in self.graph.nodes(data=True)}
       # nx.draw_networkx_labels(self.graph,labels=nodesLabels, font_color="black",font_size=12,font_family="Times New Roman",font_weight="bold")
      
        #edges labels
        edgeLabels={(nodeA,nodeB):dictionary["gn"] for nodeA,nodeB,dictionary in self.graph.edges(data=True)}
        #nx.draw_networkx_edge_labels(self.graph,edge_labels=edgeLabels,label_pos=0.5)#label_pos=0.5 puts the label in the middle of the arrow
        plt.margins(0.2)
        plt.show()
        
    def retornarHeuristicas(self):
       #dicionarioHeuristicas={node:dictionary for node,dictionary in self.graph.nodes(data=True)}
        dicionarioHeuristicas={}
        lista=[] 
        for node, dictionary in self.graph.nodes(data=True):
            if "Tecnicol" not in lista:
                lista.append(node)
                dicionarioHeuristicas[node]=dictionary["hn"]
        return dicionarioHeuristicas

    def getGrafo(self):
        return self.graph
    
g=Grafo()        
g.inicializarGrafo()
g.retornarHeuristicas()
g.desenharGrafo()

print("Numero nos:",g.getGrafo().nodes())
print("Numero nos:",g.getGrafo().number_of_nodes())

