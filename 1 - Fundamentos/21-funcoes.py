# 1 - Função para imprimir
def wellcom():
  print("Hello World")

wellcom()

# 2 - Função para somar
def sum():
 # print(5 + 4)
  return 5 + 4

print(sum())


# 3 - Função para cadastrar um jogo
def create_game():
  name = input("Digite o nome do jogo: \n ") 
  yearLaunch = int(input("Digite o ano do jogo: \n ")) 
  gamePrice = float(input("Digite o preço do jogo: \n"))
  noteRating = float(input("digite a nota do jogo? \n"))

  print(f"{name} - R$ {gamePrice}")

create_game()
create_game()
