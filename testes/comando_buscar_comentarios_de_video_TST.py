#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import comando_buscar_comentarios_de_video
import obj_sessao
import util_testes

import sys

# Conecta no banco e alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_buscar_comentarios_de_video
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessão em que o usuário dela é o administrador.
ses_adm_id = "S-00000001"
ses_adm = obj_sessao.obtem_objeto(ses_adm_id)

# Teste passando um id do video
testa_processa("T1",   str, ses_adm, {'video': "V-00000001"})
testa_processa("T2",   str, ses_adm, {'video': "V-00000002"})
testa_processa("T3",   str, None,    {'video': "V-00000003"})
testa_processa("T4",   str, None,    {'video': "V-00000004"})
testa_processa("T5",   str, None,    {'video': "V-00000005"})

if ok_global:
  sys.stderr.write("Testes terminados normalmente.")
else:
  aviso_erro("Alguns testes falharam", True)
