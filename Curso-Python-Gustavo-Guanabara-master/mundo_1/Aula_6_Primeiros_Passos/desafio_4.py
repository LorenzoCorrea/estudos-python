# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

algo = str(input("Digite uma plavra: "))
print(f"O tipo primitivo desse valor é: {type(algo)}")
print(f"Só tem espaços? {algo.isspace()}")
print(f"É um número? {algo.isnumeric()}")
print(f"É alfabético (só letras)? {algo.isalpha()}")
print(f"É alfanumérico (letras e/ou números)? {algo.isalnum()}")
print(f"Está tudo em maiúsculas? {algo.isupper()}")
print(f"Está tudo em minúsculas? {algo.islower()}")
print(f"Está capitalizada (1ª letra maiúscula)? {algo.istitle()}")