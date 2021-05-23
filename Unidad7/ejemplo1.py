def promedio(*muestras):
    """Calcula el promedio de los valores que introudzcas """
    promedio = sum(muestras)/len(muestras)
    print(f'El promedio es: {promedio}')
promedio(1,3,4,5,6)
