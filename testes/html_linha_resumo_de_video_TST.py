#! /usr/bin/python3

# Interfaces usadas por este script:

import html_linha_resumo_de_video
import db_base_sql
import db_tabelas_do_sistema
import obj_video
import obj_sessao #####
import util_testes
from util_erros import aviso_prog


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
  modulo = html_linha_resumo_de_video
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# sessão de admin
ses1 = obj_sessao.obtem_objeto("S-00000001")

vid_ids = [
  "V-00000001",
  "V-00000002",
]

for vid_id in vid_ids:
  for mostra_autor in False, True:
    vid = obj_video.obtem_objeto(vid_id)
    tag = f"_{vid_id}" + f"_autor{str(mostra_autor)[0]}"
    testa_gera("res" + tag, list, vid, mostra_autor)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
