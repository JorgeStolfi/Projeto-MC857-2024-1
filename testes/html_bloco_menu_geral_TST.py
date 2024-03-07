#! /usr/bin/python3

import html_bloco_menu_geral
import util_testes; from util_testes import testa_gera_html

def testa(rotulo, *args):
  modulo = html_bloco_menu_geral
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("deslogado", False, None,            False)
testa("cliente",   True,  "José Primeiro", False)
testa("admin",     True,  "Geraldo Ente",  True)

