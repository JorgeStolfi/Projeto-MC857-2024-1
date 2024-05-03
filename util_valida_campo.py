# Este módulo define funções para verificar a validade de dados digitados
# pelo usuário em diversos formulários.

# Cada função abaixo verifica se o parâmetro {val} satisfaz certas
# condições. Em caso afirmativo, a função devolve uma lista vazia. Senão
# devolve uma lista de uma ou mais mensagens de erro (strings). O
# parâmetro {chave} é usado para montar as mensagens de erro.

# O parâmetro booleano {nulo_ok} diz se {None} deve ser considerado
# um valor válido de {val} (se {True}) ou não (se {False}).

import util_valida_campo_IMP

def booleano(chave, val, nulo_ok):
  """Exige que o parâmetro {val} seja um booleano."""
  return util_valida_campo_IMP.booleano(chave, val, nulo_ok)

def identificador(chave, val, letra, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  identificador, no formato "{L}-{NNNNNNNN} onde {L} é a {letra}
  dada e {NNNNNNNN} são 8 dígitos decimais.  Se {letra} for {None},
  aceita qualquer letra maiúscula."""
  return util_valida_campo_IMP.identificador(chave, val, letra, nulo_ok) 

def data(chave, val, nulo_ok):
  """Toda data no sistema deve ser um string to formato ISO 
  "{yyyy}-{mm}-{dd} {HH}:{MM}:{SS} UTC". O campo {yyyy}
  deve ter quatro dígitos começando com "19" ou "20". 
  Os demais campos devem ter exatamente dois algarismos.  O mes 
  {mm} pode ser de "01" a "12", o dia {dd} pode ser de "01" a "31",
  a hora {HH} de "00" a "23", o minuto {MM} de "01" a "59",
  e o segundo {SS} de "01" a "60" [sic]."""
  return util_valida_campo_IMP.data(chave, val, nulo_ok)

  
