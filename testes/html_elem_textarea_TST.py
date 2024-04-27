import html_elem_textarea
import util_testes

import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = html_elem_textarea
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, modulo.gera, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
   
testa_gera("text_dica",   str, "Peso",    "peso", "idpeso", None,         True,  "Máximo 50 kg", "vade_retro", True, None, None)
testa_gera("text_vini",   str, "Peso",    "peso", "idpeso", None,         True,  None,           "vade_retro", True, None, None)
testa_gera("text_rdonly", str, "Peso",    "peso", None,     "50",         False, None,           "vade_retro", True, None, None)

testa_gera("text_obrTV",  str, "Usuario", "user", "iduser", "U-12345678", True,  None,           "do_it", True, None, None)
testa_gera("text_obrFV",  str, None,      "user", "iduser", "U-12345678", True,  None,           "do_it", True, None, None)
testa_gera("text_obrFN",  str, None,      "user", "iduser", None,         True,  "Seu UID",      "do_it", True, None, None)

testa_gera("text_dica_with_size",   str, "Peso",    "peso", "idpeso", None,         True,  "Máximo 50 kg", "vade_retro", True, 150, 300)
testa_gera("text_vini_with_size",   str, "Peso",    "peso", "idpeso", None,         True,  None,           "vade_retro", True, 150, 300)
testa_gera("text_rdonly_with_size", str, "Peso",    "peso", None,     "50",         False, None,           "vade_retro", True, 150, 300)

testa_gera("text_obrTV_with_size",  str, "Usuario", "user", "iduser", "U-12345678", True,  None,           "do_it", True, 150, 300)
testa_gera("text_obrFV_with_size",  str, None,      "user", "iduser", "U-12345678", True,  None,           "do_it", True, 150, 300)
testa_gera("text_obrFN_with_size",  str, None,      "user", "iduser", None,         True,  "Seu UID",      "do_it", True, 150, 300)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.");
else:
  aviso_erro("Alguns testes falharam", True)
