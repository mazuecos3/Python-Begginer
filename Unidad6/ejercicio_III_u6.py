import random

contador = 0
x=random.randint(1, 6)
while x != 6:
    print('Vuelve a lanzar el dado hasta que aparezca 6')
    x=random.randint(1, 6)
    contador = contador + 1
print('Ha salido el 6 por eso ha salido de el bucle.')
print(contador)

