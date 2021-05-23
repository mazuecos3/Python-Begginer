def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
      print(suma, '+')
 
  if num == suma:
    return True
  else:
    return False
 
num = int(input("introduzca un numero:"))
 
if NumeroPerfecto(num):
  print(f'{num} es un numero perfecto' )
else:
  print(f'{num} no es un numero perfecto' )