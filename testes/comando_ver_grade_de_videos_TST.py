#! /usr/bin/python3

import comando_ver_grade_de_videos
import db_base_sql
import util_testes
import db_tabelas_do_sistema
import obj_sessao

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
  modulo = comando_ver_grade_de_videos
  funcao = modulo.processa
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Obtém uma sessão de um usuario que é de administrador:
ses_A = obj_sessao.obtem_objeto("S-00000001")
assert obj_sessao.de_administrador(ses_A)

# Obtém uma sessão de um usuario comum:
ses_C = obj_sessao.obtem_objeto("S-00000003")
assert not obj_sessao.de_administrador(ses_C)

# Teste de módulo comando_ver_grade_de_videos para sessão vazia
testa_processa("ses_None",  str, None, {})

# Teste de módulo comando_ver_grade_de_videos para sessão administrador
testa_processa("ses_A",  str, ses_A, {})

# Teste de módulo comando_ver_grade_de_videos para sessão comum
testa_processa("ses_C",  str, ses_C, {})

# Teste de módulo comando_ver_grade_de_videos para sessão inválida
testa_processa("ses_error", "AssertionError", 'error', {})

# Teste de módulo comando_ver_grade_de_videos para argumento que não é do tipo dicionário
testa_processa('ses_error_dict', "AssertionError", ses_C, {"bla, bla, bla"}) 

# Teste de módulo comando_ver_grade_de_videos para argumento diferente de vazio
testa_processa('ses_error_args', "AssertionError", ses_C, {"error": True}) 


if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
