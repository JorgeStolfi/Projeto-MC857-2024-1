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

def nome_de_usuario(chave, val, nulo_ok):
  erros = [].copy()
  if val == None:
    if not nulo_ok: erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif type(val) is not str:
    erros += [ f"campo '{chave}' = \"{str(val)}\" não é nome válido: deve ser string" ]
  else:
    nmin = 6
    nmax = 60
    n = len(val)
    if n < nmin:
      erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: é muito curto ({n} caracteres, mínimo {nmin})" ]
    elif n > nmax:
      erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: é muito longo ({n} caracteres, máximo {nmax})" ]
    padrao = r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s.'-]+$"
    if not re.match(padrao, val):
      erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: tem caracteres não permitidos" ]
    if (not val[0].isupper()):
      erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: começa com letra minúscula" ]
    elif (not val[-1].isalpha()):
      erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: o último caractere não é uma letra" ]
    else:
        for i in range(1, n):
          digito = val[i]
          if (digito == "."):
              if (not val[i-1].isalpha()):
                erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: o ponto não segue uma letra" ]
              elif (val[i+1] != " "):
                erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: o ponto não é seguido por um espaço em branco" ]
          elif (digito == "'"):
              if (not val[i-1].isalpha()):
                erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: o apóstrofe não segue uma letra" ]
              elif (not val[i+1].isalpha() or not val[i+1].isupper()):
                erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: o apóstrofe não é seguido por uma letra maiúscula" ]
          elif (digito == "-"):
              if (not (val[i-1].isalpha() or val[i-1] != ".")):
                erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: o hífen não segue uma letra ou um ponto" ]
              elif (not val[i+1].isalpha() or not val[i+1].isupper()):
                erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: o hífen não é seguido por uma letra maiúscula" ]
          elif (digito == " "):
              if (not val[i+1].isalpha()):
                erros += [ f"campo '{chave}' = \"{val}\" não é nome válido: o espaço em branco não é seguido por uma letra" ]  
  return erros

def senha(chave, val, nulo_ok):
  # O padrão {re} para caracter ASCII visível é [!-~], e para
  # letra ou dígito é [A-Za-z0-9].
  erros = [].copy()
  if val == None:
    if not nulo_ok:
      erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif type(val) is not str:
    erros += [ f"campo '{chave}' = \"{str(val)}\" não é senha válida: deve ser string" ]
  else:
    if not re.search(r'^[!-~]*$', val):
      erros += [ f"campo '{chave}' não é senha válida: pode conter apenas caracters visíveis ASCII ([!-~])" ]
    nmin = 8  # Comprimento mínimo.
    nmax = 14 # Comprimento máximo.
    n = len(val)
    if n < nmin:
      erros += [ f"campo '{chave}' não é senha válida: muito curto ({n} caracteres, mínimo {nmin})"]
    elif n > nmax:
      erros += [ f"campo '{chave}' não é senha válida: muito longo ({n} caracteres, máximo {nmax})"]
    if not re.search(r'[A-Za-z]', val):
      erros += [ f"campo '{chave}' não é senha válida: deve conter no mínimo uma letra" ]
    if not re.search(r'[0-9]', val):
      erros += [ f"campo '{chave}' não é senha válida: deve conter no mínimo um dígito" ]
    if re.search(r'^[a-zA-Z0-9]*$', val):
      erros += [ f"campo '{chave}' não é senha válida: não pode ser apenas letras e dígitos" ]
  return erros

def email(chave, val, nulo_ok):
  erros = [].copy()
  if val == None:
    if not nulo_ok: erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif type(val) is not str:
    erros += [ f"campo '{chave}' = \"{str(val)}\" não é um email válido: deve ser string" ]
  else:
    # !!! Corrigir conforme documentado na interface !!!
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao_email, val):
      erros += [ f"campo '{chave}' = '%s' não é um email válido" % ( str(val))]
  
  return erros

def data(chave, val, nulo_ok):
  erros = [].copy()
  if val == None:
    if not nulo_ok: erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif type(val) is not str:
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
      if not ano <= 2099 and ano >= 1900:
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o ano deve estar em 1900..2099"]
      elif not mes <= 12 and mes >= 1:
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o mês deve estar em 01..12"]
      elif not dia <= 31 and dia >= 1:
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o dia deve estar em 01..31"]
      elif not hora <= 23 and hora >= 0:
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: a hora deve estar em 00..23"]
      elif not minuto <= 59 and minuto >= 0:
        erros += [ f"campo '{chave}' = \"{str(val)}\" é data inválida: o minuto deve estar em 00..59"]
      elif not segundo <= 60 and segundo >= 0:
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
  erros = [].copy() 
  # !!! Implementar conforme documentação na interface !!!
  return erros
