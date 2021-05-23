numeros = [
              [56, 13, 93, 45, 18],
              [59, 83, 16, 75, 43],
              [49, 59, 93, 83, 62],
              [41, 72, 56, 10, 87]
           ]
# Lmada function (less code)

medias = list(map(lambda numeros: sum(numeros) / len(numeros), numeros))
print(medias)           