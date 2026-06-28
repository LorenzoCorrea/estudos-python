gamesList = ["Miranha", "Zelda", "Red Dead 2", "Fifa 24", "Sonic"]

# 1 - Tamanho da lista
print(len(gamesList)) ###LEN conta o numero de itens da lista

# 2 - Recuperar um item da lista pelo indice
print(gamesList.index("Miranha")) ### No caso ele retornou em que lugar da fila ta o miranha, ou seja 0

# 3 - Adicionar item ao final da lista
gamesList.append("GTA V")
print(gamesList)

# 4 - Ordenar a lista em ordem alfabética
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra
gameReset = gamesList.copy()
gameReset.remove("GTA V")
print(gameReset)

# 6 - Remove todos os itens da lista
gamesList.clear
print(gamesList)