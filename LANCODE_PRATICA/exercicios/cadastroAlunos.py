# Você está chegando ao fim do básico da linguagem... Estou tão orgulhoso por te ver aqui! 💖

# Para prosseguirmos, gostaria de me certificar que você entendeu tudo que vimos ate então. Pois será de grande importância para os próximos temas! Portanto, criei um desafio um pouco mais difícil para você praticar. Se não conseguir, tudo bem! É algo no tanto quanto extenso, então não se culpe se não conseguir. Mas de qualquer forma, veja o vídeo de resolução! aposto que você aprenderá coisas que nem imaginava ser possível.



# 📚 Projeto: Sistema de Cadastro de Alunos
# Você foi contratado para desenvolver um pequeno sistema de cadastro de alunos para uma escola fictícia. 
# O sistema será usado no terminal e deve permitir que o usuário cadastre, consulte e remova alunos, além de exibir informações úteis sobre os dados inseridos.

# 🎯 Objetivo:
# Criar um sistema simples e funcional que utilize tudo o que você aprendeu até agora em Python — como listas, dicionários, funções, loops e condicionais.

# 🧠 O que seu programa deve fazer:
# Exibir um menu com as opções:
# 1. Adicionar aluno
# 2. Listar todos os alunos
# 3. Buscar aluno pelo nome
# 4. Remover aluno
# 5. Mostrar média geral das notas
# 6. Sair

# ✏️ Funcionalidades detalhadas:
# ➕ Adicionar aluno
# Pedir o nome, a idade e a nota (0 a 10) do aluno.

# Salvar os dados em um dicionário.

# Adicionar o dicionário a uma lista de alunos.

# 📋 Listar todos os alunos
# Mostrar todos os alunos cadastrados com nome, idade e nota.

# Exibir mensagem se não houver nenhum aluno.

# 🔍 Buscar aluno pelo nome
# Perguntar um nome e procurar na lista.

# Exibir os dados se o aluno for encontrado.

# Se não existir, exibir uma mensagem de erro.

# 🗑️ Remover aluno
# Perguntar o nome do aluno.

# Se existir, remover da lista.

# Se não existir, exibir aviso.

# 📊 Média geral das notas
# Calcular e exibir a média de todas as notas dos alunos cadastrados.

# Se não houver alunos, exibir uma mensagem adequada.

# ✅ Requisitos técnicos:
# Usar listas e dicionários para armazenar os dados.

# Separar funcionalidades em funções.

# Usar um loop principal com menu (while True) para manter o programa rodando até o usuário sair.

# Validar entradas (por exemplo: nota deve ser um número entre 0 e 10).




alunos = []  ### As chaves são para criar lista

def adicionar_aluno():
  nome = input("Digite o nome do aluno: \n")
  idade = int(input("Digite a idade do aluno: "))
  while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 0 and nota <= 10:
      break
    else:
      print("Nota inválida, a nota deve ser de 0 a 10.")
  dados = {
    'nome':nome,
    'idade':idade,
    'nota':nota
  }

  alunos.append(dados)




while True:
  opcao = int(input("O que deseja fazer?\n1. Adicionar Aluno\n2. Listar todos os Alunos\n3. Buscar aluno pelo nome\n4. remover aluno\n5. Mostrar media das notas\n6. Sair"))
  match opcao:
    case 1:
      ...
    case 2:
      ...
    case 3:
      ...
    case 4:
      ...
    case 5:
      ...
    case 6:
      break

