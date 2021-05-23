nombre = str(input("Escribe tu numbre: "))
edad = int(input("Escribe tu edad: "))
direccion = str(input("Escribe tu direccion: "))
telefono = int(input("Escribe tu telefono: "))

dic = {'nombre_usuario':nombre, 'edad_usuario':edad, 'direccion_usuario':direccion,'telefono_usuario':telefono}


print(dic['nombre_usuario'],"tiene ", dic['edad_usuario'], "años, vive en ", dic['direccion_usuario'], "y su número de teléfono es ", dic['telefono_usuario'],".")
