total_compra = float(input("Cuanto ha gastado el cliente: "))
importe_a_pagar = total_compra
if total_compra > 100:
    tasa_descuento = 15
    importe_descuento = total_compra * tasa_descuento / 100
    importe_a_pagar = total_compra - importe_descuento
    print(F'como has sobrepasado el gasto común recibes un descuento del 15%, así que de {total_compra}, has pagado {importe_a_pagar}') 
else:
    diferencia = 100 - total_compra
    print(F'Como no has llegado a la cantidad mínima de 100€ no se te aplica descuento, si gastases {diferencia}€ más si te haríamos el descuento del 15%')        
