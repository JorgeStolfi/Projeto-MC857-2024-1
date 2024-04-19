#! /usr/bin/python3

import html_pag_upload_video
import db_tabelas_do_sistema
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_pag_upload_video
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")

args1 = \
  { 'arq':     "foguete.mp4",
    'titulo':  "Lançamento do foguete subterrâneo da NASA",
  }

for tag, erros in (
    ("N", None),
    ("V", []),
    ("E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  testa_gera("ComValores-err" + tag, ses, args1, erros)
  testa_gera("SemValores-err" + tag, ses, {},    erros)
