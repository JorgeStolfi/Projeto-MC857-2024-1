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
  funcao = html_form_postar_alterar_comentario.gera
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

# Executa os testes de criação:
for ed_nota in False, True:
  xedn = "_ednota{str(ed_nota)[0]}"
  for ed_voto in False, True:
    xedv = "_edvoto{str(ed_voto)[0]}"
    rot_teste = "CR" + xedn + xedv
    testa_gera(rot_teste, str, None, comC1_atrs, ed_nota, ed_voto)

# Executa testes de alteração:
atrs_triv = comC1_atrs # Todos atributos sem alterar nada.
atrs_txto = { 'texto': "Alteradus", }
atrs_voto = { 'voto': (comC1_atrs['voto'] + 1) % 5, }
atrs_dic = { 'Nulo': {}, 'Triv': atrs_triv, 'Txto': atrs_txto, 'Voto': atrs_voto }
for atrs_tag, atrs in atrs_dic.items():
  xatr = f"_atrs{atrs_tag}"
  for ed_nota in False, True:
    xedn = "_ednota{str(ed_nota)[0]}"
    for ed_voto in False, True:
      xedv = "_edvoto{str(ed_voto)[0]}"
      rot_teste = "AL" + xatr + xedn + xedv
      testa_gera(rot_teste, str, comC1_id, atrs, ed_nota, ed_voto)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
