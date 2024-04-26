# Imlementação do módulo {util_valida_campo}

import sys, re
import util_valida_campo
from math import floor

def booleano(chave, val, nulo_ok):
  erros = [].copy()
  if val == None:
    if not nulo_ok: erros += [ f"campo '{chave}' não pode ser omitido" ]
  else:
    if not type(val) is bool:
      erros += [ f"campo '{chave}' = \"{str(val)}\" deve ser um booleano" ]
  return erros
  
def identificador(chave, val, letra, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ f"campo '{chave}' não pode ser omitido" ]
  else:
    if type(val) is not str:
      erros += [ f"campo '{chave}' = \"{str(val)}\" não é identificador válido: deve ser string" ]
    else:
      n = len(val)
      if letra != None and n >= 1 and val[0] != letra:
        erros += [ f"campo '{chave}' = \"{val}\" não é identificador válido: deve comecar com {letra}" ]
      if n != 10 or not re.match(r'^[A-Z]-[0-9]*$', val):
        erros += [ f"campo '{chave}' = \"{val}\" não é identificador válido: deve ser \"{letra}-\" e oito algarismos" ]
  return erros

def data(chave, val, nulo_ok):
  erros = [].copy()
  if val is None:
    if not nulo_ok:
      erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif not isinstance(val, str):
    erros += [ f"campo '{chave}' = \"{str(val)}\" deve ser uma string no formato ISO" ]
  else:
    # Padrão geral do formato ISO UTC:
    formatoISO = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$'
    if not re.match(formatoISO, val):
      erros += [ f"campo '{chave}' = \"{str(val)}\" deve ser uma string no formato ISO" ]
    else:
      ano = int(val[:4])
      mes = int(val[5:7])
      dia = int(val[8:10])
      hora = int(val[11:13])
      minuto = int(val[14:16])
      segundo = int(val[17:19])

      if not (1900 <= ano <= 2099):
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o ano deve estar em 1900..2099"]
      elif not (1 <= mes <= 12 ):
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o mês deve estar em 01..12"]
      elif not (1 <= dia <= 31 ):
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o dia deve estar em 01..31"]
      elif not (0 <= hora <= 23 ):
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: a hora deve estar em 00..23"]
      elif not (0 <= minuto <= 59):
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o minuto deve estar em 00..59"]
      elif not (0 <= segundo <= 60):
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o segundo deve estar em 00..60"]
  return erros

def nome_de_arq_video(chave, val, nulo_ok):
  erros = [].copy()
  if val is None and not nulo_ok:
    erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif not isinstance(val, str):
    erros += [ f"campo '{chave}' = \"{str(val)}\" é nome de arquivo inválido: deve ser string"]
  else:
    if not val.endswith(".mp4"):
      erros += [ f"campo '{chave}' = \"{val}\" é nome de arquivo inválido: deve ter extensão .mp4" ]
    nome_arq = val[:-4]
    if not re.match("^[A-Za-z0-9_]*$", nome_arq):
      erros += [ f"campo '{chave}' = \"{val}\" é nome de arquivo inválido: pode usar apenas apenas letras, dígitos, e underscores ASCII" ]
    nmin = 4
    nmax = 12
    n = len(nome_arq)
    if n < nmin:
      erros += [ f"campo '{chave}' = \"{nome_arq}\" é nome de arquivo inválido: muito curto ({n} caracteres, mínimo {nmin})" ]
    if n > nmax:
      erros += [ f"campo '{chave}' = \"{nome_arq}\" é nome de arquivo inválido: muito longo ({n} caracteres, maximo {nmax})" ]

  return erros

def titulo_de_video(chave, val, nulo_ok):

  # Erro crasso de programa, não deveria acontecer:
  assert val == None or type(val) is str, "argumento de tipo inválido"
 
  erros = [].copy() 

  if val is None:
    if not nulo_ok: erros.append(f"campo '{chave}' não pode ser omitido")
  else:
    n = len(val)
    nmin = 10
    nmax = 60
    if len(val) < nmin:
      erros.append(f"campo '{chave}' = \"{str(val)}\" muito curto ({n} caracteres, mínimo {nmin})")
    elif len(val) > nmax:
      erros.append(f"campo '{chave}' = \"{str(val)}\" muito longo ({n} caracteres, máximo {nmax})")

    if not val[0].isupper():
      erros.append(f"campo '{chave}' = \"{str(val)}\" a primeira letra deve ser maiúscula")

    if val[-1].isspace():
      erros.append(f"campo '{chave}' = \"{str(val)}\" não pode terminar com espaços")

    if "  "  in val:
      erros.append(f"campo '{chave}' = \"{str(val)}\" não pode conter dois espaços seguidos")

    # Caracterers válidos ISO-Latin-1:
    padrao = r'^[A-Za-z0-9À-ÖØ-öø-ÿ!"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~\s]+$'
    if not re.match(padrao, val):
      erros.append(f"campo '{chave}' = \"{str(val)}\" contém caracteres não permitidos")

  return erros
