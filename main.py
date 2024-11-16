import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from grafo import Grafo
from  algoritmosBusca import AlgoritmosBusca 

BACKGROUND_COLOR = "#4B0082"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#4CAF50"

#Grafo
grafo=Grafo()
figure=grafo.criarGrafo()
listaNos=list(grafo.getGrafo().nodes)


button_style = {
    "font": ("Inter", 10, "bold"),
    "button_color": (TEXT_COLOR, BUTTON_COLOR),
    "border_width": 1,
    "size": (12, 1),
    "pad": (5, 5)
}

layout = [
    [sg.Text("Semáforos Inteligentes", font=("Inter", 24, "bold"), expand_x=True, justification="center", pad=(0, 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR)],

    [sg.Canvas(size=(800, 450), background_color="#F8F8FF", key="-CANVAS-", expand_x=True, expand_y=True, pad=(0, 10))],

    [
        sg.Text("Origem:", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5)),
        sg.Combo(listaNos, key="-ORIGEM-", size=(15, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF"),
        
        sg.Text("Destino:", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5)),
        sg.Combo(listaNos, key="-DESTINO-", size=(15, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF"),
        
        sg.Text("Algoritmo:", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5)),
        sg.Combo(["Profundidade Iterativa", "Busca em Custo Uniforme", "A*"], key="-ALGORITMO-", size=(20, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF")        
    ],

    [
        sg.Button("Buscar", **button_style),
        sg.Button("Resumo", font=("Inter", 10, "bold"), button_color=(TEXT_COLOR, "#008B8B"), border_width=1, size=(12, 1), pad=(5, 10)),
        sg.Button("Reset", font=("Inter", 10, "bold"), button_color=(TEXT_COLOR, "#FF0000"), border_width=1, size=(12, 1), pad=(5, 10))
    ],

    [sg.Text("", size=(1, 1), background_color=BACKGROUND_COLOR)]
]

window = sg.Window("Semáforos Inteligentes - Maputo", layout, resizable=True, finalize=True, background_color=BACKGROUND_COLOR)
textoResumo=""


#Methods
def desenharGrafo(canvas,figure):
    #Limpar os widgets antigos
    for widget in canvas.winfo_children():
        widget.destroy()
        
    figureCanvasAgg=FigureCanvasTkAgg(figure,canvas)
    figureCanvasAgg.draw()#Draw the figure in the canvas
    figureCanvasAgg.get_tk_widget().pack(side="top",fill="both",expand=1)
    return figureCanvasAgg

#Colocar o grafo no canvas
canvas=window["-CANVAS-"].TKCanvas #Creates a tkinter canvas object       // #expand(True, True)
desenharGrafo(canvas,figure)


def validarSelecao(valor,alerta):
    if valor=="":
         sg.popup(alerta)
    else:
        return valor

def formatarCaminho(caminho):
    textoCaminho=caminho.pop(0)
    tamanho=len(caminho)
    #tamanho-=1
    for i in range(tamanho):
        textoCaminho=textoCaminho+" -> "+caminho[i]
    #textoCaminho=textoCaminho+caminho[-1]#Retorna o ultimo no
    print(textoCaminho)
    return textoCaminho

def desenharNosPintados(caminho):
    global figure
    contador=0
    corNormal="#c1121f"
    corVisitados="#008B8B"
    corSolucao="#06d6a0"
    dicionarioCores={}
    for node in grafo.getGrafo().nodes:
        dicionarioCores[node]=corNormal
        
    for elemento in caminho:
        dicionarioCores[elemento]=corVisitados
        figure=grafo.pintarNoSolucao(dicionarioCores)
        desenharGrafo(canvas,figure)
        window.Refresh()   

def  executarAlgoritmo(inicio,objectivo,algoritmo):
    
    match algoritmo:
        case "Busca em Custo Uniforme":
            custoAcumulado,caminho,nosVisitados=AlgoritmosBusca.buscaCustoUniforme(AlgoritmosBusca,grafo.getGrafo(),inicio,objectivo)
            global textoResumo
            textoResumo=f"Caminho da solucao: {formatarCaminho(caminho)}\nCusto total: {custoAcumulado} minutos"
            caminho.insert(0,inicio)
            desenharNosPintados(caminho)

        
        case "Profundidade Iterativa":
            limite,caminho=AlgoritmosBusca.buscaProfundidadeIterativa(grafo.getGrafo(),inicio,objectivo)
            textoResumo=f"Caminho da solucao: {formatarCaminho(caminho)}\nNivel: {limite}"
            caminho.insert(0,inicio)
            desenharNosPintados(caminho)
        
        case "A*":
            custoAcumulado,caminho,visitados=AlgoritmosBusca.buscaAestrela(grafo.getGrafo(),inicio,objectivo)
            textoResumo=f"Caminho da solucao: {formatarCaminho(caminho)}\nCusto total: {custoAcumulado} minutos"
            caminho.insert(0,inicio)
            desenharNosPintados(caminho)
                       
            
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Buscar":
        inicio=validarSelecao(values["-ORIGEM-"],"Por favor selecione a origem!")
        objectivo=validarSelecao(values["-DESTINO-"],"Por favor selecione o destino!")
        algoritmo=validarSelecao(values["-ALGORITMO-"],"Por favor selecione um algoritmo de busca!")
        executarAlgoritmo(inicio,objectivo,algoritmo)
    elif event == "Resumo":
        sg.popup(textoResumo)
        
    elif event == "Reset":
        sg.popup("Parâmetros resetados")
        for key in ["-ORIGEM-", "-DESTINO-", "-ALGORITMO-"]:
            window[key].update("") 
        textoResumo=""
        figure=grafo.criarGrafo()
        desenharGrafo(canvas,figure)

window.close()
