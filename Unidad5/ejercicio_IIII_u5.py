dni =  int(input("Inserte su numero de dni: "))

str = "TRWAGMYFPDXBNJZSQVHLCKE"

algoritmo = dni % 23
#print(algoritmo)
letra = str[algoritmo]
#print(str[algoritmo])
if letra in str[0:5]  :
    print ("Este DNI ingresara en la Aula 1")
elif letra in str[6:11] :
    print ("Este DNI ingresara en la Aula 2")
elif letra in str[12:17] :
    print ("Este DNI ingresara en la Aula 3")
elif letra in str[18:22] :
    print ("Este DNI ingresara en la Aula 4")        

   
