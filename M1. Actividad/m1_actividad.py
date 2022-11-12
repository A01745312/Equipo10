"""
    Robot de limpieza reactivo
    Autores:
        Paula Sophia Santoyo Arteaga,
        Nadia Paola Ferro Gallegos
    Noviembre, 2022
"""
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import SimultaneousActivation
import numpy as np


class AgenteAspiradora(Agent):
    """
    Representa a un agente que va a limpiar la celda
    """


    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.live = 3
        self.next_state = None
        self.pos = pos


    def avanzar(self):
        l = []
        siguienteMovimiento = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center = True)
        neighbors = self.model.grid.get_neighbors(self.pos,
                                                moore=True,
                                                include_center = True)
        for n in neighbors:
            if n.live == 1 and n.pos == self.pos:
                n.live = 0
            if n.live == 1:
                l.append(n.pos)
        if len(l) == 0:
            posicion = self.random.choice(siguienteMovimiento)
            self.model.grid.move_agent(posicion)
        else:
            posicion = self.random.choice(l)
            self.model.grid.move_agent(posicion)
    
    


class AgenteSuciedad(Agent):
    """
    Representa una celda sucia
    """


    def __init__(self, unique_id: int, model: Model, pos) -> None:
        super().__init__(unique_id, model)
        self.live = np.random.choice([0,1])
        self.next_state = None
        self.pos = pos

class ModeloLimpieza(Model):
    '''
    Define el modelo de simulador de limpieza
    '''
    def __init__(self, width, height):
        self.num_agents = width * height
        self.grid = MultiGrid(width, height, True)
        self.schedule = SimultaneousActivation(self)
        self.running = True 

        for (content, x, y) in self.grid.coord_iter():
            if x == 1 and y == 1:
                comienza = AgenteAspiradora(("A", 1, 1), self, (1,1))
                self.grid.place_agent(comienza,(1,1))
                self.schedule.add(comienza)
            
            dirty = AgenteSuciedad(("S", x, y), self, (x,y))
            self.grid.place_agent(dirty,(x, y))
            self.schedule.add(dirty)
    
    def step(self):
        self.schedule.step()

