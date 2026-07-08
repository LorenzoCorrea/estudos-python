gameName = input("Digite o nome do jogo \n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0

while(rating != -1):
  rating = float(input("Informe a nota do jogo: \n"))
  if(rating != -1):
    totalRating += rating  ###Pegue o total atual e some com a nova nota
    qtdRating += 1 ###Adiciona 1 à contagem de pessoas que votaram.
    average = totalRating / qtdRating ###Calcula a média.
 
print(f"A média das avaliações do jogo {gameName} é {average:.2f}")