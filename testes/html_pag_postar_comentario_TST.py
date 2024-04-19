#! /usr/bin/python3

import html_pag_postar_comentario
import db_tabelas_do_sistema
import obj_sessao
import db_base_sql
import util_testes
from util_erros import aviso_prog

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_pag_postar_comentario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")

aviso_prog("!!! html_pag_postar_comentario_TST.py ainda não escrito !!!", True)
