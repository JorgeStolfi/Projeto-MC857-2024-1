#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.


import html_bloco_dados_de_usuario
import obj_usuario
import db_base_sql
import db_tabelas
import util_testes
import util_identificador

import sys

from obj_usuario import obtem_atributos, obtem_identificador

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_bloco_dados_de_usuario
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# fixtures
sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Testes das funções de {gera_html_elem_form}:
usr1 = obj_usuario.busca_por_identificador("U-00000001")
assert usr1 != None
testa("N", obtem_identificador(usr1), obtem_atributos(usr1), None)
