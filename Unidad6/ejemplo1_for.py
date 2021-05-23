número = int(input('¿De que número quieres saber su tabla de multiplicar? '))
for i in range(1,11):
    resultado = número * i
    print(número, ' x ', i, ' es igual a:', resultado)