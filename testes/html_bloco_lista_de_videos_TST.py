import sys

import db_base_sql
import html_bloco_lista_de_videos
import db_tabelas_do_sistema
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_bloco_lista_de_videos   
  funcao = modulo.gera
  frag = True     # Resultado é só um fragmento de página?
  pretty = False  # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

vid_ids = [
  "V-00000001",
  "V-00000002",
  "V-00000003",
  "V-00000004",
]

for mostra_autor in (False, True):
  for lista in [], vid_ids:
    xmaut = f"_maut{str(mostra_autor)[0]}"
    xlis = "_Sem" if len(lista) == 0 else "_Com"
    testa_gera("lista" + xmaut + xlis, str, lista, mostra_autor)
  
if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
