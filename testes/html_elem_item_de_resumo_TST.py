#! /usr/bin/python3

import html_elem_item_de_resumo
import util_testes

import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_elem_item_de_resumo
  funcao = usa_item
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
def usa_item(texto, cab, cor_fundo, alinha):
  """Converte um item numa tabela completa"""
  ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo, alinha)
  ht_linha_1 = f"<tr><td style=\"background: #77ffcc; text-align: {alinha}\" width=500px>Resultado de gera()</td></tr>"
  ht_linha_2 = f"<tr>{ht_item}</tr>"
  ht_tab = "<table>" + ht_linha_1 + ht_linha_2 + "</table>"
  return ht_tab

for cab, cor_fundo in (False, "#ffcc55"), (False, None), (True, None):
  for alinha in "left", "center", "right":
    rot_teste = f"cab{str(cab)[0]}_fundo{str(cor_fundo)}_{alinha}"
    texto = "Cabecalho" if cab else "Item itemoso"
    testa_gera(rot_teste, str, texto, cab, cor_fundo, alinha)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.");
else:
  aviso_prog("Alguns testes falharam", True)
