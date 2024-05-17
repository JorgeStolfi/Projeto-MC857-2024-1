import sys, re

def valida_email(chave, val, nulo_ok):

  # Validação de tipos (paranóia):
  assert isinstance(chave, str)
  assert isinstance(nulo_ok, bool)
  
  erros = []
  
  if val == None:
    if not nulo_ok: erros.append(f"O campo '{chave}' não pode ser omitido")
  elif type(val) is not str:
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{str}'}")
  elif re.search(r"@.*@", val):
    erros.append(f"O campo '{chave}' = \"{val}\" tem mais de um caracter '@'")
  else:
    indice_arr = val.find("@")
    if indice_arr < 0:
      erros.append(f"O campo '{chave}' = \"{val}\" não tem o caracter '@'")
    else:
      erros += valida_email_cx_postal(chave, val[0:indice_arr])
      erros += valida_email_dominio(chave, val[indice_arr+1:])
  return erros

def valida_email_cx_postal(chave, cx):
  """ Valida a parte de um email antes da '@'."""

  erros = []
  if cx == "":
    erros.append(f"Campo '{chave}': a caixa postal não pode ser vazia")
  else:
    epref = f"Campo '{chave}': a caixa postal \"{cx}\"" 
    n = len(cx)
    nmax = 64
    if n > nmax:
      erros.append(f"{epref} é muito longa ({n} caracteres, maximo {nmax}")

    re_validos = r"[A-Za-z0-9.%'/-]"
    if not re.match(r"^" + re_validos + "+$", cx):
      erros.append(f"{epref} tem caracteres inválidos - pode ter só {re_validos}")

    if cx[0] == "." or cx[-1] == ".":
      erros.append(f"{epref} não pode começar ou terminar com ponto")

    if cx.find("..") >= 0:
      erros.append(f"{epref} não pode ter dois pontos seguidos")

  return erros
  

def valida_email_dominio(chave, dom):
  """ Valida a parte de um email depois da '@'."""

  erros = []

  if dom == "":
    erros.append(f"Campo '{chave}': o domínio não pode ser vazio")
  else:

    epref = f"Campo '{chave}', domínio \"{dom}\": " 
    n = len(dom)
    nmax = 255
    if n > nmax:
      erros.append(f"{epref}muito longo ({n} caracteres, maximo {nmax}")

    partes = dom.split('.')
    assert len(partes) >= 1 # Porque neste ponto {dom} não é vazia.
    for parte in partes:
      erros += valida_email_dominio_parte(chave, parte)

    if re.match(r"^[0-9]*$", partes[-1]):
      erros.append(f"{epref}a última parte não pode ser só dígitos")
    
  return erros

def valida_email_dominio_parte(chave, parte):
  """ Valida a parte de um email depois da '@'."""

  erros = []

  if parte == "":
    erros.append(f"Campo '{chave}': o domínio não pode ter partes vazias")
  else:
    epref = f"Campo '{chave}', parte \"{parte}\" do domínio: " 

    n = len(parte)
    nmax = 63
    if n > nmax:
      erros.append(f"{epref}muito longa ({n} caracteres, maximo {nmax}")
    
    re_validos = r"[A-Za-z0-9-]"
  
    if not re.match(r"^" + re_validos + "+$", parte):
      erros.append(f"{epref}tem caracteres inválidos - pode ter só {re_validos}")

    if parte[0] == "-" or parte[-1] == "-":
      erros.append(f"{epref}não pode começar ou terminar com hífen")

  return erros
