import comando_solicitar_pag_upload_video
import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import obj_video
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

ses1 = obj_sessao.busca_por_identificador("S-00000001")
cmd_args1 = {'coisa': True}

def testa_processa(rotulo, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_solicitar_pag_upload_video
  funcao = modulo.processa
  frag = False
  pretty = False
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *cmd_args)

testa_processa("T1", ses1, cmd_args1)

sys.stderr.write("Testes terminados normalmente.")
