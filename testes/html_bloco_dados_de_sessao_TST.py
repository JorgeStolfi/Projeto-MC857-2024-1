#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import obj_sessao
import db_base_sql
import db_tabelas_do_sistema
import html_bloco_dados_de_sessao
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
  modulo = html_bloco_dados_de_sessao
  funcao = html_bloco_dados_de_sessao.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Uma sessão de administrador:
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)
assert sesA != None
assert obj_sessao.de_administrador(sesA)

# Uma sessão de usuário comum:
sesC_id = "S-00000003"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert sesC != None
assert not obj_sessao.de_administrador(sesC)

# Uma sessão fechada:
sesF_id = "S-00000005"
sesF = obj_sessao.obtem_objeto(sesF_id)
assert sesF != None
obj_sessao.fecha(sesF)
assert not obj_sessao.aberta(sesF)

testa_gera("S_A",  str, sesA)
testa_gera("S_C",  str, sesC)
testa_gera("S_F",  str, sesF)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
