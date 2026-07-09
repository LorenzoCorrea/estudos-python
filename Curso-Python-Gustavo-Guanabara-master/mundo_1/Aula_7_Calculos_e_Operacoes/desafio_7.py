# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input("Digite a nota do primeiro trimestre: "))
n2 = float(input("Digite a nota do segundo trimestre: "))
n3 = float(input("Digite a nota do terceiro trimestre: "))

nota = n1 + n2 + n3 
media = nota / 3

print(f"A nota final foi: {media}")