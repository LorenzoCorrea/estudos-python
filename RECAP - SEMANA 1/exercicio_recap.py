# 🗡️ Desafio 1: O Gerador de Códigos (Fundamentos, Strings e Slicing)
# As empresas de tecnologia costumam gerar códigos de acesso automáticos para os funcionários. Vamos criar um!
# O que você deve fazer:
# Peça para o usuário digitar o primeiro nome dele (ex: "Lorenzo").
# Peça para ele digitar o ano de nascimento (ex: 1995).
# Usando os métodos de string e fatiamento (slicing):
# Pegue apenas as 3 primeiras letras do nome e deixe tudo em MAIÚSCULO (Ex: "LOR").
# Pegue a palavra inteira e inverta ela de trás pra frente em letras minúsculas (Ex: "oznerol").
# Imprima na tela o código final usando F-String no formato:
# "Seu código de acesso é: LOR-oznerol-1995"    

# name = str(input("Digite seu nome: \n"))
# yearNasc = int(input("Digite seu ano de nascimento: \n"))
# # Pega as 3 primeiras e deixa maiúsculo 
# char = name[:3].upper()
# # Inverte a palavra E garante que fique tudo minúsculo
# acess1 = name[::-1].lower()

# print(f"{char}-{acess1}-{yearNasc}")











# 🎒 Desafio 2: O Inventário do Aventureiro (Listas, Sets e For)
# Você está programando o inventário de um jogo, mas houve um bug e o jogador 
# recebeu itens duplicados!
# O que você deve fazer:
# Crie no seu código a seguinte lista com itens repetidos:
# mochila = ["Poção", "Espada", "Poção", "Escudo", "Poção", "Mapa"]
# Usando o poder do tipo Set, remova todas as duplicatas da mochila de uma vez
#  só (lembre-se que Sets não aceitam repetições).
# Transforme esse Set de volta para uma Lista.
# Adicione o item "Arco" no final dessa nova lista.
# Use um laço for para imprimir cada item final do inventário do jogador,
#  um embaixo do outro.

# mochila = ["Poção", "Espada", "Poção", "Escudo", "Poção", "Mapa"]

# # 1. Transformamos em Set (limpa duplicatas) e logo em seguida de volta em Lista
# mochila_limpa = list(set(mochila))

# # 2. Agora sim, adicionamos o Arco no final da lista limpa
# mochila_limpa.append("Arco")

# # 3. O Viajante: Para cada 'item' individual dentro da 'mochila_limpa'
# for item in mochila_limpa:
#     print(item) # Imprime apenas o item da rodada








# 🏦 Desafio 3: O Caixa Eletrônico (While e If/Elif/Else)
# Vamos testar sua lógica de controle de repetições e tomadas de decisão.
# O que você deve fazer:
# Crie uma variável saldo começando com o valor 500.0.
# Crie um loop while que rode continuamente (você pode usar uma variável como opcao 
# != "3" para controlar o loop).
# Dentro do loop, mostre o saldo atual e dê 3 opções para o usuário (usando input):
# [1] Sacar
# [2] Depositar
# [3] Sair
# Use if/elif/else:
# Se for 1: Pergunte o valor do saque. Se o valor for maior que o saldo, imprima 
# "Saldo insuficiente!". Se não for, subtraia o valor do saldo.
# Se for 2: Pergunte o valor e some ao saldo.
# Se for 3: Imprima "Saindo..." e encerre o programa.

saldo = 500.0
opcao = ""

while opcao != "3":
    
    print(f"\n--- CAIXA ELETRÔNICO ---")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("[1] Sacar")
    print("[2] Depositar")
    print("[3] Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Repare como o if, os elif e o else estão colados na mesma reta vertical!
    if opcao == "1":
        valor = float(input("Quanto deseja sacar? R$ "))
        if valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo = saldo - valor
            print(f"Saque de R$ {valor:.2f} realizado!")

    elif opcao == "2":
        valor = float(input("Quanto deseja depositar? R$ "))
        saldo = saldo + valor
        print(f"Depósito de R$ {valor:.2f} realizado!")
        
    elif opcao == "3":
        print("Saindo do sistema... Até logo!")
        
    else:
        print("Opção inválida! Tente novamente.")
















# 🧙‍♂️ Desafio 4: A Taverna (Funções, Dicionários, *args e kwargs)
# Vamos criar a máquina que registra os heróis na guilda.

# O que você deve fazer:

# Crie uma função chamada registrar_heroi.

# Ela deve receber um parâmetro obrigatório nome, depois um *equipamentos (para as armas) e um atributos (para força, velocidade, etc).

# Dentro da função, faça o seguinte:

# Imprima o nome do herói.

# Use a função sum() para somar quantos equipamentos ele tem no total (lembre que *args vira uma tupla, e o len() conta o tamanho dela). Imprima: "Total de equipamentos: X".

# Use um for para viajar pelo atributos (lembre do .items()) e imprima o nome e o valor de cada atributo.

# Teste a função assim (pode copiar e colar essa última linha no seu código para testar):
# registrar_heroi("Arthur", "Espada", "Escudo", "Capa", forca=90, agilidade=75, magia=10)