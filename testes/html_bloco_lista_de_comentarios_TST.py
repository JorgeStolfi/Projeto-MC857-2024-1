import sys

import db_base_sql
import html_bloco_lista_de_comentarios
import obj_comentario
import db_tabelas_do_sistema
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ids_comentarios = [
  "C-00000001",
  "C-00000002",
  "C-00000003",
  "C-00000004",
  "C-00000005",
  "C-00000006",
]

def testa_html_bloco_lista_de_comentarios(rot_teste, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

    modulo = html_bloco_lista_de_comentarios   
    funcao = modulo.gera
    frag = True     # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)


for ver in (False, True):
  tag = "ver" + str(ver)[0]
  testa_html_bloco_lista_de_comentarios("muitas-" + tag, ids_comentarios, ver, ver)
  testa_html_bloco_lista_de_comentarios("lhufas-" + tag, [], ver, ver)
