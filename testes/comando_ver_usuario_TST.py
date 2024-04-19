#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import obj_sessao
import obj_video
import util_testes
from util_erros import erro_prog, aviso_prog, mostra
import comando_ver_objeto

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# ----------------------------------------------------------------------
# Função de teste:

def testa_comando_ver_usuario(rot_teste, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = comando_ver_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)

aviso_prog('!!! programa de teste do modulo {comando_ver_usuario} ainda nao foi escrito !!!', True)
