name = input("Digite seu nome: \n")
'''
- Arquivos:
1 - W - Write - Escrever
2 - A - Append - Adicionar no final da lista
3 - R - Read


'''


# #Alternativa 1
# file = open("names.txt", "a") ###Serve para trabalhar com arquivos
# file.write(f"{name}\n")
# file.close()


#Alternativa 2
with open("names.txt", "a") as file:
  file.write(f"{name}\n")