#! /usr/bin/python3

import html_bloco_erro
import util_testes

import sys

# Testes das funções de {html_bloco_erro}:

def testa_html_bloco_erro(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_bloco_erro
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_html_bloco_erro("simple", "ERROR MESSAGE")
testa_html_bloco_erro("linebreak", "ERROR MESSAGE\nERROR DESCRIPTION")
testa_html_bloco_erro("multiple_arguments", [ "ERROR MESSAGE", "ERROR DESCRIPTION"])
testa_html_bloco_erro("all_combined", [ "ERROR TITLE", "ERROR DESCRIPTION 1\nERROR DESCRIPTION 2"])
