from collections import deque
import heapq



class AlgoritmosBusca:

    def breadthFirstSearch(graph,startNode):
        nodesVisited=set()
        fila=deque([startNode])
        
        while fila:
            vertice=fila.popleft()
            if vertice not in nodesVisited:
                nodesVisited.add(vertice)
                print(vertice,end='')
                fila.extend(graph[vertice]-nodesVisited)
                
                
    def buscaCustoUniforme(grafo,inicio,objectivo):
        fila=[(0,inicio)] #Custo de caminho e o estado inicial
        visitados=set()
        
        while fila:
            custoAcumulado,vertice=heapq.heappop(fila) #Atribui o custo a cumulado e o vertice actual
            if vertice not in visitados:
                visitados.add(vertice)
                if vertice == objectivo:
                   # print("Nos visitados",visitados)
                    print(f"Custo ate {vertice}: {custoAcumulado}")
                    return
                for vizinho in grafo[vertice]:
                    if vizinho not in visitados:
                        custoActual=grafo[vertice][vizinho][0]
                        heapq.heappush(fila,(custoAcumulado+custoActual,vizinho))
                        #Ao entrar no nó vizinho esta deve ser pintado de outra cor na interface.
                        #heapq.heappush(fila,(custoAcumulado+custos[(vertice,vizinho)],vizinho))
                        
                    
                         
    def buscaAestrela(grafo,inicio,objectivo):
        fila=[]
        lista=list(grafo[inicio].keys())
        heuristicaInicial=grafo[inicio][lista[0]][1]# a lista[0][1] me retorna a heuristica do primeiro elemento do grafo
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
                print(f"Caminho ate o objectivo: {caminho} com custo {custoReal}")   
                return
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    custoVizinho=grafo[vertice][vizinho][0]
                    custoActual = custoReal+custoVizinho
                    heuristica=grafo[vertice][vizinho][1] #Heuristica do novo vizinho
                    funcaoAvaliacao=custoActual+heuristica
                    heapq.heappush(fila,(funcaoAvaliacao,custoActual,vizinho,caminho))
                    #print("custo actual: ",custoActual)
                    #print("funcao: ",funcaoAvaliacao )
              

    def buscaProfundidadeIterativa(grafo,inicio,objectivo):
        
        def buscaEmAprofundamentoLimitado(vertice,limite,visitados):
            if vertice==objectivo:
                return True
            if limite==0:
                return False
            visitados.add(vertice)
            
            for vizinho in grafo[vertice]:
                if vizinho not in visitados and buscaEmAprofundamentoLimitado(vizinho,limite-1, visitados):
                    return True
            visitados.remove(vertice)
            return False
            
        limite=0
        while True:
            visitados=set()
            if buscaEmAprofundamentoLimitado(inicio,limite,visitados):
                print(f"Objectivo {objectivo} encontrado no nivel {limite}")
                return
            limite+=1
        


