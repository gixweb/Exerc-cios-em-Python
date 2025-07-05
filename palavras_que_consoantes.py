palavra = input()
palavras = []
consoantes = []
vogais = "aeiouAEIOU"

while palavra != "fim":
    palavras.append(palavra)
    palavra = input()

for item in palavras:
    if(item[0] not in vogais):
        consoantes.append(item)
        print(item)
    else:
        continue
if consoantes == []:
    print("Nenhuma palavra digitada começa com consoante.")



'''
abacaxi
mesa
melão
uva
garrafa
fim

abacate
aipim
Uva
ingrid
Olhar
estou
fim
'''