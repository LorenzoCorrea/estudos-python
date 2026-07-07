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
    super().__init__(nome, descricao, inscritos)

canal_lohn= Canal("Lohn", "Sem desc", 0)
canal_lancode = Canal("Lancode", "Códigos e Gatos", 65600)


