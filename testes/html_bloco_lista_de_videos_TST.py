import sys

import db_base_sql
import html_bloco_lista_de_videos
import db_tabelas
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

ids_videos = [
  "V-00000001",
  "V-00000002",
  "V-00000003",
  "V-00000004",
]

def testa_html_bloco_lista_de_videos(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_bloco_lista_de_videos   
  funcao = modulo.gera
  frag = True     # Resultado é só um fragmento de página?
  pretty = False  # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for ver in (False, True):
  tag = "ver" + str(ver)[0] 
  testa_html_bloco_lista_de_videos("ComVideos-" + tag, ids_videos)
  testa_html_bloco_lista_de_videos("SemVideos-" + tag, ())
  
sys.stderr.write("Testes terminados normalmente.\n")
