# Imlementação do módulo {util_valida_campo}

import sys, re
import util_valida_campo
from math import floor

def booleano(rotulo, val, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if not type(val) is bool:
      erros += [ "campo '%s' = \"%s\" deve ser booleano" % (rotulo, str(val)) ]
  return erros
  
def identificador(rotulo, val, letra, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not str:
      erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
    else:
      n = len(val)
      if letra != None and n >= 1 and val[0] != letra:
        erros += [ "campo '%s' = \"%s\" deve comecar com %s" % (rotulo, val, letra) ]
      if n != 10 or not re.match(r'^[A-Z]-[0-9]*$', val):
        erros += [ "campo '%s' = \"%s\" tem formato inválido" % (rotulo, val) ]
  return erros

def nome_de_usuario(rotulo, val, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not str:
      erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
    else:
      n = len(val)
      if n < 6:
        erros += [ "campo '%s' (%d caracteres) muito curto" % (rotulo,n), ]
      elif n > 60:
        erros += [ "campo '%s' (%d caracteres) muito longo" % (rotulo,n), ]
      padrao = r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s.'-]+$"
      if not re.match(padrao, val):
        erros += [ "campo '%s' não permite caracteres especiais nem números" % rotulo, ]
  return erros

def senha(rotulo, val ):
  # O padrão {re} para caracter ASCII visível é [!-~], e para
  # letra ou dígito é [A-Za-z0-9].
  erros = []
  if val == None:
     erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not str:
      erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
    else:
      n = len(val)
      if n < 8:
        erros += ["campo '%s' não pode ter menos de 8  caracteres (%d caractes atualmente)  caracteres" % (rotulo, n)]
      elif n > 16:
        erros += ["campo '%s' não pode ter mais de 16 caracteres (%d caractes atualmente) caracteres" % (rotulo, n)]
      if not re.search(r'[A-Z]', val):
        erros += ["campo '%s' deve ter no mínimo 1 caracter maiúsculo" % rotulo,]
      if not re.search(r'[a-z]', val):
        erros += ["campo '%s' deve ter no mínimo 1 caracter minúsculo" % rotulo,]
      if not re.search(r'\d', val):
        erros += ["campo '%s' deve ter no mínimo 1 caracter numérico" % rotulo,]
      if not re.search(r'[!@#%¨&*()_+{}|:"<>?]]', val):
        erros += ["campo '%s' deve ter no mínimo 1 caracter especial" % rotulo,]
    return erros

def email(rotulo, val, nulo_ok):
  erros = []
  padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not str:
      erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
    elif not re.match(padrao_email, val):
      erros += ["campo '%s' deve conter um email válido. O email '%s' não é válido" % (rotulo, str(val))]
  
  return erros

def data_valida(data):
    formatoISO = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$'
    return re.match(formatoISO, data)

def data(rotulo, val, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    # verifica se é ISO
    if not data_valida(val):
      erros += [ "campo '%s' = \"%s\" deve ser uma string no formato ISO" % (rotulo, str(val)) ]
    else:
      ano = int(val[:4])
      mes = int(val[5:7])
      dia = int(val[8:10])
      hora = int(val[11:13])
      minuto = int(val[14:16])
      segundo = int(val[17:19])
      if not ano <= 2099 and ano >= 1900:
        erros += ["campo '%s' = \"%s\" - O ano não pode ser menor que 1900 ou maior que 2099" % (rotulo, str(val))]
      elif not mes <= 12 and mes >= 1:
        erros += ["campo '%s' = \"%s\" - O mês não pode ser menor que 1 ou maior que 12" % (rotulo, str(val))]
      elif not dia <= 31 and dia >= 1:
        erros += ["campo '%s' = \"%s\" - O dia não pode ser menor que 1 ou maior que 31" % (rotulo, str(val))]
      elif not hora <= 23 and hora >= 0:
        erros += ["campo '%s' = \"%s\" - A hora não pode ser menor que 0 ou maior que 23" % (rotulo, str(val))]
      elif not minuto <= 59 and minuto >= 1:
        erros += ["campo '%s' = \"%s\" - O minuto não pode ser menor que 1 ou maior que 59" % (rotulo, str(val))]
      elif not segundo <= 60 and segundo >= 1:
        erros += ["campo '%s' = \"%s\" - O segundo não pode ser menor que 1 ou maior que 60" % (rotulo, str(val))]
  return erros

def nome_de_arq_video(rotulo, val, nulo_ok):
  erros = []
  if val is None and not nulo_ok:
    erros += ["campo '%s' não pode ser omitido" % rotulo]
  elif not isinstance(val, str):
    erros += ["campo '%s' = \"%s\" deve ser string" % (rotulo, str(val))]
  else:
    if not val.endswith(".mp4"):
      erros += ["campo '%s' deve ser o nome de um arquivo de video .mp4" % rotulo]

    nome_arq = val[:-4]

    if nome_arq == "" or not val.endswith(".mp4"):
      erros += ["campo '%s', cujo valor é '%s' deve ser o nome de um arquivo de video não vazio seguido da extensão .mp4"% (rotulo, val)]

    if not re.match("^[A-Za-z0-9_-]*$", nome_arq):
      erros += ["campo '%s' deve ser conter apenas apenas letras, dígitos, e underscores ASCII" % rotulo]

  return erros
