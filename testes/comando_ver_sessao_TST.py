#! /usr/bin/python3
import sys
import comando_ver_sessao
import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Usuário a examinar: 

def testa_comando_ver_sessao(rotulo, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_ver_sessao
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *cmd_args)

id_ses = "S-00000001"
ses1 = obj_sessao.busca_por_identificador(id_ses)

# Sessão de usuário comum:
testa_comando_ver_sessao("uso_comum", ses1, {'id_ses': 'S-00000001'})  

# Cliente tentando acessar sessão que não e dele:
testa_comando_ver_sessao("acesso_invalido", ses1, {'id_ses': 'S-00000003'})  

# Chamada sem argumentos
testa_comando_ver_sessao("sem_argumento", ses1, {})  

sys.stderr.write("Testes terminados normalmente.\n")
 
