name = input("Digite o nome do jogo: \n ") # Sempre que tiver um "\n" é uma quebra de linha
yearLaunch = int(input("Digite o ano do jogo: \n "))
gamePrice = float(input("Digite o preço do jogo: \n"))
planIncluided = bool(input("Eatá incluso na gamepass? \n"))


#Alternativa 1
# print("###Dados do Jogo #####")
# print("================")
# print("Nome do jogo:", name)
# print("Ano do jogo:", yearLaunch)
# print("Preço do jogo:", gamePrice)
# print("Incluido na mensalidade:", planIncluided)


# #Alternativa 2
# print("Nome do jogo:", name, "\n Ano de lançamento:", yearLaunch,
#       "\n Preço do jogo:", gamePrice, "\n Está incluso no serviço?", planIncluided)



#Alternativa 3 / F string (recomnedada)
print(f"Nome do jogo: {name} \n Ano Lançamento: {yearLaunch} \n Preço do Jogo: {gamePrice} \n Está incluso no serviço? {planIncluided}")