from turtle import Turtle

class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-240, 250)

    def atualiza_placar(self, valor):
        self.clear()
        self.write(f'level :{valor}',align='center', font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER' ,align='center', font=('Verdana', 25, 'normal'))