#! /usr/bin/python3

import html_estilo_titulo
import html_elem_span
import util_testes
import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_estilo_titulo
  funcao = usa_estilo
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
def usa_estilo(cor_texto):
  """Retorna um fragmento HTML que é um titulo arbitrário
  com os parâmetros de estilo indicados."""
  estilo = html_estilo_titulo.gera(cor_texto)
  ht_titulo = html_elem_span.gera(estilo, "Coisas que Todo Feiticeiro Precisa Saber:")
  return ht_titulo

for cor_texto in "#0044ff", "#dd2200":
  rot_teste = f"cor{cor_texto[1:]}"
  testa_gera(rot_teste, str, cor_texto)

if ok_global:
  sys.stderr.write("Testes terminados normalmente");
else:
  aviso_erro("Alguns testes falharam", True)
