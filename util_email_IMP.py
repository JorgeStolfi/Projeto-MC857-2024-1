import sys, re

def valida_email(chave, val, nulo_ok, padrao_ok):
  erros = [].copy()
  if val == None:
    if not nulo_ok: erros.append(f"campo '{chave}' não pode ser omitido")
  elif type(val) is not str:
    erros.append(f"campo '{chave}' = \"{str(val)}\" deve ser string")
  else:
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    padrao_email_aux=r'@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao_email, val) and not re.match(padrao_email_aux, val):
      erros.append(f"campo '{chave}' = '{str(val)}' não é um email válido" )

  if padrao_ok:
    erros.append(f"campo '{chave}': validação de padrões não está implementada")

  return erros
