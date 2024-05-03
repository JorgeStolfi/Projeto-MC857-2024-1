#! /usr/bin/python3

# Interfaces usadas por este script:

import comando_fazer_logout
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes

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
  modulo = comando_fazer_logout
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Testa logout com uma sessao nao ativa
ses = None
testa_processa("Erro", tuple, ses, {})
assert ses == None

# Testa logout com uma sessao ativa
ses = obj_sessao.obtem_objeto("S-00000001")
assert ses != None
assert obj_sessao.aberta(ses)

testa_processa("Ok",  str, ses, {})
assert not obj_sessao.aberta(ses)


if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
