name = input("Digite seu nome: \n")
'''
- Arquivos:
1 - W - Write
2 - A - Append
3 - R - Read


'''

file = open("names.txt", "w") ###Serve para trabalhar com arquivos
file.write(name)
file.close()