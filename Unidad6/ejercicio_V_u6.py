import random
numero_elegido = int(input("Elige un numero entre el 1 y el 10: "))

contador = 0
numero_acertado = random.randint(1, 10)

while numero_elegido != numero_acertado:
    print('Vuelve a elegir numero hasta que aciertes ')
    contador = contador + 1
    numero_elegido = int(input("Elige un numero entre el 1 y el 10: "))
    print(f'Llevas un total de {contador} intentos')
print('Ha salido el numero ganador por eso ha salido de el bucle.')
print(f'Lo has conseguido en un total de  {contador} intentos')
