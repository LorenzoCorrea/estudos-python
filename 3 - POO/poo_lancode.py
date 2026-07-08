### O que não é POO?
##exemplo: Esse codigo cria uma função de soma e soma 2 + 3
# def somar (a, b):
#   return a + b

# resultado = somar(2, 3)
# print(resultado)

#Isso é um exemplo de programaçõ estruturada, segue uma linha reta
#Poo é uma base (molde) para criar objetos
#Uma classe (exemplo: canal) contem atributos (nome, descrição, inscrito)


class Canal:
  def __init__(self, nome, descricao, inscritos):  ###Função dentro de uma classe é método // Init é o método construtor, 
    self.nome = nome ###Self representa instancia, ou seja está instanciando o "canal_lancode"
    self.descricao = descricao
    self.inscritos = inscritos

  def inscrever(self, quantidade=1):
    self.inscritos += quantidade

class CanalEmpresarial(Canal): ##O canal empresarial herdou do "CANAL"
  def __init__(self, nome, descricao, inscritos):
    super().__init__(nome, descricao, inscritos) ###Super chama a classe pai, de cima ou seja a CANAL
    self._equipe = []

  @property 
  def equipe(self):
    return self._equipe
  
  def adicionar_membro_equipe(self, membro):
    if membro not in self._equipe:
      self._equipe.append(membro)
    else:
      print(f"O membro {membro} ja está na equipe!")

  def remover_membro_equipe(self, membro):
    if membro in self._equipe:
      self._equipe.remove(membro)
    else:
      print(f"O membro {membro} não está mais na equipe")


canal_lohn= Canal("Lohn", "Sem desc", 0)
canal_lancode = Canal("Lancode", "Códigos e Gatos", 65600)
canal_duolingo = CanalEmpresarial("Duolingo", "ingres", 6000000)

canal_duolingo.adicionar_membro_equipe("Pedro")
canal_duolingo.remover_membro_equipe("Pedro")
canal_duolingo.adicionar_membro_equipe("Andre")
print(f"Membros Atuais: \n {canal_duolingo.equipe}")
