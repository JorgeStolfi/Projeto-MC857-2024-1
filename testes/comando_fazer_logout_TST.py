#! /usr/bin/python3

# Interfaces usadas por este script:

import comando_fazer_logout
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

def testa_comando_fazer_logout(rotulo, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_fazer_logout
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *cmd_args)

ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None
assert obj_sessao.aberta(ses)

testa_comando_fazer_logout("A", ses, {})

sys.stderr.write("Testes terminados normalmente.\n")
