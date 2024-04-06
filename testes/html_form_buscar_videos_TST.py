#! /usr/bin/python3

# Interfaces usadas por este script:

import html_form_buscar_videos
import util_testes

import sys

# deve criar um formulario editavel se admin == True
def testa_form_editavel(rot_teste):
  

  # Cria formulário:
  ht_form = html_form_buscar_videos.gera({}, admin=True)
  
  frag = True
  pretty = False
  util_testes.escreve_resultado_html(html_form_buscar_videos, rot_teste, ht_form, frag, pretty)

# deve criar um formulario readonly se admin == False
def testa_form_readonly(rot_teste):
  
  # Cria formulário:
  ht_form = html_form_buscar_videos.gera({}, admin=False)
  
  frag = True
  pretty = False
  util_testes.escreve_resultado_html(html_form_buscar_videos, rot_teste, ht_form, frag, pretty)

# deve criar um formulario com os valores iniciais se o atrs nao for vazio
def testa_form_valores_iniciais(rot_teste):
  
  # Cria formulário:
  ht_form = html_form_buscar_videos.gera({'ID': 'V-111111', 'titulo': 'La la land', 'usr': 'José Primeiro', 'arq': 'la_la_land.mp4'}, admin=False)
  
  frag = True
  pretty = False
  util_testes.escreve_resultado_html(html_form_buscar_videos, rot_teste, ht_form, frag, pretty)

testa_form_editavel("form editavel")
testa_form_readonly("form readonly")
testa_form_valores_iniciais(" form com valores iniciais")
sys.stderr.write("Testes terminados normalmente.")