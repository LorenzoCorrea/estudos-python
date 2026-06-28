gamesSet = {"Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2"}

# - Não possibilita recuperar valores via fatiamento ou slice

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são a mesma coisa
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3 - aDICIONAR ITEM DE OUTRO SET
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item do set
gamesSet.remove(True)
gamesSet.remove(90.50)

print(gamesSet)
