from turtle import Turtle, Screen

cima = 90
baixo = 270
direita = 0
esquerda = 180



class Cobra(Turtle):
    def __init__(self):
        super().__init__()
        self.segmentos = []
        self.posicao = 0
        self.tela = Screen()
        self.tela.listen()
        self.corpos()                       # chamei o metodo corpo para não dar erro de indice
        self.head = self.segmentos[0]       # cabeça da cobra!

    def corpos(self):
        for i in range(3):
            self.new_cobra = Turtle(shape='square')   # cria instâncias da cobra
            self.new_cobra.penup()
            self.new_cobra.color('white')   # cor da cobra
            self.new_cobra.goto(0,self.posicao)     # posiaçao das primeiras peças que conpõem o corpo da cobra
            self.posicao += 20
            self.segmentos.append(self.new_cobra)   # adciona as instâncias na lista de segmentos

    def para_cima(self):
        if self.head.heading() != baixo:      # se a cabeça da cobra esta indo numa direção diferente que o valor da variavel baixo
            self.head.setheading(cima)

    def para_baixo(self):
        if self.head.heading() != cima:
            self.head.setheading(baixo)

    def para_direita(self):
        if self.head.heading() != esquerda:
            self.head.setheading(direita)

    def para_esquerda(self):
        if self.head.heading() != direita:
            self.head.setheading(esquerda )
            


    def conjunto(self):

        for seg_num in range(len(self.segmentos) -1 , 0, -1):      # loop que ira conectar o corpo da cobra
            novo_x = self.segmentos[seg_num - 1].xcor()
            novo_y = self.segmentos[seg_num - 1].ycor()
            self.segmentos[seg_num].goto(novo_x, novo_y)

        self.head.forward(20)

        self.tela.onkey(self.para_cima,'Up')
        self.tela.onkey(self.para_baixo,'Down')
        self.tela.onkey(self.para_direita, 'Right')
        self.tela.onkey(self.para_esquerda, 'Left')
        

    def reset(self):
        for seg in self.segmentos:
            seg.goto(1000, 1000)

        self.segmentos.clear()
        self.posicao = 0
        self.corpos()
        self.head = self.segmentos[0]
    
    
    def novo_corpo(self):
        for i in range(1):
            self.new_cobra = Turtle(shape='square')   # cria instâncias da cobra
            self.new_cobra.penup()
            self.new_cobra.color('white')   # cor da cobra
            self.new_cobra.goto(self.posicao,0)     # posiaçao das primeiras peças que conpõem o corpo da cobra
            self.posicao += 20
            self.segmentos.append(self.new_cobra)   # adciona as instâncias na lista de segmentos

