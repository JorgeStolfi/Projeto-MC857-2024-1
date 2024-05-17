import util_texto_de_comentario
import sys, re

def valida(chave, val, nulo_ok):
 
  erros = [] 
  epref = f"Campo '{chave}' = \"{str(val)}\": "

  if val is None:
    if not nulo_ok: 
      erros.append(f"campo '{chave}' não pode ser omitido")
  elif not isinstance(val, str):
    erros.append(f"campo '{chave}' tem tipo inválido {type(val)}")
  else:
    n = len(val)
    nmin = 1 
    nmax = 1003
    if len(val) < nmin:
      erros.append(epref + f"é muito curto ({n} caracteres, mínimo {nmin})")
    elif len(val) > nmax:
      erros.append(epref + f"é muito longo ({n} caracteres, máximo {nmax})")
      
    parcial = ( n >= 2 and val[0] == "*" and val[-1] == "*" )

    if parcial:
      val = val[1:-1]
      n = len(val)

    if not parcial and n > 0 and (val[0] == " " or val[0] == "\n"):
      erros.append(epref + f"a primeira letra não pode ser branco ou newline")

    if not parcial and n > 0 and (val[-1] == " " or val[-1] == "\n"):
      erros.append(epref + f"a primeira letra não pode ser branco ou newline")

    # Caracterers válidos para texto de comentario:
    padrao = r'^[A-Za-z0-9À-ÖØ-öø-ÿ!"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~\s' + "\n" + r']+$'
    if not re.match(padrao, val):
      erros.append(epref + f"contém caracteres não permitidos")

  return erros
