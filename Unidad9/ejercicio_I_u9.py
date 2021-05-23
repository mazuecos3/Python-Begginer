class Triangulo:

# Creamos la clase, primero sus atributos   
    def __init__(self):
        self.a = int(input('Lado 1 del triangulo: '))
        self.b = int(input('Lado 2 del triangulo: '))
        self.c = int(input('Lado 3 del triangulo: '))
        self.tipo = str(input('Tipo de triangulo '))
           

# Los imprimipos           
    def imprimr(self):
        return self.a,self.b,self.c,self.tipo
# Establecemos los metodos, en este caso la formula para calcular el area del triangulo no rectangulo    
    def area(self):
        self.semi_perimetro = (self.a + self.b + self.c) / 2
        self.area = ( self.semi_perimetro*(self.semi_perimetro- self.a) * (self.semi_perimetro- self.b) * (self.semi_perimetro- self.c)) **0.5
        return self.area       

# Instanciamos la clase
triangulo = Triangulo()

# Llamamos a esas funciones desde la isntancia.
print(triangulo.imprimr())
print(triangulo.area()) 