import matplotlib.pyplot as plt
import networkx as nx
from ficheiro import Ficheiro
import numpy as np
import random 

#seed=1
#random.seed(seed)
#np.random.seed(seed)#Usamos random seed para que a saida do grafo seja a mesma sempre

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

    def retornarCustos(self):
        dicionarioCustos={}
        dicionarioCustos={(nodeA,nodeB):dictionary["gn"] for nodeA,nodeB,dictionary in self.graph.edges(data=True)}   
        return dicionarioCustos
    
    
        
    def retornarHeuristicas(self):
       #dicionarioHeuristicas={node:dictionary for node,dictionary["hn"] in self.graph.nodes(data=True)}
        dicionarioHeuristicas={}
        for node, dictionary in self.graph.nodes(data=True):
            dicionarioHeuristicas[node]=dictionary["hn"]
        return dicionarioHeuristicas

    def getGrafo(self):
        return self.graph
    
    def desenharGrafo(self):
        #Grafo
        nx.draw(self.graph,pos=self.positionOfNodes(),with_labels=True,node_color="red",node_size=3000, font_color="white",font_size=8,font_family="Times New Roman",font_weight="bold",edge_color="black",width=3)

        #Nodes labels
        nodesLabels=self.retornarHeuristicas()
        #{node:dictionary["hn"] for node,dictionary in self.graph.nodes(data=True)}
        
        #nx.draw_networkx_labels(self.graph,pos=,labels=nodesLabels, font_color="black",font_size=12,font_family="Times New Roman",font_weight="bold")


        #edges labels
        edgeLabels={(nodeA,nodeB):dictionary["gn"] for nodeA,nodeB,dictionary in self.graph.edges(data=True)}
        #nx.draw_networkx_edge_labels(self.graph,edge_labels=edgeLabels,label_pos=0.5)#label_pos=0.5 puts the label in the middle of the arrow
        plt.margins(0.2)
        plt.show()
    
    def positionOfNodes(self):
        position={
            "Inhagoia":(32,5),"Absa":(28,5),"Mogas":(24,5),"Praca Magaia":(20,5),"UIR":(16,5),"Brigada montada":(12,5),"HGJM":(8,9),
            "Versalhes":(0.067,0.071),"Estatua Mondlane":(16,2),
            "Jardim Majerman":(6,9),
            "Guerra popular":(6,9),
            "Pep":(6,9),
            "Movitel":(6,9),
            "Ponto final":(6,9),
            "Belita":(24,-0.7),
            "Tecnicol":(22,-0.7)}    
        return position 
g=Grafo()        
g.inicializarGrafo()
g.retornarHeuristicas()
g.desenharGrafo()

print("Numero nos:",g.getGrafo().nodes())
print("Numero nos:",g.getGrafo().number_of_nodes())

