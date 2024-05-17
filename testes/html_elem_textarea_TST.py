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
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
   
for alt, lar in ((None,None), (40, 800), (900, 300)):
  dim = f"{alt:04d}x{lar:04d}" if alt != None else ""
  testa_gera(f"text_dica" + dim,   str, "Titulo",  'peso',   "idtitu", None,             True,  "[dica] Título",   "vade_retro", True, alt, lar)
  testa_gera(f"text_vini" + dim,   str, "Titulo",  'peso',   "idtitu", None,             True,  None,              "vade_retro", True, alt, lar)
  testa_gera(f"text_rdonly" + dim, str, "Titulo",  'peso',   None,     "[val] Lusíadas", False, None,              "vade_retro", True, alt, lar)

  testa_gera(f"text_obrTV" + dim,  str, "Fofoca",  'fofoca', "idfofo", "[val] Magina!",  True,  None,              "manda_brasa", True, alt, lar)
  testa_gera(f"text_obrFV" + dim,  str, None,      'fofoca', "idfofo", "[val] Nossa!",   True,  None,              "manda_brasa", True, alt, lar)
  testa_gera(f"text_obrFN" + dim,  str, None,      'fofoca', "idfofo", None,             True,  "[dica] Conta aí", "manda_brasa", True, alt, lar)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n");
else:
  aviso_prog("Alguns testes falharam.", True)
