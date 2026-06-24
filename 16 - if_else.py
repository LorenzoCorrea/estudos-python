name = input("Digite o nome do jogo: \n")
yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"))
classification = float(input("Digite a nota de classificação do jogo: \n"))

if classification > 8.0 and  yearLaunch >2015:                                #### A estrutura do if else (simples):
  print("Recomendo o jogo!")                                                  #### if STRING:
else:
  print("Não recomnedo o jogo!")