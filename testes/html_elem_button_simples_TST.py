#! /usr/bin/python3

import html_elem_button_simples
import util_testes

import sys

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_elem_button_simples
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_gera("Principal", "Principal", 'principal', None, '#60a3bc')

testa_gera("Entrar",    "Entrar", 'solicitar_pag_login', None, '#55ee55')

testa_gera("Sair",      "Sair", 'fazer_logout', None, '#60a3bc')

testa_gera("simples_Cadastrar", "Cadastrar", 'solicitar_pag_cadastrar_usuario', None, '#60a3bc')

testa_gera("simples_OK",        "OK", 'principal', None, '#55ee55')

sys.stderr.write("Testes terminadso normalmente.")
