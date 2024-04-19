#! /usr/bin/python3

import comando_fechar_sessao
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_comando_fechar_sessao(rot_teste, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  modulo = comando_fechar_sessao
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)
  
id_ses1 = "S-00000001" # Sessao do usuário fechador.
ses1 = obj_sessao.busca_por_identificador(id_ses1)
assert ses1 != None
assert obj_sessao.aberta(ses1)

for rot_teste, ses, cmd_args in [ \
    # ('inexistente',          ses1,    {'sessoa' : ''}) Não está implementado um tratamento para sessão inexistente
    ('existente',  ses1,    {'sessao' : 'S-00000002'}),
    ('proprio',    ses1,    {'sessao' : 'S-00000001'}),
    ('fechada',    ses1,    {'sessao' : 'S-00000003'})
  ]:
  testa_comando_fechar_sessao(rot_teste, ses, cmd_args)

sys.stderr.write("Testes terminados normalmente.\n")
