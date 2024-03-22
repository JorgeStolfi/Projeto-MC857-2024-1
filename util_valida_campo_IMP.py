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
      # !!! Verificar caracteres permitidos !!!
  return erros
  
def senha(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def email(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []


