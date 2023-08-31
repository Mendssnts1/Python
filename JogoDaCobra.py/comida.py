import random
from turtle import Turtle

class Comida(Turtle):           # a classe comida está herdando a classe Turtle
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.refazer()

    def refazer(self):
        random_x = random.randint(-280,280)
        randon_y = random.randint(-280, 280)
        self.goto(random_x, randon_y)
