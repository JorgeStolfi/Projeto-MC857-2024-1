import util_voto_IMP

def valida(chave, val, nulo_ok):
  """
  Exige que o parâmetro {val} seja um voto -- un inteiro em {0..4} --
  ou um string que pode ser convertido em voto com {int()}.
  
  Caso {val} seja uma voto válida, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro.
  """
  return util_voto_IMP.valida(chave, val, nulo_ok)

def formata(val):        
  """Formata a voto {val} (um inteiro em {0..4}, ou string conversível para tal)
  como emoji: 0 - muito ruim, 1 - ruim, 2 - indiferente,
  3 - bom, 4 - muito bom."""
  return util_voto_IMP.formata(val)
