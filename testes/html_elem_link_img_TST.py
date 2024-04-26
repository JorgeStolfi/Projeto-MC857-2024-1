#! /usr/bin/python3

import html_elem_link_img
import util_testes

import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = html_elem_link_img
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, modulo.gera, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
 
testa_gera("img1",     str, "/logotipo.png", "logotipo",  100, "urlteste")

testa_gera("img2",     str, "/AZ.png",       "AZ",         50, "urlteste")

testa_gera("img3",     str, "/GO.png",       "GO",         75, "urlteste")

testa_gera("imgFalsa", str, "/falsa.png",    "falsa",     150, "urlteste")

testa_gera("noImg",    str, None,            "no image",  150, "urlteste")

if ok_global:
  sys.stderr.write("Testes terminados normalmente.");
else:
  aviso_erro("Alguns testes falharam", True)
