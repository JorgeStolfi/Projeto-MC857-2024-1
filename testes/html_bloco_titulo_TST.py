#! /usr/bin/python3

import html_bloco_titulo
import util_testes

def testa_html_bloco_titulo(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_bloco_titulo
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

testa_html_bloco_titulo("R", "Sobre a Necessidade de Títulos Titulosos")
