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
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Testes do modulo:
ses1_id = "S-00000001"
ses1 = obj_sessao.obtem_objeto(ses1_id)
assert ses1 != None

for para_admin in False, True:
  for para_proprio in False, True:
    rot_teste = "S" + f"_adm{str(para_admin)[0]}" + f"_pro{str(para_proprio)[0]}"
    testa_gera(rot_teste,  str, ses1_id, para_admin, para_proprio)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
