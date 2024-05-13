#! /usr/bin/python3

# Interfaces usadas por este script:

import html_linha_resumo_de_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
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
  modulo = html_linha_resumo_de_comentario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Um comentário sem pai:
com1_id = "C-00000001"
com1 = obj_comentario.obtem_objeto(com1_id)
assert obj_comentario.obtem_atributo(com1, 'pai') == None

# Um comentário com pai:
com2_id = "C-00000005"
com2 = obj_comentario.obtem_objeto(com2_id)
assert obj_comentario.obtem_atributo(com2, 'pai') != None

for ms_autor in False, True:
  for ms_video in False, True:
    for ms_pai in False, True:
      xargs = f"aut{str(ms_autor)[0]}_vid{str(ms_video)[0]}_pai{str(ms_pai)[0]}_"
      testa_gera(xargs + "C1",  list, com1, ms_autor, ms_video, ms_pai)
      testa_gera(xargs + "C2",  list, com2, ms_autor, ms_video, ms_pai)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
