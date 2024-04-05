#! /usr/bin/python3

import html_bloco_rodape
import util_testes

def testa_html_bloco_rodape(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_bloco_rodape
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_html_bloco_rodape("R")
