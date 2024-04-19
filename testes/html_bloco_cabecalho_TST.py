#! /usr/bin/python3

import html_bloco_cabecalho
import util_testes

def testa_html_bloco_cabecalho(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_bloco_cabecalho
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

testa_html_bloco_cabecalho("P", "TESTINHO", False)
testa_html_bloco_cabecalho("G", "TESTÃO", True)
