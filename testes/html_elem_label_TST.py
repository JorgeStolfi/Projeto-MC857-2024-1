#! /usr/bin/python3

import html_elem_label 
import util_testes
import sys

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{rotulo}.html"."""
  
  modulo = html_elem_label
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_gera("1", "Banana", " --> ")

sys.stderr.write("Testes terminados normalmente.");
