'''

Exercicio 1:

Calculo de distancia:
-> Escreva um programa que pergunte a distância que um passageiro
  deseja percorrer em km

  Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
  E R$0,35 para viagens mais longas.

'''

  # distancia = float(input("Qual a distancia que deseja percorrer: \n"))
  # if distancia <= 200:
  #     preco = distancia * 0.50
  # else: 
  #    preco = distancia * 0.35

  # print(f"O valor da passagem é de R${preco}")




# Exercicio 2:
# Aumento de salário do funcionário:
# -> Escreva um programa que pergunte o salário de um funcionario
# e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%
# Para inferiores ou iguais, de 15%


salario = float(input("Digite seu salário: \n"))

if salario > 1250.00: 
  aumento = salario * 0.10
else:
   aumento = salario * 0.15

print(f"O valor do aumento é de R${aumento}")