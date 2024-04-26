#! /usr/bin/python3

import html_form_postar_comentario
import util_testes
import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_form_postar_comentario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

comment1 = { 'autor': "autor1", 'video': "video1", 'pai': "pai1", "texto": "texto1" } 
comment2 = { 'autor': "autor2", 'video': "video2", 'pai': "pai2", "texto": "texto2" } 

testa_gera("postar_comentario_1", str, comment1)
testa_gera("postar_comentario_2", str, comment2)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
