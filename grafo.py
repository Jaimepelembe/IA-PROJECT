import matplotlib.pyplot as plt
import networkx as nx
from ficheiro import Ficheiro

class Grafo:
    
    def __init__(self):
        self.graph=nx.Graph()
    
    def receberNos(self):
        ficheiro=Ficheiro()
        listaNos=ficheiro.loadData("dadosNos.json")
        for node ,data in listaNos:
            self.graph.add_node(node,hn=data)
          

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
      
    def retornarHeuristicas(self):
       #dicionarioHeuristicas={node:dictionary for node,dictionary in self.graph.nodes(data=True)}
        dicionarioHeuristicas={}
        lista=[]
        for node, dictionary in self.graph.nodes(data=True):
            if "Tecnicol" not in lista:
                lista.append(node)
                dicionarioHeuristicas[node]=dictionary["hn"]
        return dicionarioHeuristicas
    
    
g=Grafo()        
g.inicializarGrafo()
g.retornarHeuristicas()

