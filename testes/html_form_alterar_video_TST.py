#! /usr/bin/python3

import html_form_alterar_video
import obj_video
import obj_sessao
import util_identificador
import db_base_sql
import db_tabelas_do_sistema
import util_testes

import sys

from obj_video import obtem_atributos, obtem_identificador

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
  modulo = html_form_alterar_video
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Video:
vidC1_id = "V-00000002"
vidC1 = obj_video.obtem_objeto(vidC1_id)
assert vidC1 != None

atrs_tot = obj_video.obtem_atributos(vidC1)
atrs_som = { 'titulo': "Alteradus", }
atrs_dic = { 'N': {}, 'T': atrs_tot, 'S': atrs_som, }

for para_admin in False, True:
  for at, atrs in atrs_dic.items():
    xpadm = f"_admin{str(para_admin)[0]}"
    xatrs = f"_atrs{at}"
    rot_teste = "AV" + xpadm + xatrs
    testa_gera(rot_teste, str, vidC1_id, atrs, para_admin)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
