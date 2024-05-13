#! /usr/bin/python3

# Interfaces usadas por este script:

import html_linha_resumo_de_usuario
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

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_linha_resumo_de_usuario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

usr1_ident = "U-00000001"
usr1 = obj_usuario.obtem_objeto(usr1_ident)

usr2_ident = "U-00000002"
usr2 = obj_usuario.obtem_objeto(usr2_ident)

usr5_ident = "U-00000005"
usr5 = obj_usuario.obtem_objeto(usr5_ident)

testa_gera("TUSER1",  list, usr1)
testa_gera("TUSER2",  list, usr2)
testa_gera("TUSER5",  list, usr5)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
