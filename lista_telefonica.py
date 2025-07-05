lista_telefonica = {}
linha = input("me diga o nome da pessoa: ")

def adicionar_lista (nome, numero):
    nome.lower()
    lista_telefonica[nome] = numero

while True:
    if(linha == "fim"):
        break
    else:
        num = input("me diga o número da pessoa: ")
        adicionar_lista(linha, num)
        linha = input("me diga o nome da pessoa: ")
       

pergunta = input("pra quem você quer discar? ")

if pergunta in lista_telefonica:
    print(lista_telefonica[pergunta])
else:
    print("Essa pessoa não está na lista telefônica")

'''
Ana 1248
Fabricio 1874
Leonardo 2525
fim

vanessa 8745
André 8989
Carlos 5847
João 178444
pedro 6487
fim

lucas 7848
emilly 4857
francisco 3648
gabriel 7485
Matheus 147155
fim
'''