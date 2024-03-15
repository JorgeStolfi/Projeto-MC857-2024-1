#! /usr/bin/python3

import html_elem_button_submit
import util_testes
import sys

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_elem_button_submit
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_gera("Cadastrar",        "Cadastrar", 'cadastrar_usuario', None, '#55ee55')

testa_gera("Alterar_usuario",  "Alterar", 'alterar_usuario', {'id_usr': "U-00000001"}, '#55ee55')

testa_gera("Entrar",           "Entrar", 'fazer_login', None, '#55ee55')

sys.stderr.write("Testes terminados normalmente.")
