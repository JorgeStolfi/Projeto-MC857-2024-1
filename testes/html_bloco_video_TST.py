#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import obj_usuario
import obj_video
import db_base_sql
import db_tabelas_do_sistema
import html_bloco_video
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
  modulo = html_bloco_video
  funcao = html_bloco_video.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Dados para teste:

# Video existente:
vid1_id = "V-00000001"
vid1 = obj_video.obtem_objeto(vid1_id)
assert vid1 != None
vid1_atrs = obj_video.obtem_atributos(vid1)

for bt_alterar in False, True:
  xedit = f"_edi{str(bt_alterar)[0]}"
  for bt_conversa in False, True:
    xconv = f"_conv{str(bt_conversa)[0]}"
    for bt_comentar in False, True:
      xcomt = f"_comt{str(bt_comentar)[0]}"
      for calcnota in False, True:
        xcalc = f"_calc{str(calcnota)[0]}"
        for bt_baixar in False, True:
          xbaixa = f"_calc{str(bt_baixar)[0]}"
          tag = xedit + xconv + xcomt + xcalc + xbaixa
        testa_gera("exist" + tag, str, vid1, bt_alterar, bt_conversa, bt_comentar, calcnota, bt_baixar)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
