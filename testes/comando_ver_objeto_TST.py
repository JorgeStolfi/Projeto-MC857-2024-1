#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes
from util_erros import erro_prog, aviso_prog, mostra
import comando_ver_objeto

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  
  global ok_global
  modulo = comando_ver_objeto
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Obtem uma sessao de um usuario que é de administrador:
ses1 = obj_sessao.obtem_objeto("S-00000001")
assert obj_sessao.de_administrador(ses1)

for tag, id_obj in ( \
    ("U", "U-00000001"),
    ("S", "S-00000001"),
    ("V", "V-00000001"),
    ("C", "C-00000001"),
    ("invalid_class", "N-00000001"),
    ("item_not_found", "U-12345678"),
    ("blank", ""),
  ):
  testa_processa(tag,  str, ses1, {'objeto': id_obj})

# ----------------------------------------------------------------------
# Veredito final:
if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
