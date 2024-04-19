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
obj_usuario.inicializa_modulo(False)
obj_usuario.cria_testes(True)
obj_sessao.inicializa_modulo(False)
obj_sessao.cria_testes(True)
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_pag_mensagem_de_erro
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

for tag, erros in (
    ("N", None),
    ("V", []),
    ("1", "Você cometeu um erro, rapaz!"),
    ("2", "Você cometeu um erro, rapaz!\nE outro erro também!"),
    ("L", ["Você cometeu um erro, rapaz!", "E outro erro também!", "E mais um!"])
  ):
  rot_teste = tag
  testa_gera(rot_teste, ses, erros)

sys.stderr.write("Testes terminados normalmente.\n")
