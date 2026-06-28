# 1 - Crie uma função que receba 2 argumentos, primeiro e segundo nome

def full_name(fname, lname):
  print(f"Nome Completo: {fname}{lname}")

full_name("Lorenzo", "Correa")

# 2 - Crie uma função que some dois numeros via parametros

def sum(a, b):
  return a + b

print(sum(10,50))



# 3 - Argumentos default de uma funlçai

def adress(country="Brasil"):
  print(f"Eu moro no {country}")

adress()
adress("Canadá")

# 4 - Avaliação do jogo

def rating_game(qtdRating):
  game_name = inout("Digite o nome do jogo: ")
  sum = 0
  for i in range (qtdRating):
    note = float(input("Digite a nota do jogo"))
    sum += note
    print(f"A média de avaliações {game_name} é {sum / qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo"))
rating_game(rating)