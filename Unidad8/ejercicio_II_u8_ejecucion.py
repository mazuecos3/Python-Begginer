import ejercicio__II_u8_modulo
# Pedimos al usuario el precio total de compras
compras = float(input("Ingrese  el total de compras: "))

# Comprobamos la verificacion y en caso de que sea correcto ejecutamos la promocion
# En caso contrario, le avisamos de que tiene que llegar a cierta cantidad.

if ejercicio__II_u8_modulo.verificacion(compras):
    print(ejercicio__II_u8_modulo.promocion(compras))
else: print("Compra mas cantidad para llegar a los 100€ Si quieres que podamos aplicar una promocion, gracias.")    