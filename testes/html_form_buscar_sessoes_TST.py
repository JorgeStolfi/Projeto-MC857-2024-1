#! /usr/bin/python3

import html_form_buscar_sessoes
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

atrs1 = { 'usuario': "U-00000002", 'aberta': True }
atrs2 = {}

for admin in False, True:
  testa_gera("ComValores-a" + str(admin)[0], atrs1, admin)
  testa_gera("SemValores-a" + str(admin)[0], atrs2, admin)

sys.stderr.write("Testes terminados normalmente.")

