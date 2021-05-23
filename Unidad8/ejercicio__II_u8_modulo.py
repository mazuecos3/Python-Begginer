import random 
# Funcion verificar cantidad
def verificacion(cantidad):
    if cantidad < 100:
        print("Lo sentimos no podemos aplicar ninguna promocion.")
    else:
         return cantidad   
# Funcion aplicar descuento en base a el color de la pelota que se elige de manera random
def promocion(cantidad):
    lista_bolas = ['BLANCA','ROJA','AZUL','VERDE','AMARILLA']
    bola_random = random.choice(lista_bolas)
    #print(bola_random)
    precio_final = cantidad
    if bola_random == 'BLANCA':
        print("No tiene descuento")
    elif bola_random == 'ROJA':
        print("Descuento de el 10%")
        precio_final -=  precio_final * 0.10 
    elif bola_random == 'AZUL':
        print("Descuento de el 20%")
        precio_final -=  precio_final * 0.20    
    elif bola_random == 'VERDE':
        print("Descuento de el 25%")
        precio_final -=  precio_final * 0.25    
    elif bola_random == 'AMARILLA':
        print("Descuento de el 50%")        
        precio_final -=  precio_final * 0.50 
    #print(precio_final)                  
    return precio_final       