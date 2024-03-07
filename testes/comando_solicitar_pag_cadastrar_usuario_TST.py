#! /usr/bin/python3

import comando_solicitar_pag_cadastrar_usuario
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

# Sessao de teste:
sessoes = [
  obj_sessao.busca_por_identificador("S-00000001"),
  obj_sessao.busca_por_identificador("S-00000002"),
  obj_sessao.busca_por_identificador("S-00000003")
]
assert sessoes != None

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = comando_solicitar_pag_cadastrar_usuario
  funcao = modulo.processa
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for ses, rotulo, atrs in ( 
    (sessoes[0], "N", None), 
    (sessoes[1], "V", []), 
    (None, "E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  testa(rotulo, ses, atrs)
