# verifica quais os numeros primos de 1 a 1000 

lista = []
for i in range(1,1001):
    divisor = 0
    if i != 1:
        if i %1 == 0:
            divisor += 1

    if i != 2:
        if i %2  == 0:
            divisor += 1

    if i != 3:
        if i %3 == 0:
            divisor += 1

    if i%i == 0:
        divisor += 1


    if divisor == 2:
        lista.append(i)
        

    elif divisor > 2 :
        pass

print(lista)
    
