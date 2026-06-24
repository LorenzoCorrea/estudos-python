num1 = float(input("Digite o primeiro numero: \n"))
num2 = float(input("Digite o segundo numero: \n"))

operation = input("digite a operação a realizar (+, -, /, *) \n")

### Um = (Atribuição, receber) dois == (Comparação)

if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  result = num1 / num2
else:
  print("Operalção inválida")
  resul = 0

print(f"Resultado é: {result:.2f}") ### os .2f serve para delimitar o resultado para apenas 2 casas decimais