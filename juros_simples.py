capital = float(input("informe o capital: "))
taxa = float(input("informe a taxa: "))
tempo = int(input("informe o tempo: "))


taxaP = taxa/100
juros = capital * taxaP * tempo

print(f"O total alcançado é de R${juros:.2f} ao final dos {tempo} meses.")


'''
1500 
25
12
'''