#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import obj_sessao
import obj_video
import util_testes
from util_erros import erro_prog, aviso_prog, mostra
import comando_ver_video

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
  modulo = comando_ver_video
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok


# Obtem uma sessao de um usuario que é de administrador:
ses1 = obj_sessao.busca_por_identificador("S-00000001")
assert obj_sessao.de_administrador(ses1)

for id_vid in (
    "V-00000001",
    "V-00000002",
    "V-00000003",
    "V-00000004",
  ):
  testa_processa(ses1, {'video': id_vid})

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  erro_prog("Alguns testes falharam")
