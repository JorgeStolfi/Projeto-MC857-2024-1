import util_nota
import sys
import re

def valida(chave, val, nulo_ok):

  erros = []
  val_num = None
  if val == None:
    if not nulo_ok:
      erros.append(f"O campo '{chave}' não pode ser omitido")
  elif isinstance(val, str):
    if re.match(r"^[-+]?[0-9]*([0-9]|[.][0-9]+)$", val):
      val_num = int(float(val)*100)/100
    else:
      erros.append(f"O campo '{chave}' = \"{val}\" de tipo {'{str}'} não é uma nota válida")
  elif isinstance(val, int):
    val_num = float(val)
  elif isinstance(val, float):
    val_num = val
  else:
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{int}'} ou {'{float}'}")

  val_min = 0.0
  val_max = 4.0
  if val_num != None:
    if val_min != None and val_num < val_min:
      erros.append(f"O campo '{chave}' = {val_num}, devia ser no mínimo {val_min}")
    if val_max != None and val_num > val_max:
      erros.append(f"O campo '{chave}' = {val_num}, devia ser no máximo {val_max}")

  return erros

def formata(val):        
  nota = float(val)
  assert nota >= 0.0 and nota <= 4.0, f"Nota {nota} inválida"
  texto = f"{nota:.2f} "
  emoji = [ "🤮", "😞", "😐", "😊", "😍", ]
  texto += emoji[round(nota)]
  return texto
