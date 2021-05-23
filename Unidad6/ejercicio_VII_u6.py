nombres = ["Sheldon Cooper", "Leonard Hofstadter", "Howard Wolowitz", "Rajesh Koothrappali"]

incrementador = 0
for i in list(nombres):

    
    nombres[incrementador] = nombres[incrementador].lower()
    print(nombres[incrementador].replace(" ", "_"))
    incrementador = incrementador + 1


