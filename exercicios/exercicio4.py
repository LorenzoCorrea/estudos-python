# Contagem Regressiva
# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e
#  disparar um “beep”.

contador = 10
for contador in range(10, -1, -1):
    print(f"Contagem Regressiva! {contador}")
print("... Boom!!")





# Tabuada
# Faça um programa que calcule a tabuada de um número, com
#  valores iniciais e finais informados pelo usuário

num = int(input("Digite o numero: \n"))
for num in range(10):
    print(f"A tabuada do {num} é:")