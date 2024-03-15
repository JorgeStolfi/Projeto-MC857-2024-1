#! /usr/bin/python3

import html_bloco_menu_geral
import util_testes
import sys

def testa_html_bloco_menu_geral(rotulo, *args):
  modulo = html_bloco_menu_geral
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_html_bloco_menu_geral("deslogado", False, None,            False)
testa_html_bloco_menu_geral("comum",     True,  "José Primeiro", False)
testa_html_bloco_menu_geral("admin",     True,  "Geraldo Ente",  True)

sys.stderr.write("Testes terminados normalmente.\n")
