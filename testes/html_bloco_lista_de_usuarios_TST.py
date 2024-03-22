import sys

import db_base_sql
import html_bloco_lista_de_usuarios
import obj_sessao
import db_tabelas
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

ids_usuarios = [
  "U-00000001",
  "U-00000002",
  "U-00000003",
  "U-00000004",
  "U-00000005",
  "U-00000006",
  "U-00000007",
  "U-00000008",
  "U-00000009",
]

def testa_html_bloco_lista_de_usuarios(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = html_bloco_lista_de_usuarios
    funcao = modulo.gera
    frag = True     # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for ver in (False, True):
  for fechar in (False, True):
    tag = "ver" + str(ver)[0] + "-fechar" + str(fechar)[0] 
    testa_html_bloco_lista_de_usuarios("muitas-" + tag, ids_usuarios)
    testa_html_bloco_lista_de_usuarios("lhufas-" + tag, ids_usuarios)
