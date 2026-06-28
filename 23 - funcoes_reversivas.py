"""

Fatorial de um numero:

3 - > 3 * 2 * 1

5 -> 5 * 4 * 3 * 2 *1
"""
# 1- fatorial de um numero
def factorial (num):
  if num == 1:
    return 1
  else: 
    return (num * factorial(num-1))

number = int(input("Digite um numero "))
print(f"o fatorial de {number} é {factorial(number)}")

