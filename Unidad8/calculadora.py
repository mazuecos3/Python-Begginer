 #!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""Ejemplo de script utilizado como módulo dentro de Python
 
Este módulo se puede usar como una calculadora básica
 
"""
 
__author__ = "Oscar"
__copyright__ = "Programación en Python"
__credits__ = ["Oscar Mazuecos"]
__license__ = "GPL"
__version__ = "0.1"
__email__ = "oscar3mmm@gmail.com"
__status__ = "Desrrollo"
 
def suma(a,b):
    """Función que realiza la suma de a + b"""
    print("el resultado de la suma es: ",a+b)
 
def resta(a,b):
    """Funcion que realiza la resta de a - b"""
    print("el resultado de la resta es: ",a-b)
 
def multiplica(a,b):
    """Función que realiza la miltiplicación de a * b"""
    print("el resultado de la multiplicación es: ",a*b)
 
def divide(a,b):
    """Función que realiza la división de a / b"""
    print("el resultado de la división es: ",a/b)
 
if __name__ == "__main__":
    print('Ejecutando como programa principal')
    suma(6,5)