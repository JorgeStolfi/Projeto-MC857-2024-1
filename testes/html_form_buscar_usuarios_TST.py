#! /usr/bin/python3
 
# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_elem_form_buscar_usuarios
import usuario
import identificador
import db_base_sql
import tabelas
import sessao
import compra
import util_testes
import comando_alterar_usuario

import sys

# Testes das funções de {html_elem_form}:

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_elem_form_buscar_usuarios
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

atrs = { 'nome': "Primeiro", 'documento': "Tamanho" }

admin = True
testa_gera("Valores_Admin", atrs, admin)

admin = False
testa_gera("Valores_Comum", atrs, admin)

atrs = {}

admin = True
testa_gera("Sem_Valores_Admin", atrs, admin)

admin = False
testa_gera("Sem_Valores_Comum", atrs, admin)

