#! /usr/bin/python3

import html_form_buscar_videos
import util_testes

import sys

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_form_buscar_sessoes
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)
  return

atrs1 = \
  { 'video': 'V-11111111', 
    'titulo': 'La la land', 
    'autor': 'José Primeiro', 
    'arq': 'la_la_land.mp4',
  }

testa_gera("SemValores", {})
testa_gera("ComValores", atrs1)

sys.stderr.write("Testes terminados normalmente.")
