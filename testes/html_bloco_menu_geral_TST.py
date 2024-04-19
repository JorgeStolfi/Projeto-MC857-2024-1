#! /usr/bin/python3

import html_bloco_menu_geral
import util_testes
import sys

def testa_html_bloco_menu_geral(rot_teste, *args):
  modulo = html_bloco_menu_geral
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

testa_html_bloco_menu_geral("deslogado", False, None,            False)
testa_html_bloco_menu_geral("comum",     True,  "José Primeiro", False)
testa_html_bloco_menu_geral("admin",     True,  "Geraldo Ente",  True)

sys.stderr.write("Testes terminados normalmente.\n")
