#! /usr/bin/python3

import html_bloco_bemvindo
import obj_usuario
import obj_sessao

import db_base_sql
from util_erros import aviso_prog
import util_testes
import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
obj_usuario.cria_testes(True)
obj_sessao.cria_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = html_bloco_bemvindo
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
# Usuários para teste:
usrA = obj_usuario.obtem_objeto("U-00000001")
assert usrA != None
assert obj_usuario.eh_administrador(usrA)

usrC = obj_usuario.obtem_objeto("U-00000003")
assert usrC != None
assert not obj_usuario.eh_administrador(usrC)

for xusr, usr in ("N", None), ("A", usrA), ("C", usrC):
  rot_teste = f"usr{xusr}"
  testa_gera(rot_teste, str, usr)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
