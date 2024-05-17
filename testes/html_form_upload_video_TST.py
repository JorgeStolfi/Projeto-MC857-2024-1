#! /usr/bin/python3

import html_form_upload_video
import obj_usuario
import util_identificador
import db_base_sql
import db_tabelas_do_sistema
import util_testes

import sys

from obj_usuario import obtem_atributos, obtem_identificador

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
  modulo = html_form_upload_video
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Testes das funções de {gera_html_elem_form}:
usr1_id = "U-00000003"
usr1 = obj_usuario.obtem_objeto(usr1_id)

atrs0 = { 'autor': usr1_id, }
atrs1 = { 'autor': usr1_id, 'titulo': "Bananas comendo macacos", }

for ed_nota in False, True:
  xednt = f"_ednt{str(ed_nota)[0]}"
  tag = xednt
  testa_gera("SemAtrs" + tag, str, atrs0, ed_nota)
  testa_gera("ComAtrs" + tag, str, atrs1, ed_nota)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
