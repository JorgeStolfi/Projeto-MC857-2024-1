import util_senha
import sys, re

def valida(chave, val, nulo_ok):

  # O padrão {re} para caracter ASCII visível é [!-~], e para
  # letra ou dígito é [A-Za-z0-9].

  erros = []
  epref = f"O campo '{chave}' "

  if val == None:
    if not nulo_ok:# !!! Implementar conforme documentação na interface !!!
      erros.append(epref + f"não pode ser omitido")
  elif not isinstance(val, str):
    erros.append(epref + f"não é senha válida: deve ser string")
  else:
    if not re.search(r'^[!-~]*$', val):
      erros.append(epref + f"não é senha válida: pode conter apenas caracters visíveis ASCII ([!-~])")
    nmin = 8  # Comprimento mínimo.
    nmax = 14 # Comprimento máximo.
    n = len(val)
    if n < nmin:
      erros += [ epref + f"não é senha válida: muito curto ({n} caracteres, mínimo {nmin})"]
    elif n > nmax:
      erros += [ epref + f"não é senha válida: muito longo ({n} caracteres, máximo {nmax})"]
    if not re.search(r'[A-Za-z]', val):
      erros.append(epref + f"não é senha válida: deve conter no mínimo uma letra")
    if not re.search(r'[0-9]', val):
      erros.append(epref + f"não é senha válida: deve conter no mínimo um dígito")
    if re.search(r'^[a-zA-Z0-9]*$', val):
      erros.append(epref + f"não é senha válida: não pode ser apenas letras e dígitos")
  return erros
