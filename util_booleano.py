import util_booleano_IMP

def valida(chave, val, nulo_ok):
  """Exige que o parâmetro {val} seja um valor de tipo {bool}, ou um {int} ou string que
  representa um valor booleano.
  
  Se val é {int}, deve ser 0 para {False} ou 1 para {True}
  
  Se {val} é string, deve ser "true", "on", "yes", "1" representando {True},
  ou "false", "off", "no", "0" representando {False}.  Os strings exceto "on" e "off"
  podem ser abreviados para uma letra.
  
  Caso {val} seja válido, como acima, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_booleano_IMP.valida(chave, val, nulo_ok)

def converte(val):
  """Se {val} é um {bool}, devolve {val}. Se {val} é {int} ou string,
  converte para {bool} como descrito em {valida} acima.  Senão,
  falha com {AssertionFailure}."""
  return util_booleano_IMP.converte(val)
