#! /usr/bin/python3

import html_form_buscar_usuarios
import obj_usuario
import obj_sessao
import db_base_sql
import db_tabelas_do_sistema
import util_testes

import sys

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_form_buscar_usuarios
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

atrs1 = { 'nome': "José", 'email': "unicamp.br" }

for admin in False, True:
  testa_gera("ComValores-adm" + str(admin)[0], atrs1, admin)
  testa_gera("SemValores-adm" + str(admin)[0], {},    admin)

sys.stderr.write("Testes terminados normalmente.")
