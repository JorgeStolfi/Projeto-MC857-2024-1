#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import obj_usuario
import obj_video
import db_base_sql
import db_tabelas
import html_bloco_dados_de_video
import util_testes

import sys

def testa_html_bloco_dados_de_video(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_bloco_dados_de_video
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# fixtures
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Teste com video existente:
vid1 = obj_video.busca_por_identificador("V-00000001")
vid1_usr = obj_video.obtem_usuario(vid1)
assert vid1 != None
testa_html_bloco_dados_de_video("V1-exist-muF-etF", vid1, vid1_usr, False, False)
testa_html_bloco_dados_de_video("V1-exist-muF-etT", vid1, vid1_usr, False, True )
testa_html_bloco_dados_de_video("V1-exist-muT-etF", vid1, vid1_usr, True,  False)
testa_html_bloco_dados_de_video("V1-exist-muT-etT", vid1, vid1_usr, True,  True )

# Teste com video a carregar:
vid2 = None
vid2_usr = obj_usuario.busca_por_identificador("U-00000003")
assert not obj_usuario.obtem_atributo(vid2_usr, 'administrador')
assert vid2_usr != None
testa_html_bloco_dados_de_video("V2-novo", vid2, vid2_usr, False, False)

sys.stderr.write("Testes terminados normalmente.\n")
