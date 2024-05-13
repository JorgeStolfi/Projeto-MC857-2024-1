#! /usr/bin/python3

import comando_solicitar_pag_buscar_sessoes
import db_tabelas_do_sistema
import obj_sessao
import obj_usuario
import db_base_sql
import util_testes
from util_erros import erro_prog

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_solicitar_pag_buscar_sessoes
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

sesC = obj_sessao.obtem_objeto("S-00000003")
sesA = obj_sessao.obtem_objeto("S-00000001")

lixo_args = {'any_arg': 'any_val'}

test_suites = [
  ('t01', str,              None, {}),        # Mostra pagina de erro: somente administradores podem acessar
  ('t02', str,              sesC, {}),        # Mostra pagina de erro: somente administradores podem acessar
  ('t03', str,              sesA, {}),        # Mostra pagina com formulario de buscar sessoes
  ('t04', 'AssertionError', sesA, lixo_args), # Levanta AssertionError por conta de argumentos espúrios
]

for suite in test_suites:
  testa_processa(*suite)

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  erro_prog("Alguns testes falharam")
