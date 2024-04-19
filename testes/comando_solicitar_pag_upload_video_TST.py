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

# Uma sessão de administrador:
ses_A1 = obj_sessao.busca_por_identificador("S-00000001")
assery obj_sessao.de_administrador(ses_A1)

# Uma sessão de usuário comum:
ses_C1 = obj_sessao.busca_por_identificador("S-00000003")
assery not obj_sessao.de_administrador(ses_C1)

def testa_processa(rot_teste, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  modulo = comando_solicitar_pag_upload_video
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)

testa_processa("A1", ses_A1, {})
testa_processa("C1", ses_C1, {})

sys.stderr.write("Testes terminados normalmente.")
