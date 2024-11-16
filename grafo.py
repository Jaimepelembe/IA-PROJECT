import matplotlib.pyplot as plt
import networkx as nx
from ficheiro import Ficheiro
#import numpy as np
#import random 

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

    def receberVertices(self):
        ficheiro=Ficheiro()
        listaVertices=ficheiro.loadData("dadosVertices.json")
        for verticeA,VerticeB,custo in listaVertices:
            self.graph.add_edge(verticeA,VerticeB,gn=custo)
        
    def criarGrafo(self):
        plt.clf()#Limpar grafico antigo
        self.receberNos()
        self.receberVertices()
        colorNodes="#c1121f"
        colorFontNodes="#fdf0d5"
        #Grafo
        nx.draw(self.graph,pos=self.positionOfNodes(),with_labels=True,node_color=colorNodes,node_size=1900, font_color=colorFontNodes,font_size=6,font_family="verdana",font_weight="bold",edge_color="black",width=3)
       
         #Nodes labels
        nodesLabels=self.retornarHeuristicas()        
        nx.draw_networkx_labels(self.graph,pos=self.positionOfNodesLabel(),labels=nodesLabels, font_color="black",font_size=12,font_family="Times New Roman",font_weight="bold")

        #edges labels
        edgeLabels={(nodeA,nodeB):dictionary["gn"] for nodeA,nodeB,dictionary in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph,pos=self.positionOfNodes(),edge_labels=edgeLabels,label_pos=0.5)#label_pos=0.5 puts the label in the middle of the arrow
        
        plt.margins(0.2)
        #plt.show()
        return plt.gcf() #plt.gcf() get the current figure
    
    def pintarNoSolucao(self,dicionarioCores):
        #corVisitados="#ffd166"
        colorFontNodes="#fdf0d5"
        coresNos=[]
        for node, element in dicionarioCores.items():
            coresNos.append(element)
                
        #Grafo
        plt.clf()#Limpar grafico antigo
        nx.draw(self.graph,pos=self.positionOfNodes(),with_labels=True,node_color=coresNos,node_size=1900, font_color=colorFontNodes,font_size=6,font_family="verdana",font_weight="bold",edge_color="black",width=3)
       
        #Nodes labels
        nodesLabels=self.retornarHeuristicas()        
        nx.draw_networkx_labels(self.graph,pos=self.positionOfNodesLabel(),labels=nodesLabels, font_color="black",font_size=12,font_family="Times New Roman",font_weight="bold")

        #edges labels
        edgeLabels={(nodeA,nodeB):dictionary["gn"] for nodeA,nodeB,dictionary in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph,pos=self.positionOfNodes(),edge_labels=edgeLabels,label_pos=0.5)#label_pos=0.5 puts the label in the middle of the arrow
        
        plt.margins(0.2)
        return plt.gcf() #plt.gcf() get the current figure

    def pintarCaminhoSolucao(self,caminho):
        corNormal="#c1121f"
        corVisitados="#ffd166"
        colorFontNodes="#fdf0d5"
        coresNos=[]
        
        for node in self.getGrafo().nodes:
            if node in caminho:
                coresNos.append(corVisitados)
            else:
                coresNos.append(corNormal)
        print("Caminho: ",caminho)
        #Grafo
        plt.clf()#Limpar grafico antigo
        nx.draw(self.graph,pos=self.positionOfNodes(),with_labels=True,node_color=coresNos,node_size=1900, font_color=colorFontNodes,font_size=6,font_family="verdana",font_weight="bold",edge_color="black",width=3)
       
        #Nodes labels
        nodesLabels=self.retornarHeuristicas()        
        nx.draw_networkx_labels(self.graph,pos=self.positionOfNodesLabel(),labels=nodesLabels, font_color="black",font_size=12,font_family="Times New Roman",font_weight="bold")

        #edges labels
        edgeLabels={(nodeA,nodeB):dictionary["gn"] for nodeA,nodeB,dictionary in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph,pos=self.positionOfNodes(),edge_labels=edgeLabels,label_pos=0.5)#label_pos=0.5 puts the label in the middle of the arrow
        
        plt.margins(0.2)
        return plt.gcf(),coresNos #plt.gcf() get the current figure

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


    def positionOfNodes(self):
        position={
            "Inhagoia":(46,5),"Absa":(40,5),"Mogas":(34,5),"Praca Magaia":(28,5),"UIR":(22,5),"Brigada montada":(16,5),"HGJM":(10,5),
            "Versalhes":(4,6),"Jardim Majerman":(-2,6),
            "Guerra popular":(-8,6),
            "Estatua Mondlane":(8,3),
            "Pep":(-7,7),
            "Movitel":(-14,6),
            "Ponto final":(-9,3),
            "Belita":(0,3),
            "Tecnicol":(-15,3)}    
        return position 
    
    def positionOfNodesLabel(self):
        positionOfLabel={}
        for node,data in self.positionOfNodes().items():
            positionOfLabel[node]=(data[0]-0.6,data[1]+0.35)
        return positionOfLabel

