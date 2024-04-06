#! /usr/bin/python3
 
# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_form_buscar_usuarios
import obj_usuario
import obj_sessao
import db_base_sql
import db_tabelas
import util_testes
import comando_alterar_usuario

import sys

# Testes das funções de {html_elem_form}:

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_buscar_usuarios
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

atrs = { 'autor': "Primeiro", 'documento': "Tamanho" }

admin = True
testa_gera("Valores_Admin", atrs, admin)

admin = False
testa_gera("Valores_Comum", atrs, admin)

atrs = {}

admin = True
testa_gera("Sem_Valores_Admin", atrs, admin)

admin = False
testa_gera("Sem_Valores_Comum", atrs, admin)

