import comando_solicitar_pag_upload_video
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import obj_video
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = comando_solicitar_pag_upload_video
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Uma sessão de administrador:
ses_A1 = obj_sessao.obtem_objeto("S-00000001")
assert obj_sessao.de_administrador(ses_A1)

# Uma sessão de usuário comum:
ses_C1 = obj_sessao.obtem_objeto("S-00000003")
assert not obj_sessao.de_administrador(ses_C1)

testa_processa("A1",  str, ses_A1, {})
testa_processa("C1",  str, ses_C1, {})

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
