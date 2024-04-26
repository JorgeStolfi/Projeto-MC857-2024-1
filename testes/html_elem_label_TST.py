#! /usr/bin/python3

import html_elem_label 
import util_testes
import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_elem_label
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

testa_gera("1", str, "Banana", " --> ")

if ok_global:
  sys.stderr.write("Testes terminados normalmente.");
else:
  aviso_erro("Alguns testes falharam", True)
