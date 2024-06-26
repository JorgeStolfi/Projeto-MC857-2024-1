import sys

import db_base_sql
import html_bloco_lista_de_sessoes
import obj_sessao
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
  modulo = html_bloco_lista_de_sessoes
  funcao = modulo.gera
  frag = True     # Resultado é só um fragmento de página?
  pretty = False  # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

sessoes = ["S-00000001", "S-00000002", "S-00000003"]

for ver in (False, True):
  for fechar in (False, True):
    for musr in False, True:
      tag = "_ver" + str(ver)[0] + "_fechar" + str(fechar)[0] + "_musr" + str(musr)[0] 
      testa_gera("muitas" + tag, str, sessoes, ver, fechar, musr)
      testa_gera("lhufas" + tag, str, [],      ver, fechar, musr)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.")
