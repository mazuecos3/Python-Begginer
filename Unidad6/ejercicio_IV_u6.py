numero = int(input('Introduce un numero entero de el 0 al 9 '))

lista = [1, 3, 9]

while numero not in lista:
    print("Numero ",  numero ," no aparece en la lista prueba otro")
    numero = int(input('Introduce un numero entero de el 0 al 9 '))

print("Numero ", numero, "correcto, si esta en la lista")