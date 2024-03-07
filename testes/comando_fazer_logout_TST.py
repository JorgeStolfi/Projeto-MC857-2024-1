#! /usr/bin/python3

# Interfaces usadas por este script:

import comando_fazer_logout
import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_fazer_logout
  funcao = modulo.processa
  frag = False
  pretty = False
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None
assert obj_sessao.aberta(ses)

testa("A", ses, {})
