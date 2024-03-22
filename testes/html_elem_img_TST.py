#! /usr/bin/python3

import html_elem_img
import util_testes

import sys

def testa_gera(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_elem_img
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args)
 
testa_gera("1", "GO.png", "Texto alternativo da imagem", 100)

sys.stderr.write("Testes terminados normalmente.");
