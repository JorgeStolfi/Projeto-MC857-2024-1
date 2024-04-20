#! /usr/bin/python3

import html_form_postar_comentario
import util_testes
import sys

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_form_postar_comentario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

comment1 = { 'autor': "autor1", 'video': "video1", 'pai': "pai1", "texto": "texto1" } 
comment2 = { 'autor': "autor2", 'video': "video2", 'pai': "pai2", "texto": "texto2" } 

testa_gera("postar_comentario_1", comment1)
testa_gera("postar_comentario_2", comment2)

sys.stderr.write("Testes terminados normalmente.\n")
