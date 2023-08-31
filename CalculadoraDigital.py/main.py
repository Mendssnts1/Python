from tkinter import *

calculation = ''

def adcionar_a_calculadora(simbolos):
    global calculation
    calculation += str(simbolos)

    # vai apagar as formulas de calculo
    text_result.delete(1.0, 'end')
    # vai imprimir na tela o resultado do calculo
    text_result.insert(1.0, calculation)

def fazer_calculos():
    global calculation
    try:
        resultado = str(eval(calculation))
        calculation = ''
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, resultado)

    except:
        limpa_campo()
        text_result.insert(1.0, 'Error')
        pass

def limpa_campo():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')
    

# criar Janela
root = Tk()
root.title('My Calculadora')
root.geometry('300x275')

text_result = Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)


# criação de botões para a calculadora
btn_1 = Button(root, text='1', command=lambda: adcionar_a_calculadora(1), width=5, font=('Arial', 14 ))
btn_1.grid(row=2, column=1)

btn_2 = Button(root, text='2', command=lambda: adcionar_a_calculadora(2), width=5, font=('Arial', 14 ))
btn_2.grid(row=2, column=2)

btn_3 = Button(root, text='3', command=lambda: adcionar_a_calculadora(3), width=5, font=('Arial', 14 ))
btn_3.grid(row=2, column=3)

btn_4 = Button(root, text='4', command=lambda: adcionar_a_calculadora(4), width=5, font=('Arial', 14 ))
btn_4.grid(row=3, column=1)

btn_5 = Button(root, text='5', command=lambda: adcionar_a_calculadora(5), width=5, font=('Arial', 14 ))
btn_5.grid(row=3, column=2)

btn_6 = Button(root, text='6', command=lambda: adcionar_a_calculadora(6), width=5, font=('Arial', 14 ))
btn_6.grid(row=3, column=3)

btn_7 = Button(root, text='5', command=lambda: adcionar_a_calculadora(7), width=5, font=('Arial', 14 ))
btn_7.grid(row=4, column=1)

btn_8 = Button(root, text='8', command=lambda: adcionar_a_calculadora(8), width=5, font=('Arial', 14 ))
btn_8.grid(row=4, column=2)

btn_9 = Button(root, text='9', command=lambda: adcionar_a_calculadora(9), width=5, font=('Arial', 14 ))
btn_9.grid(row=4, column=3)

btn_0 = Button(root, text='0', command=lambda: adcionar_a_calculadora(0), width=5, font=('Arial', 14 ))
btn_0.grid(row=5, column=2 )

btn_mais = Button(root, text='+', command=lambda: adcionar_a_calculadora('+'), width=5, font=('Arial', 14 ))
btn_mais.grid(row=2, column=4)

btn_menos = Button(root, text='-', command=lambda: adcionar_a_calculadora('-'), width=5, font=('Arial', 14 ))
btn_menos.grid(row=3, column=4)

btn_mult = Button(root, text='*', command=lambda: adcionar_a_calculadora('*'), width=5, font=('Arial', 14 ))
btn_mult.grid(row=4, column=4)

btn_div = Button(root, text='/', command=lambda: adcionar_a_calculadora('/'), width=5, font=('Arial', 14 ))
btn_div.grid(row=5, column=4)

btn_open = Button(root, text='(', command=lambda: adcionar_a_calculadora('('), width=5, font=('Arial', 14 ))
btn_open.grid(row=5, column=1)

btn_close = Button(root, text=')', command=lambda: adcionar_a_calculadora(')'), width=5, font=('Arial', 14 ))
btn_close.grid(row=5, column=3)

btn_igual = Button(root, text='=', command=fazer_calculos, width=12, font=('Arial', 14 ))
btn_igual.grid(row=6, column=1, columnspan=2)

btn_clear = Button(root, text='c', command=limpa_campo, width=12, font=('Arial', 14 ))
btn_clear.grid(row=6, column=3, columnspan=2)


root.mainloop()