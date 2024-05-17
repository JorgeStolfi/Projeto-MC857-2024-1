import util_booleano
import sys

def valida(chave, val, nulo_ok):

  erros = []
  if val == None:
    if not nulo_ok:
      erros.append(f"O campo '{chave}' não pode ser omitido")
  elif not isinstance(val, bool):
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{bool}'}")
  else:
    # Must be a bool:
    pass
  return erros
