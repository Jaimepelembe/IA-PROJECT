import PySimpleGUI as sg
import tkinter as tk
from grafo import Grafo

BACKGROUND_COLOR = "#4B0082"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#229954"

button_style = {
    "font": ("Inter", 10, "bold"),
    "button_color": (TEXT_COLOR, BUTTON_COLOR),
    "border_width": 1,
    "size": (12, 1),
    "pad": (5, 5)
}

layout = [
    [sg.Text("Semáforos Inteligentes", font=("Inter", 24, "bold"), expand_x=True, justification="center", pad=(0, 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR)],
    [sg.Canvas(size=(800, 400), key="-CANVAS-", expand_x=True, expand_y=True, background_color="#F5EEF8", pad=(0, 10))],
    [
        sg.Text("Origem:", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5)),
        sg.Combo(["Inhagoia", "Absa", "Mogas", "Praca Magaia", "UIR", "Brigada montada", "HGJM", "Versalhes", "Jardim Majerman", "Guerra popular", "Estatua Mondlane", "Pep", "Movitel", "Ponto final", "Belita", "Tecnicol"], key="-ORIGEM-", size=(15, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF"),
        sg.Text("Destino:", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5)),
        sg.Combo(["Inhagoia", "Absa", "Mogas", "Praca Magaia", "UIR", "Brigada montada", "HGJM", "Versalhes", "Jardim Majerman", "Guerra popular", "Estatua Mondlane", "Pep", "Movitel", "Ponto final", "Belita", "Tecnicol"], key="-DESTINO-", size=(15, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF"),
        sg.Text("Algoritmo:", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5)),
        sg.Combo(["Profundidade Iterativa", "Busca em Custo Uniforme", "A*"], key="-ALGORITMO-", size=(20, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF"),
        sg.Button("Buscar", **button_style),
        sg.Button("Resumo", font=("Inter", 10, "bold"), button_color=(TEXT_COLOR, "#F1C40F"), border_width=1, size=(12, 1), pad=(5, 5)),
        sg.Button("Reset", font=("Inter", 10, "bold"), button_color=(TEXT_COLOR, "#FF0000"), border_width=1, size=(12, 1), pad=(5, 5))
    ],
    [sg.Text("", size=(1, 1), background_color=BACKGROUND_COLOR)]
]

window = sg.Window("Semáforos Inteligentes - Maputo", layout, resizable=True, finalize=True, background_color=BACKGROUND_COLOR)
canvas_elem = window["-CANVAS-"]
canvas = canvas_elem.TKCanvas

g = Grafo()
g.inicializarGrafo()

def desenhar_grafo_no_canvas(grafo):
    canvas.delete("all")
    pos = g.positionOfNodes()
    scale_factor = 20
    offset_x, offset_y = 350, 100

    for edge in grafo.edges():
        node1, node2 = edge
        x1, y1 = pos[node1]
        x2, y2 = pos[node2]
        canvas.create_line(x1 * scale_factor + offset_x, y1 * scale_factor + offset_y,
                           x2 * scale_factor + offset_x, y2 * scale_factor + offset_y, fill="black", width=1)

    for node in grafo.nodes():
        x, y = pos[node]
        x, y = x * scale_factor + offset_x, y * scale_factor + offset_y
        canvas.create_oval(x-25, y-25, x+25, y+25, fill="#229954")
        canvas.create_text(x, y, text=node, fill="white", font=("Inter", 6, "bold"))

desenhar_grafo_no_canvas(g.getGrafo())

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Buscar":
        sg.popup("Busca iniciada com parâmetros:", values)
    elif event == "Resumo":
        sg.popup("Mostrando resumo dos dados.")
    elif event == "Reset":
        for key in ["-ORIGEM-", "-DESTINO-", "-ALGORITMO-"]:
            window[key].update("")

window.close()
