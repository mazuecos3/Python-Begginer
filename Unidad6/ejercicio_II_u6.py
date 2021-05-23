numero1 = int(input('Introduce el primer numero para establecer un rango: '))
numero2 = int(input('Introduce el segundo numero para establecer un rango: '))
numeros_pares = 0

for i in range(numero1,numero2):
    if i % 2 == 0:
        numeros_pares = numeros_pares + 1
     
       

print(numeros_pares)    