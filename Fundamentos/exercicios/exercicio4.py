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

number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1