import sys

import db_base_sql
import html_elem_link_text
import db_tabelas_do_sistema
import util_testes
from util_erros import aviso_prog

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
  modulo = html_elem_link_text   
  funcao = html_elem_link_text.gera
  frag = True     # Resultado é só um fragmento de página?
  pretty = False  # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

sys.stderr.write("  ** !!! O programa de testes ainda não foi escrito !!!\n")
ok_global = False
  
if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
