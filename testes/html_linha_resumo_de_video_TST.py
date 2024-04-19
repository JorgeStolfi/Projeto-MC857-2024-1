#! /usr/bin/python3

# Interfaces usadas por este script:

import html_linha_resumo_de_video
import db_base_sql
import db_tabelas_do_sistema
import obj_video
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_html_linha_resumo_de_video(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_linha_resumo_de_video
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

ids_videos = [
  "V-00000001",
  "V-00000002",
  "V-00000003",
  "V-00000004",
]

for vid_ident in ids_videos:
  vid = obj_video.busca_por_identificador(vid_ident)
  testa_html_linha_resumo_de_video(vid_ident, vid)

sys.stderr.write("Testes terminados normalmente.\n")