#! /usr/bin/python3

import html_elem_button_submit
import util_testes
import sys

def testa_html_elem_button_submit_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_elem_button_submit
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

dados= [ \
    ("C", "Cadastrar", 'cadastrar_usuario', None,                         '#55ee55'),                            
    ("A", "Alterar",   'alterar_usuario',   {'id_usuario': "U-00000001"}, '#55ee55'),    
    ("E", "Entrar",    'fazer_login',       None,                         '#55ee55'),
  ]
  
for tag, texto, URL, cmd_args, cor_fundo in dados:
  testa_html_elem_button_submit_gera(tag, texto, URL, cmd_args, cor_fundo)

sys.stderr.write("Testes terminados normalmente.")
