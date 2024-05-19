#! /usr/bin/python3

import html_estilo_div_dados
import html_elem_span
import util_testes
import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_estilo_div_dados
  funcao = usa_estilo
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
def usa_estilo(display, width, word_wrap, padding, line_height):
  """Retorna um fragmento HTML que é um texto arbitrário
  com os parâmetros de estilo indicados."""

  estilo = html_estilo_div_dados.gera(display, width, word_wrap, padding, line_height)
  ht_texto = html_elem_span.gera(estilo, "As barbas e os ladrões amaciados")
  return ht_texto

for display in ["block"]:
  for width in ["100%", "5%"]:
    for word_wrap in ["break-word"]:
      for padding in [( "10px", "0px", "5px", "0px" )]:
        for line_height in ["100%", "90%"]:
          xpadding= "N" if padding == None else "L"
          rot_teste = f"display{display}_width{width}_word_wrap{word_wrap}_marg{xpadding}_line_height{line_height}"
          testa_gera(rot_teste, str, display, width, word_wrap, padding, line_height)
 
if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n");
else:
  aviso_prog("Alguns testes falharam.", True)
