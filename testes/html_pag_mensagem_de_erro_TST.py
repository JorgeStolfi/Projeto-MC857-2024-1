#! /usr/bin/python3

import db_tabelas_do_sistema
import obj_sessao
import db_base_sql
import util_testes
import obj_usuario
import html_pag_mensagem_de_erro

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

obj_usuario.inicializa_modulo(True)
obj_usuario.cria_testes(True)
obj_sessao.inicializa_modulo(True)
obj_sessao.cria_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_pag_mensagem_de_erro
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

ses = obj_sessao.obtem_objeto("S-00000001")
assert ses != None

for tag, erros in (
    ("STR", "Você cometeu um erro, rapaz!"),
    ("STR-NL", "Você cometeu um erro, rapaz!\nE outro erro também!"),
    ("LIST-3", ["Você cometeu um erro, rapaz!", "E outro erro também!", "E mais um!"])
  ):
  rot_teste = tag
  testa_gera(rot_teste,  str, ses, erros)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
