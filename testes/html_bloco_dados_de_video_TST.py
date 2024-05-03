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
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# fixtures

# Testes com video existente:
vid1_id = "V-00000001"
vid1 = obj_video.obtem_objeto(vid1_id)
assert vid1 != None
vid1_atrs = obj_video.obtem_atributos(vid1)

for edita_titulo in False, True:
  tag = f"V'-exist-etit{str(edita_titulo)[0]}"
  testa_gera(tag, str, vid1_id, vid1_atrs, edita_titulo)

# Teste com video a carregar:
vid2_autor = obj_usuario.obtem_objeto("U-00000003")
vid2_atrs_nul = { 'autor': vid2_autor, }
vid2_atrs_tit = { 'autor': vid2_autor, 'titulo': "Panacéia patética", }

tag = f"V2-novo"
testa_gera(tag + "-aN",  str, None, vid2_atrs_nul, True)
testa_gera(tag + "-aT",  str, None, vid2_atrs_tit, True)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
