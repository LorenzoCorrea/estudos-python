# Crie uma função chamada quadrado(numero) que recebe um número como argumento e retorna o quadrado dele.

# Depois, use a função com um valor recebido via input() e exiba o resultado com print().

# Crie uma função chamada apresentar_pessoa(nome, idade) que exibe a seguinte mensagem:

# "Nome: <nome> | Idade: <idade> anos"
# Chame a função passando valores diferentes.

# Crie uma função chamada verificar_par(numero) que retorna:

# "Par" se o número for par

# "Ímpar" se for ímpar

# Peça um número ao usuário com input(), chame a função e mostre o resultado.

# 1. Criando a função corretamente
def quadrado(numero):
    return numero ** 2  # Elevando ao quadrado

# 2. Recebendo o valor do usuário e convertendo para número inteiro (int)
texto_digitado = input("Digite um número: ")
valor = int(texto_digitado)

# 3. Usando a função com o valor que o usuário digitou
resultado = quadrado(valor)

# 4. Exibindo o resultado
print(f"O quadrado do número é: {resultado}")