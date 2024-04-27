#! /usr/bin/python3

import html_bloco_menu_geral
import util_testes
import sys

import db_base_sql
import db_tabelas_do_sistema

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = html_bloco_menu_geral
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

testa_gera("deslogado", str, False, None,            False)
testa_gera("comum",     str, True,  "João Segundo", False)
testa_gera("admin",     str, True,  "José Primeiro",  True)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
