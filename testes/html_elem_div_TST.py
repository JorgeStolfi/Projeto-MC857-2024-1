#! /usr/bin/python3

# Interfaces usadas por este script:

import html_elem_div
import util_testes

import sys

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{rot_teste}.html"."""
  
  modulo = html_elem_div
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

testa_gera("N", "font-family: 'Courier'; font-size: 30px", "Hello World")

sys.stderr.write("Testes terminados normalmente.");

