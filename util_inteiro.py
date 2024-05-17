import util_inteiro_IMP

def valida(chave, val, val_min, val_max, nulo_ok):
  """Exige que o parâmetro {val} seja um inteiro, ou um string que 
  pode ser convertido em inteiro com {int()}.
  
  Se {val_min} não é {None}, deve ser um inteiro, e {val} deve ser no mínimo {val_min}.
  
  Se {val_max} não é {None}, deve ser um inteiro, e {val} deve ser no máximo {val_max}.
  
  Caso {val} seja um inteiro válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_inteiro_IMP.valida(chave, val, val_min, val_max, nulo_ok)
