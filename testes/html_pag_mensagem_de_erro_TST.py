#! /usr/bin/python3

import db_tabelas
import obj_sessao
import db_base_sql
import util_testes
import obj_usuario
import html_pag_mensagem_de_erro

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None
obj_usuario.inicializa_modulo(False)
obj_usuario.cria_testes(True)
obj_sessao.inicializa_modulo(False)
obj_sessao.cria_testes(True)
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_mensagem_de_erro
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for tag, erros in (
    ("N", None),
    ("V", []),
    ("1", "Você cometeu um erro, rapaz!"),
    ("2", "Você cometeu um erro, rapaz!\nE outro erro também!"),
    ("L", ["Você cometeu um erro, rapaz!", "E outro erro também!", "E mais um!"])
  ):
  rotulo = tag
  testa_gera(rotulo, ses, erros)

sys.stderr.write("Testes terminados normalmente.\n")
