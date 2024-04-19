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

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_bloco_dados_de_video
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# fixtures
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# Testes com video existente:
vid1_id = "V-00000001"
assert vid1 != None
vid1 = obj_video.busca_por_identificador(vid1_id)
vid1_atrs = obj_video.obtem_atributos(vid1)

for mostra_arq in False, True:
  for edita_titulo in False, True:
    tag = f"V'-exist-marq{str(mostra_arq)[0])}-etit{str(edita_titulo)[0])}"
    testa_gera(tag, vid1_id, vid1_atrs, mostra_arq, edita_titulo)

# Teste com video a carregar:
vid2_autor = obj_usuario.busca_por_identificador("U-00000003")
vid2_atrs_nul = { 'autor': vid2_autor, }
vid2_atrs_tit = { 'autor': vid2_autor, 'titulo': "Panacéia patética", }

for mostra_arq in False, True:
  tag = f"V2-novo-marq{str(mostra_arq)[0])}"
  testa_gera(tag + "-aN", None, vid2_atrs_nul, mostra_arq, True)
  testa_gera(tag + "-aT", None, vid2_atrs_tit, mostra_arq, True)

sys.stderr.write("Testes terminados normalmente.\n")
