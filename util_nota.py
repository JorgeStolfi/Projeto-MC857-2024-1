import util_nota_IMP

def valida(chave, val, nulo_ok):
  """Exige que o parâmetro {val} seja um nota, ou um string que 
  pode ser convertido em nota com {float()}.
  
  Caso {val} seja uma nota válida, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_nota_IMP.valida(chave, val, nulo_ok)

def formata(val):        
  """Formata a nota {val} com duas casas decimais e tradução em emojis,
  arredondando para inteiro: 0 - muito ruim, 1 - ruim, 2 - indiferente,
  3 - bom, 4 - muito bom."""
  return util_nota_IMP.formata(val)
