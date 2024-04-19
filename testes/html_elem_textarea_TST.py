import html_elem_textarea
import util_testes

import sys

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  modulo = html_elem_textarea
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, modulo.gera, rot_teste, frag, pretty, *args)
   
testa_gera("text_dica",   "Peso",    "peso", "idpeso", None,         True,  "Máximo 50 kg", "vade_retro", True)
testa_gera("text_vini",   "Peso",    "peso", "idpeso", None,         True,  None,           "vade_retro", True)
testa_gera("text_rdonly", "Peso",    "peso", None,     "50",         False, None,           "vade_retro", True)

testa_gera("text_obrTV",  "Usuario", "user", "iduser", "U-12345678", True,  None,           "do_it", True)
testa_gera("text_obrFV",  None,      "user", "iduser", "U-12345678", True,  None,           "do_it", True)
testa_gera("text_obrFN",  None,      "user", "iduser", None,         True,  "Seu UID",      "do_it", True)

sys.stderr.write("Testes terminados normalmente.");
