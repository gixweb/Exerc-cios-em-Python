num_Alunos = int(input("indique o número de alunos: "))
#nome_aluno = input("Informe o nome do aluno: ")
#nota_aluno = input("Informe a nota do aluno: ")

alunos_reprovados = []

def alunos_abaixo_da_media(nota, nome):
    if(nota < 7):
        alunos_reprovados.append(nome)
        return alunos_reprovados

for i in range(num_Alunos):
    nome_aluno = input("Informe o nome do aluno: ")
    nota_aluno = float(input("Informe a nota do aluno: "))
    alunos_abaixo_da_media(nota_aluno, nome_aluno)

print(f"Os alunos que foram reprovados foram: {alunos_reprovados}")

'''
2
Ana
4
Josue
8

4
Ana
7
Karla
5
João
8.5
Marcondes
7.0

'''