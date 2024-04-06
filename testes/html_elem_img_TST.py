#! /usr/bin/python3

import html_elem_img
import util_testes

import sys

def testa_gera(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_elem_img
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args)
 
testa_gera("1", "GO.png", "Texto alternativo da imagem", 100)

sys.stderr.write("Testes terminados normalmente.");
