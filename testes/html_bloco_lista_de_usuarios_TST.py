import sys

import db_base_sql
import html_bloco_lista_de_usuarios
import obj_usuario
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
  modulo = html_bloco_lista_de_usuarios   
  funcao = modulo.gera
  frag = True     # Resultado é só um fragmento de página?
  pretty = False  # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

ids_usuarios = [
  "U-00000001",
  "U-00000002",
  "U-00000003",
  "U-00000004",
  "U-00000005",
  "U-00000006",
  "U-00000007",
  "U-00000008",
  "U-00000009",
]

testa_gera("muitos", str, True, ids_usuarios)
testa_gera("lhufos", str, True, ids_usuarios)
testa_gera("lhufos", str, False, ids_usuarios)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.")
