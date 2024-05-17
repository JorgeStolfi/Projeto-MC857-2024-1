#! /usr/bin/python3

import html_bloco_rodape
import util_testes
from util_erros import aviso_prog
import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_bloco_rodape
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

testa_gera("R", str)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n");
else:
  aviso_prog("Alguns testes falharam.", True)
