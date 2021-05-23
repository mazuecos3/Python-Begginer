 
p = float(input("Inserte su peso en KG: "))
t = float(input("Inserte su talla en METROS: "))

imc = p / t**2
 
if imc >= 0 and imc < 18.5 :
    print ("Desnutrido")
elif imc >= 18.5 and imc <= 25.5 :
    print ("Peso optimo")
elif imc >= 25.5:
    print ("Sobrepeso")
   