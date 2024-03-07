#! /usr/bin/python3

# Interfaces usadas por este script:

import html_bloco_resumo_de_usuario
import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_bloco_resumo_de_usuario
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

usr1_ident = "U-00000001"
usr1 = obj_usuario.busca_por_identificador(usr1_ident)
usr2_ident = "U-00000002"
usr5_ident = "U-00000005"

testa("N",  usr1)

