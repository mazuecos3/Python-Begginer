#Oscar Mazuecos Montoro - Interes dinero

euros =  float(input('Introduce la cantidad en Euros: '))
tasa =  float(input('Introduce la tasa de interes: '))
años =  float(input('Introduce el numero de años: '))

resultado = euros * (1 + tasa/100)**años

print(resultado)