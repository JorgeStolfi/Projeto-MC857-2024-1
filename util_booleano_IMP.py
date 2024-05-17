import util_booleano
import sys

def valida(chave, val, nulo_ok):

  erros = []
  if val == None or val == "":
    if not nulo_ok:
      erros.append(f"O campo '{chave}' não pode ser omitido")
  elif isinstance(val, bool):
    pass
  elif isinstance(val, int):
    if val == 0 or val == 1:
      pass
    else:
      erros.append(f"O campo '{chave}' de tipo {'{int}'} deveria ser 0 ou 1")
  elif isinstance(val, str):
    val = val.lower()
    if  val == "true"  or val == "t" or val == "yes" or val == "y" or val == "on"  or val == "1" or \
        val == "false" or val == "f" or val == "no"  or val == "n" or val == "off" or val == "0":
      pass
    else:
      erros.append(f"O campo '{chave}' de tipo {'{str}'} deveria representar um valor booleano")
  else:
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{bool}'}")

  return erros

def converte(val):
  if val == None or val == "":
    return None
  if isinstance(val, bool):
    return val
  elif isinstance(val, int):
    if val == 0:
      return False
    elif val == 1:
      return True
    else:
      return None
  elif isinstance(val, str):
    val = val.lower()
    if val == "false" or val == "f" or val == "no"  or val == "n" or val == "off" or val == "0":
      return False
    elif val == "true"  or val == "t" or val == "yes" or val == "y" or val == "on"  or val == "1":
      return True
    else:
      return None
  else:
    return None
