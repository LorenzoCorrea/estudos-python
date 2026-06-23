# Toda string pode ser gerada uma SUB STRING
###Fatiamento é feito em 2 partes [inicio:fim]
### string[inicio:fim]
#Indicice começa no 0 e acaba em -1
### string[0:-1]
gameName = "Fifa 23"
gameDescription = """
 Fifa 23 é um jogo de futebol  
 Desenvolvido pela EA
 Tem multiplataforma
"""



#1 - Busque toda a string a partir da primeira posição
print(gameName[0:])

#2 - Busque toda a string até a ultima posição
print(gameName[:7])

#3- Busque toda a string da terceira ate a ultima posição
print(gameName[2:])

#4- busque toda a string de 2 em 2 passos
print(gameName[::2]) ### Os segundo dois pontos seria o passo, de x em x, sempre começa no 1

# Inverta uma string de trás pra frente
print(gameName[::-1])

# Imprime os caracteres nos índices ímpares
print(gameName[1::2])