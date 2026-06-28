gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.40]

# 1- interando valores da lista
for game in gamesList:
  print(game)

# 2 - Quando a condição for atendida, o loop será encerrado
for game in gamesList:
  if game == "Red Dead 2":
    break
  print(game)

# 3 - Quando a condição for atendida, o loop vai pra próxima iteração
for game in gamesList:
  if game == "Red Dead 2":
    continue
    print(game)

# 4 - Avaliação
gameName = input("Digite o nome do jogo: \n")
gameRating = int(input("Digite quantas avalições deseja fazer no jogo: \n"))

sum = 0
for i in range(gameRating):
  note = float(input("Digite a nota para o jogo: \n"))
  sum += note

  print(f"Media de avaliaçãoes do jogo {gameName} é {gameRating}")