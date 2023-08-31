from turtle import Turtle
import random
import math


class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shapesize(1)
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10        

        

    def move_mais(self):
        novo_x = self.xcor() + self.x_move 
        novo_y = self.ycor() + self.y_move 
        self.goto(novo_x,novo_y)         


    def move_y(self):
        self.y_move *= -1
        
    def move_x(self):
        self.x_move *= -1

    def resetar(self):
        self.clear()
        self.goto(0,0)
        self.move_x()
        


        #if self.ycor() > 280: self.ycor() < -280:
           #self.move_menos()
        

