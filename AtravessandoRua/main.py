# inicio do codigo
from turtle import Turtle, Screen
from carrosAleatorios import Carro
from jogador import Player
from placar import Placar
import time

tela = Screen()
tela.setup(600, 600)
tela.bgcolor("white")
tela.tracer(0)

# criação do jogador
play = Player()

# placar do jogo
placar = Placar()


# criação de carros
carros = []
quantidade = 10

for i in range(quantidade):
    carro = Carro()
    carros.append(carro)

velocidade = 0.1
level = 1
game_on = True
while game_on:
    tela.update()
    time.sleep(velocidade)

    placar.atualiza_placar(level)

    for i in range(len(carros)):
        carro = carros[i]  # aqui cria os varios carros
        carro.mover()

        if play.distance(carros[i]) < 20:       # verifica se a tartaruga bateu no carro
            placar.game_over()
            game_on = False

        for j in range(i + 1, len(carros)):  # verifica a partir do proximo carro os outro do mesmo
            outro_carro = carros[j]

            if carro.distance(outro_carro) < 25:        
                novo_y = outro_carro.ycor() + 30
                carro.sety(novo_y)


    if play.ycor() > 280:
            play.atualiza_pos()
            level += 1
            velocidade -= 0.00100
            print(velocidade)
     

tela.exitonclick()
            
