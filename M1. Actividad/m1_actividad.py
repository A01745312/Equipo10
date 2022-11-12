"""
    Robot de limpieza reactivo
    Autores:
        Paula Sophia Santoyo Arteaga,
        Nadia Paola Ferro Gallegos
    Noviembre, 2022
"""
from mesa import Agent, Model
from mesa.space import SingleGrid
from mesa.time import SimultaneousActivation
import numpy as np


class AgenteAspiradora(Agent):
    """
    Representa a un agente que va a limpiar la celda
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class AgenteSuciedad(Agent):
    """
    Representa una celda sucia
    """
    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)
