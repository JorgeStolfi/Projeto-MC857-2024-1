# Funções para conversão de identificador e índice

# Implementacao desta interface:
import util_identificador_IMP

def de_indice(let, indice):
  """Converte um índice inteiro {indice} em um string identificador da
  forma "{X}-{NNNNNNNN}" onde {X} é a string {let} dada e {NNNNNNNN} é o
  valor {indice} formatado em 8 algarismos decimais, com zeros à esquerda. Por exemplo,
  `util_identificador_de_indice("U",20557)` devolve "U-00020557".

  O índice {indice} deve estar em {0..99999999} ({10^8-1})."""
  return util_identificador_IMP.de_indice(let,indice)

def para_indice(let, ident):
  """Dado um identificador de objeto {ident}, da forma "{X}-{NNNNNNNN}",
  onde {X} deve ser a letra {let} dada, extrai o índice inteiro {NNNNNNNN} do 
  mesmo. Por exemplo, `indice_de_util_identificador("U","U-00020557")` devolve o inteiro 20555."""
  return util_identificador_IMP.para_indice(let,ident)

def de_lista_de_indices(let, indices):
  """Dada uma lista de list {indices} de índices de linhas de uma tabela, devolve
  uma lista com os identificadores dos objetos correspondentes. Se {indices} for {None}
  ou uma lista vazia, devolve uma lista vazia.
  
  Para conveniência, cada elemento da lista {indices} pode ser um inteiro, ou uma
  lista ou tupla de tamanho 1 cujo único elemento é um inteiro."""
  return util_identificador_IMP.de_lista_de_indices(let,indices)

def valida(chave, val, letra, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  identificador, no formato "{L}-{NNNNNNNN} onde {L} é a {letra}
  dada e {NNNNNNNN} são 8 dígitos decimais.  Se {letra} for {None},
  aceita qualquer letra maiúscula.
  
  Caso {val} seja um identificador válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_identificador_IMP.valida(chave, val, letra, nulo_ok) 
