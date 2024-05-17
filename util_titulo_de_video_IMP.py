import util_titulo_de_video
import sys, re

def valida(chave, val, nulo_ok):
 
  erros = [] 

  if val is None:
    if not nulo_ok: 
      erros.append(f"O campo '{chave}' não pode ser omitido")
  elif not isinstance(val, str):
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{str}'}")
  else:
  
    epref = f"Campo '{chave}' = \"{str(val)}\": "

    n = len(val)

    parcial = ( n >= 2 and val[0] == "*" and val[-1] == "*" )
    if parcial:
      val = val[1:-1]
      n = len(val)
  
    nmin = 3 if parcial else 10
    nmax = 60
    if len(val) < nmin:
      erros.append(epref + f"é muito curto ({n} caracteres, mínimo {nmin})")
    elif len(val) > nmax:
      erros.append(epref + f"é muito longo ({n} caracteres, máximo {nmax})")

    if not parcial and n > 0 and not val[0].isupper():
      erros.append(epref + f"a primeira letra deve ser maiúscula")

    if not parcial and n > 0 and val[-1].isspace():
      erros.append(epref + f"não pode terminar com espaços")

    if "  "  in val:
      erros.append(epref + f"não pode conter dois espaços seguidos")

    # Caracterers válidos ISO-Latin-1:
    padrao = r'^[A-Za-z0-9À-ÖØ-öø-ÿ!"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~\s]+$'
    if not re.match(padrao, val):
      erros.append(epref + f"contém caracteres não permitidos")

  return erros
