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

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_bloco_dados_de_comentario
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Testes com comentário existente:
com1_id = "C-00000001"
assert com1 != None
com1 = obj_comentario.busca_por_identificador(com1_id)
com1_atrs = obj_comentario.obtem_atributos(com1)

for edita_texto in False, True:
  tag = f"C1-exist-etit{str(edita_texto)[0])}"
  testa_gera(tag, com1_id, com1_atrs, edita_texto)

# Teste com comentário a criar:
com2_autor = obj_usuario.busca_por_identificador("U-00000002")
com2_video = obj_video.busca_por_identificador("V-00000002")
com2_pai = obj_comentario.busca_por_identificador("C-00000003")
com2_atrs_nul = { 'autor': com2_autor, 'video': com2_video, 'pai': com2_pai, }
com2_atrs_tit = com2_atrs_nul.copy()
com2_atrs_tit.update( { 'titulo': "Panacéia patética", } )

tag = f"V2-novo"
testa_gera(tag + "-aN", None, com2_atrs_nul, True)
testa_gera(tag + "-aT", None, com2_atrs_tit, True)

sys.stderr.write("Testes terminados normalmente.\n")
