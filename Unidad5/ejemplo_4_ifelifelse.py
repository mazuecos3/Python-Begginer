#Calcular precio de un kebab
 
tamaño=int(input('Tamaño del kebab: '))
n=int(input('Número de ingredientes extra: '))
if   tamaño == 1:
      pagar = 3 + 0.5 * n
elif tamaño == 2:
      pagar = 5 + 0.5 * n
elif tamaño == 3:
      pagar = 9 + 0.5 * n
else:
      pagar = 0
print(f'Debes pagar: {pagar}€')