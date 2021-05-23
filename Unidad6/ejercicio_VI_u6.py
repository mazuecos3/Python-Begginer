numero = int(input("Introduce un numero para averiguar su factorial: "))

resultado = 1
i = 1
    
while i <= numero:
        resultado = resultado * i
        i = i + 1
print(resultado)