#! /usr/bin/python3

import html_elem_link_img
import util_testes

import sys

def testa_gera(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_elem_link_img
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args)


testa_gera("img1", "/logotipo.png", "logotipo", 100, "urlteste")

testa_gera("img2", "/AZ.png", "AZ", 50, "urlteste")

testa_gera("img3", "/GO.png", "GO", 75, "urlteste")

testa_gera("imgFalsa", "/falsa.png", "falsa", 150, "urlteste")

# testa_gera("noImg", None, "no image", 150, "urlteste")

sys.stderr.write("Testes terminados normalmente.");
