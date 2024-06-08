import util_vistas
import sys
import re

def valida(chave, val, nulo_ok):

  erros = []
  val_num = None
  if val == None:
    if not nulo_ok:
      erros.append(f"O campo '{chave}' não pode ser omitido")
  elif isinstance(val, str):
    if re.match(r"^[-+]?[0-9]*$", val):
      val_num = int(val)
    else:
      erros.append(f"O campo '{chave}' = \"{val}\" de tipo {'{str}'} não é uma vistas válida")
  elif isinstance(val, int):
    val_num = val
  else:
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{int}'}")

  val_min = 0
  if val_num != None:
    if val_min != None and val_num < val_min:
      erros.append(f"O campo '{chave}' = {val_num}, devia ser no mínimo {val_min}")

  return erros

def formata(val):        
  vistas = int(val)
  assert vistas >= 0, f"Vistas {vistas} inválida"
  texto = f"{vistas} "
  return texto
