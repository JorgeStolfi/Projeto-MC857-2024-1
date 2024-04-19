#! /usr/bin/python3

import html_estilo_cabecalho_de_tabela
import util_testes
import sys

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_estilo_cabecalho_de_tabela
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

testa_gera("1")

sys.stderr.write("Testes terminados normalmente");
