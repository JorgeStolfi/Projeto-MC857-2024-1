import util_data
import sys, re

def valida(chave, val, nulo_ok):

  erros = []
  epref = f"O campo '{chave}' = \"{val}\" "

  if val is None:
    if not nulo_ok:
      erros.append(f"O campo '{chave}' não pode ser omitido")
  elif not isinstance(val, str):
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{str}'}")
  else:
    # Padrão geral do formato ISO UTC:
    formatoISO = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$'
    if not re.match(formatoISO, val):
      erros.append(epref + f"deve ser uma string no formato ISO")
    else:
      ano = int(val[:4])
      mes = int(val[5:7])
      dia = int(val[8:10])
      hora = int(val[11:13])
      minuto = int(val[14:16])
      segundo = int(val[17:19])

      if not (1900 <= ano <= 2099):
        erros += [ epref + f"é data inválida: o ano deve estar em 1900..2099"]
      elif not (1 <= mes <= 12 ):
        erros += [ epref + f"é data inválida: o mês deve estar em 01..12"]
      elif not (1 <= dia <= 31 ):
        erros += [ epref + f"é data inválida: o dia deve estar em 01..31"]
      elif not (0 <= hora <= 23 ):
        erros += [ epref + f"é data inválida: a hora deve estar em 00..23"]
      elif not (0 <= minuto <= 59):
        erros += [ epref + f"é data inválida: o minuto deve estar em 00..59"]
      elif not (0 <= segundo <= 60):
        erros += [ epref + f"é data inválida: o segundo deve estar em 00..60"]
  return erros
