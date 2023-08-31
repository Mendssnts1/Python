from turtle import Turtle, Screen

class Plaqueta(Turtle):     # classe para criar a plaqueta
    def __init__(self):
        super().__init__()
        self.tela = Screen()
        self.shape('square')   
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.penup()
        self.tela.listen()
        self.acima = 'Up'
        self.abaixo = 'Down'



    def mover_acima(self):      # move a plaqueta para cima
        self.y  = self.ycor()
        if self.y < 230:             # Se a posição y da plaqueta for menor que 280 ele retorna o 
            self.sety(self.y + 20)       # o valor da função sety="mover para cima" + 20


    def mover_abaixo(self):
        self.y = self.ycor()
        if self.y > -230:                # mesma coisa da função acima a uinca diferença que 
            self.sety(self.y - 20)           # move para baixo


    def controle(self):
        self.goto(x= -380,y=0)
        self.tela.onkeypress(self.mover_acima,self.acima)
        self.tela.onkeypress(self.mover_abaixo,self.abaixo)



class Player2(Plaqueta):
    def __init__(self):
        super().__init__()
        self.x = self.xcor()
        self.acima = 'w'  
        self.abaixo = 's'

    def mover_acima(self):
        super().mover_acima()
        self.y = self.x

    def mover_abaixo(self):
        super().mover_abaixo()
        self.y = self.x

    def controle(self):
        super().controle()
        self.goto(x= 380,y= 0)

