from turtle import Turtle, Screen

inicio_pos = (0, -280)
move_distancia = 10
linha_de_chegada = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.tela = Screen()
        self.shape('turtle')
        self.shapesize(1)
        self.setheading(90)
        self.penup()
        self.atualiza_pos()
        self.tela.listen()
        self.tela.onkeypress(self.avança, 'Up')
        self.tela.onkeypress(self.abaixa, 'Down')

    def avança(self):
        self.setheading(90)
        self.forward(10)

    def abaixa(self):
        self.setheading(270)
        self.forward(10)

    def atualiza_pos(self):
        self.goto(inicio_pos)