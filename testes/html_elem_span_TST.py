#! /usr/bin/python3

import html_elem_span
import util_testes 
from util_testes import escreve_resultado_html
import sys

ok_global = True

def cria_pagina():
  """Cria uma página com uma lista "<ul>...</ul>", cada entrada
  da qual contém vários elementos "<span>...</span>"."""
  linha1 = cria_linha("Potatoes")
  linha2 = cria_linha( \
    "One Two Three Four Five Six Seven Eight Nine Three Hundred Thousand and One " + \
    "Three Hundred Thousand and Two Three Hundred Thousand and Three " + \
    "Three Hundred Thousand and Four Three Hundred Thousand and Five " + \
    "Three Hundred Thousand and Six Three Hundred Thousand and Seven " + \
    "Three Hundred Thousand and Eight Three Hundred Thousand and Nine")
  pagina = "<ul>\n" + \
    linha1 + "\n" + \
    linha2 + "\n" + \
    "</ul>"
  return pagina

def cria_linha(texto):
  """Cria um item "<li>...</li>" com vários elementos "<span>...</span>", cada qual
  contendo o {texto} dado em estilos diferentes."""
  t1 = html_elem_span.gera("font-family: 'Courier'; font-size: 30px", texto)
  t2 = html_elem_span.gera("font-family: 'Helvetica'; font-size: 20px; color: red", texto)
  t3 = html_elem_span.gera("font-family: 'Helvetica'; font-size: 20px; background-color: yellow", texto)
  linha = "<li>" + \
    "Lorem ipsum: [" + t1 + "]" \
    "Gallia omnia: [" + t2 + "]" + \
    "Quousque tandem: [" + t3 + "]" \
    "</li>"
  return linha
  
def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  
  modulo = html_elem_span
  funcao = cria_pagina
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

testa_gera("T1", str)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.");
else:
  aviso_prog("Alguns testes falharam", True)
