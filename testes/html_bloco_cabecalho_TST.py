#! /usr/bin/python3

import html_bloco_cabecalho
import util_testes

def testa_html_bloco_cabecalho(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_bloco_cabecalho
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_html_bloco_cabecalho("P", "TESTINHO", False)
testa_html_bloco_cabecalho("G", "TESTÃO", True)
