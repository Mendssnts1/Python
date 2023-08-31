from Plaqueta import Plaqueta, Player2
from score import Placar
from turtle import Turtle, Screen
from Bola import Bola
import time


bola = Turtle(shape="circle")
traço = Turtle()
tela = Screen()
tela.title('Pong')
tela.bgcolor("black")
tela.setup(width=800, height=600)    # widht='largura', height='altura'
tela.tracer(0)

score = Placar()

# plaqueta jogador
plaqueta = Plaqueta()
plaqueta.controle()

player2 = Player2()
player2.controle()


# bola

bola = Bola()
bola.move_mais()


traço.goto(0, -280)
traço.speed(0)

def para():         # função que irei utilizar para encerrar game
    global game_on
    game_on = False


game_on = True
bola.move_mais()


play1 = 0
play2 = 0
velocidade = 0.0010

#while True:
while game_on:

    tela.update()
    time.sleep(velocidade)

    bola.move_mais()
    score.resultado_atualizado(play1, play2)


    tela.onkey(para,'c')
    if not game_on:
        score.encerra()

    # detecta colisão na lateral de cima e de baixo
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.move_y()

    # detectar a colisão da bola com o player 1 e o player 2
    if bola.distance(player2) < 30 and bola.xcor() > 320 or bola.distance(plaqueta) < 30 and bola.xcor() < -320:
        print('contato')
        bola.move_x()
        velocidade -= 0.0010
        print(velocidade)

        
    if bola.xcor() > 400:           # verifica se saiu da tela do jogo!
            play1 += 1
            velocidade = 0.1
            bola.resetar()
        
    if bola.xcor() < -400:         # verifica a mesma coisa que o codigo de cima!
        play2 += 1
        velocidade = 0.1
        bola.resetar()
    

    

tela.exitonclick()
