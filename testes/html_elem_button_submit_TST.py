#! /usr/bin/python3

import html_elem_button_submit
import util_testes
import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_elem_button_submit
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

dados= [ \
    ("C", "Cadastrar", 'cadastrar_usuario', None,                       '#55ee55', ),                            
    ("A", "Alterar",   'alterar_usuario',   {'usuario': "U-00000001"},  '#55ee55', ),    
    ("E", "Entrar",    'fazer_login',       None,                       '#55ee55', ),
  ]
  
for tag, texto, URL, cmd_args, cor_fundo in dados:
  testa_gera(tag, str, texto, URL, cmd_args, cor_fundo)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
