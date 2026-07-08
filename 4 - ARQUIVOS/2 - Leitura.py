'''
- Arquivos:
1 - W - Write - Escrever
2 - A - Append - Adicionar no final da lista
3 - R - Read


'''

with open("names.txt", "r") as file:
  for line in file:
    print(line)


#Leitura serve pra colocar o conteudo do txt criado na escrita no terminal