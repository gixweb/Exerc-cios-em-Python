nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))

def distancia (nota):
    resultado = 5 - nota
    return resultado

def media (AV1, AV2):
    resultado = (AV1 + AV2)/2
    return resultado


print(distancia(nota1))
print(distancia(nota2))
print(media(nota1, nota2))
print(distancia(media(nota1, nota2)))

'''
1
3
'''