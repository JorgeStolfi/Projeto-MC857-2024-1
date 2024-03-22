#! /usr/bin/python3

import html_pag_ver_video
import db_base_sql
import util_testes
import db_tabelas
import obj_sessao
import obj_video
import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao do admin
ses1 = obj_sessao.busca_por_identificador("S-00000001")

# Video de teste:
vid1 = obj_video.busca_por_identificador("V-00000002")

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_ver_video
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_gera("V-E0", ses1, vid1, None)
testa_gera("V-E2", ses1, vid1, ["Veja a mensagem abaixo", "Veja a mensagem acima"])
