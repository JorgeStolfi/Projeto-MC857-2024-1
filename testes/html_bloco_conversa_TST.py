???
#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import html_bloco_dados_de_comentario
import obj_sessao
import obj_usuario
import obj_video
import obj_comentario
import db_base_sql
import db_tabelas_do_sistema
import util_testes
import util_identificador

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
  modulo = html_bloco_dados_de_comentario
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Testes com comentário existente:
com1_id = "C-00000001"
com1 = obj_comentario.obtem_objeto(com1_id)
assert com1 != None
com1_atrs = obj_comentario.obtem_atributos(com1)

# Teste com comentário a existente
for edita_texto in False, True:
  tag = f"C1-exist-edtit{str(edita_texto)[0]}"
  testa_gera(tag, str, com1_id, com1_atrs, edita_texto)

# Teste com comentário a criar, título em branco:
com2_autor = obj_usuario.obtem_objeto("U-00000002")
com2_video = obj_video.obtem_objeto("V-00000002")
com2_pai = obj_comentario.obtem_objeto("C-00000003")
com2_atrs_nul = { 'autor': com2_autor, 'video': com2_video, 'pai': com2_pai, }
tag = f"V2-novo"
testa_gera(tag + "-aN",  str, None, com2_atrs_nul, True)

# Teste com comentário a criar, título previamente fornecido:
com2_atrs_tit = com2_atrs_nul.copy()
com2_atrs_tit.update( { 'titulo': "Panacéia patética", } )
testa_gera(tag + "-aT",  str, None, com2_atrs_tit, True)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
