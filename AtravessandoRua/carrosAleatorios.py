from turtle import Turtle
import random as ran




class Carro(Turtle):
    def __init__(self):
        super().__init__()
        self.cores = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        self.shape('square')
        self.color(ran.choice(self.cores))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(250, ran.randint(-280, 280))

        
    def mover(self):
        self.velocidade = ran.randint(1, 20)
        self.setheading(180)
        self.forward(self.velocidade)
        if self.xcor() < -100:
            self.goto(250, ran.randint(-280, 280))
            