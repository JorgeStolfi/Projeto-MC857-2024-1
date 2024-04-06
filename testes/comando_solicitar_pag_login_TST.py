import comando_solicitar_pag_login
import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

ses1 = obj_sessao.busca_por_identificador("S-00000001")
cmd_args1 = {'coisa': True}

def testa_comando_solicitar_pag_login(rotulo, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_solicitar_pag_login
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *cmd_args)

testa_comando_solicitar_pag_login("T1", ses1, cmd_args1)

sys.stderr.write("Testes terminados normalmente.\n")
