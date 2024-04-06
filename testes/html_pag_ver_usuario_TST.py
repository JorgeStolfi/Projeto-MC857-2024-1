#! /usr/bin/python3

from util_testes import erro_prog, aviso_prog
import html_pag_ver_usuario
import db_tabelas
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao de teste:
ses = obj_sessao.busca_por_identificador("S-00000004")
assert ses != None

# Usuario teste:
#usr1 = obj_sessao.obtem_usuario(ses)
usr1 = obj_usuario.busca_por_identificador("U-00000001")
assert usr1 != None
usr1_id = obj_usuario.obtem_identificador(usr1)
usr1_atrs = obj_usuario.obtem_atributos(usr1)

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_ver_usuario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Testes com erros em vários formatos:
for tag, erros in (
    ("N", None),
    ("V", []),
    ("E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  rotulo = tag
  testa_gera(rotulo, ses, usr1, erros)

sys.stderr.write("Testes terminados normalmente.\n")
