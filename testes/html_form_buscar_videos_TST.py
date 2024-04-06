#! /usr/bin/python3

# Interfaces usadas por este script:

import html_form_buscar_videos
import util_testes

import sys

# deve criar um formulario editavel se admin == True
def testa_form_editavel_admin_true(rot_teste):
  

  # Cria formulário:
  ht_form = html_form_buscar_videos.gera({}, True)
  
  frag = True
  pretty = False
  util_testes.escreve_resultado_html(html_form_buscar_videos, rot_teste, ht_form, frag, pretty)

# deve criar um formulario editavel se admin == False
def testa_form_editavel_admin_false(rot_teste):
  
  # Cria formulário:
  ht_form = html_form_buscar_videos.gera({}, False)
  
  frag = True
  pretty = False
  util_testes.escreve_resultado_html(html_form_buscar_videos, rot_teste, ht_form, frag, pretty)

# deve criar um formulario com os valores iniciais se o atrs nao for vazio
def testa_form_valores_iniciais(rot_teste):
  
  # Cria formulário:
  ht_form = html_form_buscar_videos.gera({'id_video': 'V-111111', 'titulo': 'La la land', 'usr': 'José Primeiro', 'arq': 'la_la_land.mp4'}, False)
  
  frag = True
  pretty = False
  util_testes.escreve_resultado_html(html_form_buscar_videos, rot_teste, ht_form, frag, pretty)

testa_form_editavel_admin_true("form_editavel_admin_true")
testa_form_editavel_admin_false("form_editavel_admin_false")
testa_form_valores_iniciais(" form_com_valores_iniciais")
sys.stderr.write("Testes terminados normalmente.")