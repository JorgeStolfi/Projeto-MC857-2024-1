import util_booleano
import sys

def valida(chave, val, nulo_ok):

  erros = []
  if val == None:
    if not nulo_ok:
      erros.append(f"campo '{chave}' não pode ser omitido")
  elif not isinstance(val, bool):
    erros.append(f"campo '{chave}' tem tipo inválido {type(val)}")
  else:
    # Must be a bool:
    pass
  return erros
