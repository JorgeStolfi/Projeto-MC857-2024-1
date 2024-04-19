#! /usr/bin/python3
 
import html_form_buscar_comentarios
import util_testes

import sys

# Testes das funções de {html_elem_form}:

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_form_buscar_comentarios
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

atrs1 = { 'autor': "U-00000002", 'pai': "C-00000001" }

for admin in False, True:
  testa_gera("ComValores-adm" + str(admin)[0], atrs1, admin)
  testa_gera("SemValores-adm" + str(admin)[0], {},    admin)

sys.stderr.write("Testes terminados normalmente.")
