import sys

import db_base_sql
import html_bloco_lista_de_sessoes
import obj_sessao
import db_tabelas
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

sessoes = ["S-00000001", "S-00000002", "S-00000003"]

def testa_html_bloco_lista_de_sessoes(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = html_bloco_lista_de_sessoes
    funcao = modulo.gera
    frag = True     # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for ver in (False, True):
  for fechar in (False, True):
    tag = "ver" + str(ver)[0] + "-fechar" + str(fechar)[0] 
    testa_html_bloco_lista_de_sessoes("muitas-" + tag, sessoes, ver, fechar)
    testa_html_bloco_lista_de_sessoes("lhufas-" + tag, [], ver, fechar)
