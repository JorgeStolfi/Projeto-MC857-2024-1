import util_booleano_IMP

def valida(chave, val, nulo_ok):
  """Exige que o parâmetro {val} seja um booleano.
  
  Caso {val} seja um booleano válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_booleano_IMP.valida(chave, val, nulo_ok)
