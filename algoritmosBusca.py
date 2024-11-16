from collections import deque
import heapq
import networkx as nx


class AlgoritmosBusca:

    def caminhoSolucao(dicionarioPais,vertice,nosVisitados):
        caminho=[]
        while vertice is not None:
            if vertice in nosVisitados:
                caminho.append(vertice)
                vertice=dicionarioPais.get(vertice)
        caminho.reverse()
        return caminho
                
    def buscaCustoUniforme(self,grafo,inicio,objectivo):
        fila=[(0,inicio)] #Custo de caminho e o estado inicial
        visitados=set()
        caminho={} #dicionario para armazenar o pai de cada nó
        caminho[inicio]=None
        
        while fila:
            custoAcumulado,vertice=heapq.heappop(fila) #Atribui o custo acumulado e o vertice actual
            if vertice not in visitados:
                visitados.add(vertice)
               
               #Verirfica se o objectivo foi alcançado
                if vertice == objectivo:
                    #Reconstruir o caminho a partir do dicionário
                    path=self.caminhoSolucao(caminho,objectivo,visitados)
                    return custoAcumulado,path,visitados
               
                for vizinho in grafo.neighbors(vertice):
                    custoActual=grafo.edges[vertice,vizinho]["gn"]
                    heapq.heappush(fila,(custoAcumulado+custoActual,vizinho))
                    #Armazenar o pai do vizinho actual
                    if not vizinho==inicio and vertice in visitados and vizinho not in caminho.keys():
                        caminho[vizinho]=vertice
                        
                         
    def buscaAestrela(grafo,inicio,objectivo):
        fila=[]
        heuristicaInicial=grafo.nodes[inicio]["hn"]
        heapq.heappush(fila,(heuristicaInicial,0,inicio,[]))#(Heuristica inicial(f),custo real(g),vertice inicial, caminho)
        custoActual=0
        visitados=set()
        
        while fila:
            funcaoAvaliacao, custoReal,vertice, caminho =heapq.heappop(fila)
            caminho=caminho+[vertice]
            
            if vertice in visitados:
                continue
            visitados.add(vertice)
            
            if vertice == objectivo: 
                return custoReal,caminho,visitados
            
            for vizinho in grafo.neighbors(vertice):
                if vizinho not in visitados:
                    custoVizinho=grafo.edges[vertice,vizinho]["gn"]
                    custoActual = custoReal+custoVizinho
                    heuristica=grafo.nodes[vizinho]["hn"] #Heuristica do novo vizinho
                    funcaoAvaliacao=custoActual+heuristica
                    heapq.heappush(fila,(funcaoAvaliacao,custoActual,vizinho,caminho))


    def buscaProfundidadeIterativa(grafo,inicio,objectivo):
        
        def buscaEmAprofundamentoLimitado(vertice,limite,nosVisitados):
            if vertice==objectivo:
                return True
            if limite==0:
                return False
            
            nosVisitados.append(vertice)
            
            for vizinho in grafo.neighbors(vertice):
                if vizinho not in nosVisitados and buscaEmAprofundamentoLimitado(vizinho,limite-1, nosVisitados):
                    return True
            nosVisitados.remove(vertice)
            return False
        limite=0
        
        while True:
            nosVisitados=[]
            if buscaEmAprofundamentoLimitado(inicio,limite,nosVisitados):
                nosVisitados.append(objectivo)
                return limite,nosVisitados
            limite+=1