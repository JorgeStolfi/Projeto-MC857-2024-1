#! /usr/bin/python3

import db_base_sql
import comando_ver_conversa
import db_tabelas_do_sistema
import obj_sessao
import obj_comentario
import util_testes
from util_erros import erro_prog, aviso_prog, mostra
import comando_ver_objeto

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
  
  global ok_global
  modulo = comando_ver_comentario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Obtem uma sessao de um usuario que é de administrador:
ses_A1 = obj_sessao.obtem_objeto("S-00000001")
assert obj_sessao.de_administrador(ses_A1)

# Obtem uma sessao de um usuario comum:
ses_C1 = obj_sessao.obtem_objeto("S-00000003")
assert not obj_sessao.de_administrador(ses_C1)

erro_prog("!!! {comando_ver_convera_TST} não foi implementado !!!")

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  erro_prog("Alguns testes falharam")
