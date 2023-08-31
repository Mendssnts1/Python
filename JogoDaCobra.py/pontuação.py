from turtle import Turtle

class Pontuaçao(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.maior_score = 0
        self.hideturtle()
        self.color('white')

    def atualizar_pontuaçao(self):
        self.penup()
        self.goto(0,250)
        self.clear()    
        # toda vez que atualizar o placar a função vai ler o conteudo armazenado dentro do arquivo de texto 
        self.conteudo = self.ler_arquivo()
        self.write(f'Pontuação: {self.score} Maior pontuação: {self.conteudo}', align='center', font=('Courier', 20, 'normal'))     # que aqui imprime
        

    def reset(self):
        if self.score > self.maior_score:
            self.maior_score = self.score           
            print(self.maior_score)                     #
            print(self.conteudo)                            # se a variavel score for maior que a variavel "maior_score" ela armazena no arquivo de texto o mesmo
            self.armazena_maior()                       #


        self.score = 0     # aqui transforma o valor novamente em zero
        self.atualizar_pontuaçao()
  

    def armazena_maior(self):
        with open('Projetos.py/JogoDaCobra.py/Maior_numero.txt', 'w') as file:     # aqui no começo eu criei um arquivo nas diretrizes mencionadas
            file.write(str(self.maior_score))                                      # aqui armazenei no arquivo o maior numero

    def ler_arquivo(self):
        with open('Projetos.py/JogoDaCobra.py/Maior_numero.txt') as file:
            conteudo = file.read()                                                  # aqui é uma função que retorna o valor armazenado de dentro do arquivo de texto
            return conteudo

            

