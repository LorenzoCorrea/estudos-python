# Módulo de strings
# Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

# Inverter uma string de trás pra frente.
# Retornar apenas letras com índice par.
# Retornar apenas letras com índice ímpar




import strings

name = input("Digite uma frase: \n")

print(strings.inverse(name))
print(strings.even_char(name))
print(strings.odd_char(name))