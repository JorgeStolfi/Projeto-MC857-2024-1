#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import html_form_upload_video
import obj_usuario
import util_identificador
import db_base_sql
import db_tabelas
import util_testes

import sys

from obj_usuario import obtem_atributos, obtem_identificador

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_upload_video
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# fixtures
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Testes das funções de {gera_html_elem_form}:
usr1 = obj_usuario.busca_por_identificador("U-00000001")
assert usr1 != None
testa_gera("N", obtem_identificador(usr1))

sys.stderr.write("Testes terminados normalmente.\n")
