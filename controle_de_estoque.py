'''
nome = input("informe o nome do produto: ")
quantidade = int(input("informe a quantidade do produto: "))
valor = float(input("informe o valor unitário do produto: "))

'''
valorTotalEstoque = 0
for i in range(4):
    nome = input("informe o nome do produto: ")
    quantidade = int(input("informe a quantidade do produto: "))
    valor = float(input("informe o valor unitário do produto: "))
    valorTotal = quantidade*valor
    valorTotalEstoque = valorTotal + valorTotalEstoque
    print(f"{nome} - {quantidade} unidades - R${valor:.2f} cada - Total: R${valorTotal:.2f}")
    i += 1
    if(i == 4):
        print(f"Valor total do estoque: R${valorTotalEstoque:.2f}")

'''
feijao
4
5.80
arroz parbolizado
3
4.47
macarrao
7
3.58
fuba
8 
2.97
'''