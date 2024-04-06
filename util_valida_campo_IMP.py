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
  return []
  
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
        erros += [ "nome de usuário (%d caracteres) muito longo" % (rotulo,n), ]
      padrao = r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s.'-]+$"
      if not re.match(padrao, val):
        erros += [ "campo '%s' não permite caracteres especiais nem números" % rotulo, ]
  return erros
  
def senha(rotulo, val ):
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


