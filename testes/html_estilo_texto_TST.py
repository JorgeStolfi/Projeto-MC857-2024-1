#! /usr/bin/python3

import html_estilo_texto
import html_elem_span
import util_testes
import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_estilo_texto
  funcao = usa_estilo
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
def usa_estilo(tam_fonte, peso_fonte, cor_fundo, margens):
  """Retorna um fragmento HTML que é um texto arbitrário
  com os parâmetros de estilo indicados."""
  cor_texto = "#0044ff"
  estilo = html_estilo_texto.gera(tam_fonte, peso_fonte, cor_texto, cor_fundo, margens)
  ht_texto = html_elem_span.gera(estilo, "As barbas e os ladrões amaciados")
  return ht_texto

for tam_fonte in "32px", "12px":
  for peso_fonte in "bold", "medium":
    for cor_fundo in None, "#ffdd77":
      for margens in None, ("10px", "2em", "30px", "5em"):
        xfundo = str(cor_fundo)[1:] if cor_fundo != None else "None"
        xmarg = "N" if margens == None else "L"
        rot_teste = f"tam{tam_fonte}_peso{peso_fonte}_fundo{xfundo}_marg{xmarg}"
        testa_gera(rot_teste, str, tam_fonte, peso_fonte, cor_fundo, margens)
 
if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n");
else:
  aviso_prog("Alguns testes falharam.", True)
