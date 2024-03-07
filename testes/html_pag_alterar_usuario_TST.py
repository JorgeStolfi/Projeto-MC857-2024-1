#! /usr/bin/env python3

import html_pag_alterar_usuario
import db_tabelas
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao de teste usuario 1:
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

# Usuario teste 1 (nao administrador):
usr1 = obj_sessao.obtem_usuario(ses)
assert usr1 != None
usr1_id = obj_usuario.obtem_identificador(usr1)
usr1_atrs = obj_usuario.obtem_atributos(usr1)

# Sessao de teste usuario 2:
ses = obj_sessao.busca_por_identificador("S-00000004")
assert ses != None

# Usuario teste 2 (administrador):
usr2 = obj_sessao.obtem_usuario(ses)
assert usr2 != None
usr2_id = obj_usuario.obtem_identificador(usr2)
usr2_atrs = obj_usuario.obtem_atributos(usr2)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_alterar_usuario
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = True # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for admin in (False, True):
  ad = "-adm"+str(admin)
  for tag, erros in (
      ("N"+ad, None),
      ("V"+ad, []),
      ("B"+ad, "Mensagem UM\nMensagem DOIS\nMensagem TRÊS"),
      ("L"+ad, ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
      ("LB"+ad, ["Mensagem UM-A\nMensagem UM-B", "Mensagem DOIS", "Mensagem TRÊS",]),
    ):
    rotulo = tag
    testa(rotulo, ses, usr1_id, usr1_atrs, admin, erros)
