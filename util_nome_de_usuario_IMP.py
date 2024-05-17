import util_nome_de_usuario
import sys, re
from math import floor

def valida(chave, val, nulo_ok):

  erros = []

  if val == None:
    if not nulo_ok: erros.append(f"O campo '{chave}' não pode ser omitido")
  elif not isinstance(val, str):
    erros.append(f"O campo '{chave}' tem tipo inválido {type(val)}, devia ser {'{str}'}")
  else: 
    epref = f"O campo '{chave}' = \"{val}\" "

    nmin = 10
    nmax = 60
    n = len(val)
    if n < nmin:
      erros.append(epref + f"é muito curto ({n} caracteres, mínimo {nmin})")
    elif n > nmax:
      erros.append(epref + f"é muito longo ({n} caracteres, máximo {nmax})")

    re_car_validos = r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s.'-]+$"
    if not re.match(re_car_validos, val):
      erros.append(epref + f"tem caracteres não permitidos")

    if not val[0].isupper():
      erros.append(epref + f"não começa com letra maiúscula")

    if not val[-1].isalpha():
      erros.append(epref + f"não termina com uma letra")

    if '  ' in val:
      erros.append(epref + f"tem dois ou mais espaços seguidos")
    
    re_pto_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ][.]"
    if re.search(re_pto_prev, val):
      erros.append(epref + f"tem um ponto que não segue uma letra")
      
    re_pto_prox = r"[.][^-\s]"
    if re.search(re_pto_prox, val):
      erros.append(epref + f"tem um ponto que não é seguido por hífen ou branco")
    
    re_apo_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ][']"
    if re.match(re_apo_prev, val):
      erros.append(epref + f"tem um apóstrofe que não segue uma letra")
      
    re_apo_prox = r"['][^A-ZÀ-ÖØ-Þ]"
    if re.search(re_apo_prox, val):
      erros.append(epref + f"tem um apóstrofe que não é seguido por letra maiúscula")
    
    re_hif_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ.][-]"
    if re.search(re_hif_prev, val):
      erros.append(epref + f"tem um hífen que não segue letra ou ponto")
      
    re_hif_prox = r"[-][^A-ZÀ-ÖØ-Þ]"
    if re.search(re_hif_prox, val):
      erros.append(epref + f"tem um hífen que não é seguido por uma letra maiúscula")

  return erros
