#! /usr/bin/python3

import html_form_postar_alterar_comentario
import obj_comentario
import obj_sessao
import util_identificador
import db_base_sql
import db_tabelas_do_sistema
import util_testes

import sys

from obj_comentario import obtem_atributos, obtem_identificador

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
  modulo = html_form_postar_alterar_comentario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Comentario:
comC1_id = "C-00000009"
comC1 = obj_comentario.obtem_objeto(comC1_id)
assert comC1 != None
comC1_atrs = obj_comentario.obtem_atributos(comC1)

# Form para criação:
rot_teste = "CR"
testa_gera(rot_teste, str, None, comC1_atrs)

# Form para alteração:
atrs_tot = obj_comentario.obtem_atributos(comC1)
atrs_som = { 'texto': "Alteradus", }
atrs_dic = { 'N': {}, 'T': atrs_tot, 'S': atrs_som, }
for atrs_tag, atrs in atrs_dic.items():
  xatr = f"_atr{atrs_tag}"
  rot_teste = "AL" + xatr
  testa_gera(rot_teste, str, comC1_id, atrs)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
