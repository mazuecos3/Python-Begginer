
cantidadkw = float(input("Inserte el valor que ha consumido en Kw: "))
kw = 0.135

gasto = cantidadkw * kw
consumo_extra = 0
gasto_extra = consumo_extra * (kw + kw * 0.05)

if cantidadkw > 700:
    print(gasto + gasto_extra)
else: 
    print(gasto)    