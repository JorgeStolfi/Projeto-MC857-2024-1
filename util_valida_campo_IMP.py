# Imlementação do módulo {util_valida_campo}

import re



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
      # !!! Verificar caracteres permitidos !!!
  return erros
  
def senha(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  # O padrão {re} para caracter ASCII visível é [!-~], e para
  # letra ou dígito é [A-Za-z0-9].
  return []

def email(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def data(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

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
