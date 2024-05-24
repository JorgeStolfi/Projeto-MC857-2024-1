import util_voto
import sys
import re

def valida(chave, val, nulo_ok):

  erros = []
  val_num = None
  if val == None:
    if not nulo_ok:
      erros.append(f"O campo '{chave}' não pode ser omitido")
  elif isinstance(val, str):
    if re.match(r"^[-+]?[0-9]+$", val):
      val_num = int(val)
    else:
      erros.append(f"O campo '{chave}' = \"{val}\" de tipo {'{str}'} não é um voto válido")
  elif isinstance(val, int):
    val_num = val
  elif isinstance(val, float):
    val_num = int(val)
    if val_num != val:
      erros.append(f"Campo '{chave}' = \"{val}\": voto não pode ser fracionário")
  else:
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{int}'} ou {'{float}'}")

  val_min = 0
  val_max = 4
  if val_num != None:
    if val_min != None and val_num < val_min:
      erros.append(f"O campo '{chave}' = {val_num}, devia ser no mínimo {val_min}")
    if val_max != None and val_num > val_max:
      erros.append(f"O campo '{chave}' = {val_num}, devia ser no máximo {val_max}")

  return erros

def formata(val):        
  voto = int(val)
  assert voto >= 0 and voto <= 4, f"Voto {voto} inválida"
  emoji = [ "🤮", "😞", "😐", "😊", "😍", ]
  texto = emoji[round(voto)]
  return texto
