#! /usr/bin/env python3

import html_bloco_resumo_de_sessao
import db_tabelas
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao de teste:
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

def testa_html_bloco_resumo_de_sessao(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_bloco_resumo_de_sessao
  funcao = modulo.gera

  # testes unitários de tipo
  res = funcao(*args)
  assert type(res) is tuple or type(res) is list
  for campo in res:
    assert type(campo) is str

  # Teste da função {gera} HTML
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Testes
testa_html_bloco_resumo_de_sessao("F_F", ses, False, False)
testa_html_bloco_resumo_de_sessao("F_T", ses, False, True)
testa_html_bloco_resumo_de_sessao("T_F", ses, True,  False)
testa_html_bloco_resumo_de_sessao("T_T", ses, True,  True)

sys.stderr.write("Testes terminados normalmente.\n")
