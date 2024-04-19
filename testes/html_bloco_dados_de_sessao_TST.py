#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import obj_sessao
import db_base_sql
import db_tabelas_do_sistema
import html_bloco_dados_de_sessao
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_html_bloco_dados_de_sessao(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_bloco_dados_de_sessao
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Testes do modulo:
ses1 = obj_sessao.busca_por_identificador("S-00000001")
assert ses1 != None
testa_html_bloco_dados_de_sessao("S", ses1)

sys.stderr.write("Testes terminados normalmente.\n")
