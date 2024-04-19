import html_elem_video
import util_testes

import sys

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  modulo = html_elem_video
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, modulo.gera, rot_teste, frag, pretty, *args)

testa_gera("1", "virus.mp4", "Um virus animado", 320)

sys.stderr.write("Testes terminados normalmente.");
