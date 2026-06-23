"""
Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, 
utilizando operadores de atribuição.
"""

###Escreva um programa em Python que leia quatro números e calcule a média entre esses números


# #Exercicio 1
# num1 = int(input("Digite o número: \n"))

# print(f"O antecessor de: {num1 - 1} | Sucessor do número: {num1 +1}")


#Exercicio 2

num1 = float(input("Digite a primeira nota: \n"))
num2 = float(input("Digite a segunda nota: \n"))
num3 = float(input("Digite a terceira nota: \n"))
num4 = float(input("Digite a quarta nota: \n"))

media = (num1 + num2 + num3 + num4) / 4

print(f"A media do aluno foi de {media} pontos \n")