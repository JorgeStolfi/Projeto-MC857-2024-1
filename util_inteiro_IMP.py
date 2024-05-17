import util_inteiro
import sys

def valida(chave, val, val_min, val_max, nulo_ok):

  erros = []
  val_num = None
  if val == None:
    if not nulo_ok:
      erros.append(f"O campo '{chave}' não pode ser omitido")
  elif isinstance(val, str):
    if match(r"^[-+]?[0-9]+$", val):
      val_num = int(val)
    else:
      erros.append(f"O campo '{chave}' = \"{val}\" de tipo {'{str}'} não é um iteiro válido")
  elif isinstance(val, int):
    val_num = val
  else:
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{bool}'}")

  if val_num != None:
    if val_min != None and val_num < val_min:
      erros.append(f"O campo '{chave}' = {val_num}, devia ser no mínimo {val_min}")
    if val_max != None and val_num > val_max:
      erros.append(f"O campo '{chave}' = {val_num}, devia ser no máximo {val_max}")

  return erros
