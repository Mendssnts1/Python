from cobra import Cobra
from comida import Comida
from turtle import Screen
from pontuação import Pontuaçao
from turtle import Turtle
import time


cobra = Cobra()


comida = Comida()
score = Pontuaçao()




tela = Screen()
tela.setup(width=600, height=600)  # widht='largura', height='altura'
tela.bgcolor("black")  # altera a cor de fundo para preto
tela.title("Meu jogo da Cobra!")
tela.tracer(0)
tela.listen()


def encerrar():     # função para ultilar quando aperto na tecla "c"
    global jogo_on
    jogo_on = False



jogo_on = True
colisao = 0
while jogo_on:
    tela.update()
    time.sleep(0.1)
    cobra.conjunto()

    score.atualizar_pontuaçao()

    tela.onkey(encerrar, "c")
    if jogo_on == False:        # encerra o jogo caso aperte na tecla "c"
        tela.bye()
        break

    for segmento in cobra.segmentos[1:]:            # verifica se a cabeça da cobra bateu no corpo!!

        if cobra.head.distance(segmento) < 10 :      # verifica a distância entre a cabeça e o segmento            
            colisao += 1

        if colisao == 2:                        # aqui eu fiz uma gambiarra, como sempre quando iniciava tava dando erro, eu armazenei dentro de uma variavel para quando atingisse o valor de 2
            score.reset()
            cobra.reset()
            colisao = 0
        

    if cobra.head.distance(comida) < 15:        # se a cobra comer a comida ira aumentar a pontuação e irar gerar outra comida em uma posição aleatoria!
        cobra.novo_corpo()
        comida.refazer()
        score.score += 1

    # detectar colissão na lateral!
    elif cobra.head.xcor() > 290 or cobra.head.xcor() < -290 or cobra.head.ycor() > 290 or cobra.head.ycor() < -290:
        score.reset()
        cobra.reset()
        colissao = 0
        print('Bateu nas bordas')






tela.mainloop()
