import util_nome_de_usuario
import sys, re
from math import floor

def valida(chave, val, nulo_ok, padrao_ok):

  erros = []
  epref = f"campo '{chave}' = \"{val}\" "

  if val == None:
    if not nulo_ok: erros.append(f"campo '{chave}' não pode ser omitido")
  elif not isinstance(val, str):
    erros.append(f"campo '{chave}' tem tipo inválido {type(val)}")
  else:
    # Verifica se é padrão de busca por semelhança:
    parcial = (len(val) >= 2 and val[0] == "*" and val[-1] == "*")
    if parcial: 
      if not padrao_ok:
        erros.append(f"campo {chave} não pode ser um padrão \"*...*\"")
      val = val[1:-1]
    
    # Verifica se {val} pode ser nome ou pedaço de nome:
    nmin = 3 if parcial else 10
    nmax = 60
    n = len(val)
    if n < nmin:
      erros.append(epref + f"é muito curto ({n} caracteres, mínimo {nmin})")
    elif n > nmax:
      erros.append(epref + f"é muito longo ({n} caracteres, máximo {nmax})")

    re_car_validos = r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s.'-]+$"
    if not re.match(re_car_validos, val):
      erros.append(epref + f"tem caracteres não permitidos")

    if not parcial and (val[0].isspace() or val[-1].isspace()):
      erros.append(epref + f"tem branco antes ou depois do nome")

    if '  ' in val:
      erros.append(epref + f"tem dois ou mais espaços seguidos")

    if not parcial and not val[0].isupper():
      erros.append(epref + f"não começa com letra maiúscula")

    if not parcial and not val[-1].isalpha():
      erros.append(epref + f"não termina com uma letra")
    
    re_pto_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ][.]" if parcial else r"(^|[^a-zA-ZÀ-ÖØ-öø-ÿ])[.]"
    if re.match(re_pto_prev, val):
      erros.append(epref + f"tem um ponto que não segue uma letra")
      
    re_pto_prox = r"[.][^-\s]" if parcial else r"[.]([^-\s]|$)"
    if re.match(re_pto_prox, val):
      erros.append(epref + f"tem um ponto que não é seguido por hífen ou branco")
    
    re_apo_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ][']" if parcial else r"(^|[^a-zA-ZÀ-ÖØ-öø-ÿ])[']"
    if re.match(re_apo_prev, val):
      erros.append(epref + f"tem um apóstrofe que não segue uma letra")
      
    re_apo_prox = r"['][^A-ZÀ-ÖØ-Þ]" if parcial else r"[']([^A-ZÀ-ÖØ-Þ]|$)"
    if re.match(re_apo_prox, val):
      erros.append(epref + f"tem um apóstrofe que não é seguido por letra maiúscula")
    
    re_hif_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ.][-]" if parcial else r"(^|[^a-zA-ZÀ-ÖØ-öø-ÿ.])[-]"
    if re.match(re_hif_prev, val):
      erros.append(epref + f"tem um hífen que não segue letra ou ponto")
      
    re_hif_prox = r"[-][^A-ZÀ-ÖØ-Þ]" if parcial else r"[-]([^A-ZÀ-ÖØ-Þ]|$)"
    if re.match(re_hif_prox, val):
      erros.append(epref + f"tem um hífen que não é seguido por uma letra maiúscula")

  return erros
