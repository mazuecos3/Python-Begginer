numero = int(input('Introduce un numero mayor que 1 para calcular su tabla de multiplicar correspondiente. '))

for i in range(1,11):

    resultado = numero * i
    print(numero, ' x ', i, ' es igual a:', resultado)