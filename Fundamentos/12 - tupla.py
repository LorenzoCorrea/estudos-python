
gamesTuple = ("Fifa 23", "Red dead 2", "Miranha",
               "Mario Odyssey", "Legend of Zelda")

print(gamesTuple)
# name = ("cho")
# print(type(name))###Type verifica o tipo da string
print(type(gamesTuple)) ###Type verifica o tipo da string

#Tupla não possibilida adicionar, remover e ordenar valores na tupla
#O que fazemos com uma tupla? Buscamos informações em um slice
###Ex:

# 1- Buscar os dois primeiros itens da Tupla
print(gamesTuple[:2])

# 2- Buscar o ultimo item da lista
print(gamesTuple[-1])

# 3 - buscar jogos até uma determinada posição
print(gamesTuple[:3])


# 4- buscar jogos de uma posição em diante
print(gamesTuple[2:])


# 5 - Recuperar um item da tupla pelo indice
print(gamesTuple.index("Fifa23"))