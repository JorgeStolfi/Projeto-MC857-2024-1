#! /usr/bin/python3

# Interfaces usadas por este script:

import comando_fazer_logout
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes
from util_erros import aviso_prog

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
  funcao = comando_fazer_logout.processa
  html = False # Resultado é HTML?
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao(rot_teste, modulo, funcao, res_esp, html, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Testa logout com sesão {None}:
sesN = None
assert sesN == None
testa_processa("ErroNone", ( str, None, ), sesN, {})

# Testa logout com uma sessao ativa
sesA = obj_sessao.obtem_objeto("S-00000001")
assert sesA != None
assert obj_sessao.aberta(sesA)
testa_processa("Ok", ( str, None, ), sesA, {})
assert not obj_sessao.aberta(sesA)

# Testa logout com sesão já fechada:
sesF = sesA
assert sesF != None
assert not obj_sessao.aberta(sesF)
testa_processa("ErroInativa", ( str, None, ), sesF, {})
assert not obj_sessao.aberta(sesF)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
