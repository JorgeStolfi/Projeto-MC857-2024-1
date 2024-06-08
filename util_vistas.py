import util_vistas_IMP

def valida(chave, val, nulo_ok):
  """Exige que o parâmetro {val} seja um valor de vistas, ou um string que 
  pode ser convertido em vistas com {int()}.
  
  Caso {val} seja uma vistas válida, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_vistas_IMP.valida(chave, val, nulo_ok)

def formata(val):        
  """Formata a vistas {val} como inteiro"""
  return util_vistas_IMP.formata(val)
