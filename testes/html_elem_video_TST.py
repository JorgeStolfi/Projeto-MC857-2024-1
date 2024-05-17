import html_elem_video
import util_testes

import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = html_elem_video
  funcao = html_elem_video.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

testa_gera("1", str, "V-00000001", 320)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n");
else:
  aviso_prog("Alguns testes falharam.", True)
