from turtle import Turtle,Screen
tela = Screen()

class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 180)
        self.color('white')
        self.hideturtle()
        self.maior = 0

    def resultado_atualizado(self, play1, play2):
        self.clear()
        self.write(f'{play1} x {play2}',align='center', font=('Arial', 80, 'bold') )
        
        if play1 > play2:
            self.maior = f'O vencedor é o play1 com {play1} pontos'
            
        elif play2 > play1:
            self.maior =  f'O vencedor é o play2 com {play2} pontos'

        elif play1 == play2:
            self.maior = 'Deu empate!'

    def encerra(self):
        self.clear()
        self.goto(0,0)
        self.write(f'{self.maior}', align='center', font=('Arial', 22, 'bold'))
