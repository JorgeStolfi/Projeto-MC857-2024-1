#! /usr/bin/python3

import comando_solicitar_pag_cadastrar_usuario
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import db_base_sql
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
  modulo = comando_solicitar_pag_cadastrar_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao de teste:
sessoes = [
  obj_sessao.obtem_objeto("S-00000001"),
  obj_sessao.obtem_objeto("S-00000002"),
  obj_sessao.obtem_objeto("S-00000003")
]
assert sessoes != None

for ses, rot_teste, atrs in ( 
    (sessoes[0], "N", None), 
    (sessoes[1], "V", []), 
    (None, "E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  testa_processa(rot_teste,  str, ses, atrs)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
