#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import util_testes; from util_testes import erro_prog, aviso_prog, mostra
import comando_ver_objeto

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Obtem uma sessao de um usuario que é de administrador:
ses1 = obj_sessao.busca_por_identificador("S-00000004")
assert obj_sessao.eh_administrador(ses1)

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def testa_comando_ver_objeto(rotulo, *cmd_args):
  """Testa {funcao(*cmd_args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_ver_objeto
  funcao = modulo.processa
  frag = False
  pretty = False
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *cmd_args)
  
for tag, id_obj in ( \
    ("U", "U-00000001"),
    ("S", "S-00000001"),
    ("V", "V-00000001"),
    ("invalid_class", "sthiuhtaiuhfa"),
    ("item_not_found", "U-aighdiuhfsdiuhdvsiu"),
    ("blank", ""),
  ):
  testa_comando_ver_objeto(tag, ses1, {'id_obj': id_obj})

# ----------------------------------------------------------------------
# Veredito final:
if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  erro_prog("- teste falhou")
