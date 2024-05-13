#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import obj_usuario
import obj_video
import db_base_sql
import db_tabelas_do_sistema
import html_bloco_dados_de_video
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
  modulo = html_bloco_dados_de_video
  funcao = modulo.gera
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

# Video a carregar:
vid2_autor = obj_usuario.obtem_objeto("U-00000003")
vid2_atrs_nul = { 'autor': vid2_autor, }
vid2_atrs_tit = { 'autor': vid2_autor, 'titulo': "Panacéia patética", }

for editavel in False, True:
  for para_admin in False, True:
    for para_proprio in False, True:
      tag = f"_edit{str(editavel)[0]}" + f"_admin{str(para_admin)[0]}" + f"_prop{str(para_proprio)[0]}"
      testa_gera("exist" + tag,       str, vid1_id, vid1_atrs,     editavel, para_admin, para_proprio)
      if editavel:
        testa_gera("novo_atrsN" + tag,  str, None,    vid2_atrs_nul, editavel, para_admin, para_proprio)
        testa_gera("novo_atrsT" + tag,  str, None,    vid2_atrs_tit, editavel, para_admin, para_proprio)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
