import matplotlib.pyplot as plt
import networkx as nx
from ficheiro import Ficheiro

class Grafo:
    
    def __init__(self):
        self.graph = nx.Graph()
    
    def receberNos(self):
        ficheiro = Ficheiro()
        listaNos = ficheiro.loadData("dadosNos.json")
        lista = [] 
        for node, data in listaNos:
            if node not in lista:
                lista.append(node)
                self.graph.add_node(node, hn=data)            

    def receberVertices(self):
        ficheiro = Ficheiro()
        listaVertices = ficheiro.loadData("dadosVertices.json")
        for verticeA, VerticeB, custo in listaVertices:
            self.graph.add_edge(verticeA, VerticeB, gn=custo)

    def inicializarGrafo(self):
        self.receberNos()
        self.receberVertices()

    def retornarCustos(self):
        dicionarioCustos = {(nodeA, nodeB): dictionary["gn"] for nodeA, nodeB, dictionary in self.graph.edges(data=True)}   
        return dicionarioCustos
    
    def retornarHeuristicas(self):
        dicionarioHeuristicas = {}
        for node, dictionary in self.graph.nodes(data=True):
            dicionarioHeuristicas[node] = dictionary["hn"]
        return dicionarioHeuristicas

    def getGrafo(self):
        return self.graph
    
    def gerarImagemGrafo(self):
        colorNodes = "#1D193A"
        fontNodes = "#fdf0d5"
        pos = nx.spring_layout(self.graph, seed=42, k=0.25)
        plt.figure(figsize=(12, 10))
        nx.draw(self.graph, pos=pos, with_labels=True, node_color=colorNodes, node_size=6000, 
                font_color=fontNodes, font_size=10, font_family="verdana", font_weight="bold", edge_color="gray", width=2)
        nodesLabels = self.retornarHeuristicas()
        nx.draw_networkx_labels(self.graph, pos=pos, labels=nodesLabels, font_color="black", 
                                font_size=12, font_family="Times New Roman", font_weight="bold")
        edgeLabels = {(nodeA, nodeB): dictionary["gn"] for nodeA, nodeB, dictionary in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edgeLabels, font_size=8, font_color="blue", label_pos=0.5)
        img_path = "grafo_temp.png"
        plt.margins(0.05)
        plt.axis("off")
        plt.savefig(img_path, format='PNG', dpi=300)
        plt.show()
        plt.close()

        return img_path

    def positionOfNodes(self):
        position = {
            "Inhagoia":(46,5), "Absa":(40,5), "Mogas":(34,5), "Praca Magaia":(28,5), "UIR":(22,5), "Brigada montada":(16,5), 
            "HGJM":(10,5), "Versalhes":(4,6), "Jardim Majerman":(-2,6), "Guerra popular":(-8,6), "Estatua Mondlane":(8,3), 
            "Pep":(-7,7), "Movitel":(-14,6), "Ponto final":(-9,3), "Belita":(0,3), "Tecnicol":(-15,3)}    
        return position 

    def positionOfNodesLabel(self):
        positionOfLabel = {}
        for node, data in self.positionOfNodes().items():
            positionOfLabel[node] = (data[0] - 0.6, data[1] + 0.35)
        return positionOfLabel
