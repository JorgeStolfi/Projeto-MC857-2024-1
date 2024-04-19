#! /usr/bin/python3

import comando_solicitar_pag_cadastrar_usuario
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# Sessao de teste:
sessoes = [
  obj_sessao.busca_por_identificador("S-00000001"),
  obj_sessao.busca_por_identificador("S-00000002"),
  obj_sessao.busca_por_identificador("S-00000003")
]
assert sessoes != None

def testa_comando_solicitar_pag_cadastrar_usuario(rot_teste, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = comando_solicitar_pag_cadastrar_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)

for ses, rot_teste, atrs in ( 
    (sessoes[0], "N", None), 
    (sessoes[1], "V", []), 
    (None, "E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  testa_comando_solicitar_pag_cadastrar_usuario(rot_teste, ses, atrs)

sys.stderr.write("Testes terminados normalmente.\n")
