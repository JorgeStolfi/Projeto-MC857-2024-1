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

ok_global = True # Vira {False} se algum teste falha.

# Sessao de teste:
ses = obj_sessao.obtem_objeto("S-00000001")
assert ses != None

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
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
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Testes
for bt_ver in False, True:
  for bt_fechar in False, True:
    for mostrar_usr in False, True:
      rot_teste = "R" + f"_brv{str(bt_ver)[0]}" + f"_btf{str(bt_fechar)[0]}" + f"_mus{str(mostrar_usr)[0]}"
      testa_gera(rot_teste,  list, ses, bt_ver, bt_fechar, mostrar_usr)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
