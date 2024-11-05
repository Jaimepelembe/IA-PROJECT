import PySimpleGUI as sg

BACKGROUND_COLOR = "#4B0082"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#4CAF50"

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
        sg.Combo([], key="-ORIGEM-", size=(15, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF"),
        
        sg.Text("Destino:", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5)),
        sg.Combo([], key="-DESTINO-", size=(15, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF"),
        
        sg.Text("Algoritmo:", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5)),
        sg.Combo(["Profundidade Iterativa", "Busca em Custo Uniforme", "A*"], key="-ALGORITMO-", size=(20, 1), font=("Inter", 10), pad=(5, 5), background_color="#FFFFFF"),
        
        sg.Checkbox("Aleatório", key="-ALEATORIO-", font=("Inter", 10), text_color=TEXT_COLOR, background_color=BACKGROUND_COLOR, pad=(5, 5))
    ],

    [
        sg.Button("Buscar", **button_style),
        sg.Button("Resumo", font=("Inter", 10, "bold"), button_color=(TEXT_COLOR, "#008B8B"), border_width=1, size=(12, 1), pad=(5, 10)),
        sg.Button("Rearranjar", font=("Inter", 10, "bold"), button_color=(TEXT_COLOR, "#64B5F6"), border_width=1, size=(12, 1), pad=(5, 10)),
        sg.Button("Reset", font=("Inter", 10, "bold"), button_color=(TEXT_COLOR, "#FF0000"), border_width=1, size=(12, 1), pad=(5, 10))
    ],

    [sg.Text("", size=(1, 1), background_color=BACKGROUND_COLOR)]
]

window = sg.Window("Semáforos Inteligentes - Maputo", layout, resizable=True, finalize=True, background_color=BACKGROUND_COLOR)

window["-CANVAS-"].expand(True, True)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Buscar":
        sg.popup("Busca iniciada com parâmetros:", values)
    elif event == "Resumo":
        sg.popup("Mostrando resumo dos dados.")
    elif event == "Rearranjar":
        sg.popup("Rearranjando mapa.")
    elif event == "Reset":
        sg.popup("Resetando parâmetros.")
        for key in ["-ORIGEM-", "-DESTINO-", "-ALEATORIO-", "-ALGORITMO-"]:
            window[key].update("") 

window.close()
