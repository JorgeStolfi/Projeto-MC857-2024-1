#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import obj_sessao
import db_base_sql
import db_tabelas
import html_bloco_dados_de_sessao
import util_testes

import sys

def testa_html_bloco_dados_de_sessao(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_bloco_dados_de_sessao
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# fixtures
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Testes das funções de {gera_html_elem_form}:
ses1 = obj_sessao.busca_por_identificador("S-00000001")
assert ses1 != None
testa_html_bloco_dados_de_sessao("S", ses1)

sys.stderr.write("Testes terminados normalmente.\n")
