#! /usr/bin/python3
import sys
import comando_buscar_sessoes_de_usuario
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# Sessão de usuário comum:

# Sessão de usuário administrador
ses4 = obj_sessao.busca_por_identificador("S-00000003")

# Usuário a examinar:

def testa_comando_buscar_sessoes_de_usuario(rot_teste, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = comando_buscar_sessoes_de_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)

# Sessão de usuário comum:
ses1 = obj_sessao.busca_por_identificador("S-00000004")
assert not obj_sessao.de_administrador(ses1)
usr1 = obj_sessao.obtem_usuario(ses1)
usr1_id = obj_usuario.obtem_identificador(usr1)
testa_comando_buscar_sessoes_de_usuario("teste1-N", ses1, {} )
testa_comando_buscar_sessoes_de_usuario("teste1-U", ses1, {'usuario': usr1_id } )

# Administrador olhando suas sessões:
ses2 = obj_sessao.busca_por_identificador("S-00000002")
assert obj_sessao.de_administrador(ses2)
usr2_id = "U-00000002"
testa_comando_buscar_sessoes_de_usuario("teste2-N", ses2, {} )
testa_comando_buscar_sessoes_de_usuario("teste2-U", ses2, {'usuario': usr2_id } )

sys.stderr.write("Testes terminados normalmente.\n")
