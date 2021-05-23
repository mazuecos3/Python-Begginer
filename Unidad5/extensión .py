# Cálculo de calificación final
 
nota1=int(input('Cual es la nota de tu primer examen: '))
nota2=int(input('Cual es la nota de tu segundo examen: '))
nota3=int(input('Cual es la nota de tu tercer examen: '))
if   nota1 >= nota3 and nota2 >= nota3:# aquí añadimos 2 comparaciones que concatenadas con and obliga a que las dos sean verdaderas para que if sea verdad
    t = nota1 + nota2
else:
    if nota1 >= nota2 and nota3 >= nota2:
        t = nota1 + nota3
    else:
        t = nota2 + nota3
print(f'Su calificación total es: {t}')