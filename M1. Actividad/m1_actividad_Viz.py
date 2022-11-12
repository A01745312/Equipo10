"""
    Vizualizador del robot de limpieza reactivo
    Autores:
        Paula Sophia Santoyo Arteaga,
        Nadia Paola Ferro Gallegos
    Noviembre, 2022
"""
from m1_actividad import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "black",
                 "r": 0.5}

    if agent.live == 1: #Rojos grandes cuando están vivos
        portrayal["Color"] = "black"
        portrayal["Layer"] = 0
    elif agent.live == 3 :
            portrayal["Color"] = "blue"
            portrayal["Layer"] = 1

    return portrayal
ancho = 28
alto = 28
grid = CanvasGrid(agent_portrayal, ancho, alto, 750, 750)
server = ModularServer(ModeloLimpieza,
                       [grid],
                       "Modelo limpieza",
                       {"width":ancho, "height":alto})
server.port = 8521 
server.launch()