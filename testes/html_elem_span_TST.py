#! /usr/bin/python3

import html_elem_span
from util_testes import testa_modulo_html
import sys

def cria_linha(texto):
  """Cria uma linha de teste com {texto} dado."""
  t1 = html_elem_span.gera("font-family: 'Courier'; font-size: 30px", texto)
  t2 = html_elem_span.gera("font-family: 'Helvetica'; font-size: 20px; color: red", texto)
  t3 = html_elem_span.gera("font-family: 'Helvetica'; font-size: 20px; background-color: yellow", texto)
  linha = "<li>" + \
    "Lorem ipsum" + t1 + \
    "Gallia omnia" + t2 + \
    "Quousque tandem" + t3 + \
    "Pluribus unum" + \
    "</li>"
  return linha

def cria_pagina():
  linha1 = cria_linha("Potatoes")
  linha2 = cria_linha("One Two Three Four Five Six Seven Eight Nine Three Hundred Thousand and One Three Hundred Thousand and Two Three Hundred Thousand and Three Three Hundred Thousand and Four Three Hundred Thousand and Five Three Hundred Thousand and Six Three Hundred Thousand and Seven Three Hundred Thousand and Eight Three Hundred Thousand and Nine")
  pagina = "<ul>\n" + \
    linha1 + "\n" + \
    linha2 + "\n" + \
    "</ul>"
  return pagina

pag = cria_pagina()
testa_modulo_html(html_elem_span, "diversos", pag, True, False)
