#! /usr/bin/env python3

import html_linha_resumo_de_sessao
import db_tabelas_do_sistema
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# Sessao de teste:
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

def testa_html_linha_resumo_de_sessao(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_linha_resumo_de_sessao
  funcao = modulo.gera

  # testes unitários de tipo
  res = funcao(*args)
  assert type(res) is tuple or type(res) is list
  for campo in res:
    assert type(campo) is str

  # Teste da função {gera} HTML
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Testes
testa_html_linha_resumo_de_sessao("F_F", ses, False, False)
testa_html_linha_resumo_de_sessao("F_T", ses, False, True)
testa_html_linha_resumo_de_sessao("T_F", ses, True,  False)
testa_html_linha_resumo_de_sessao("T_T", ses, True,  True)

sys.stderr.write("Testes terminados normalmente.\n")
