idade = int(input("Informe a idade: "))
cnh = int(input("Possui cnh? Informe quantidade: "))

if(idade < 18 and cnh == 1):
    print("Como você tem menos de 18 anos e pode dirigir? Alô, Polícia!!!")
elif(idade < 18 and cnh == 0):
    print("Você ainda não pode dirigir.")

elif(idade > 18 and cnh == 0):
    print("Você pode tirar a CNH e dirigir.")

elif(idade > 18 and cnh == 1):
    print("Você pode dirigir. Dirija com segurança!!")
else:
    print("rapaz fale direito")


'''
anotações de inputs
17
1

22
0


'''