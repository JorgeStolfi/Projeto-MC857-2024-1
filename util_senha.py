import util_senha_IMP
  
def valida(chave, val, nulo_ok):
  """O valor {val} deve ser uma cadeia de caracteres visíveis do conjunto ASCII,
  no intervalo [!-~].  Não pode ter letras acentuadas ou outros caracters
  Unicode, como "¿" ou "♫".  Deve ter no mínimo 8 e no máximo 14 caracters,
  e conter pelo menos uma letra, um dígito, e um caracter que não é nem 
  letra nem dígito.
  
  Caso {val} seja uma senha válida, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_senha_IMP.valida(chave, val, nulo_ok)
