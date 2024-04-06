#! /usr/bin/python3

import html_bloco_erro
import html_elem_table
import html_elem_label
import html_elem_input
import html_elem_paragraph
import html_elem_button_simples
import util_testes

import sys

def testa_html_table_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_elem_table
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False  # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

linhas = [].copy()

erro_de_teste_html = html_bloco_erro.gera("Houston, we've got a problem. Nevermind, this is just a Test!")

cabecalho=("Coluna 1", "Coluna 2")
for i in range(3):
  ht_lab = html_elem_label.gera(f"Teste {i:03d}", ":")
  if i == 0:
    ht_val = html_elem_input.gera(None, "text", f"input_{i:03d}", None, None, True, "Me edite!", None, False)
  elif i == 1:
    ht_val = html_elem_button_simples.gera("OK", 'pag_principal', None, '#55ee55')
  elif i == 2:
    ht_val = html_elem_paragraph.gera(None, "As armas e os barões assinalados<br/>Que da ocidental praia lusitana")

  linhas.append((ht_lab, ht_val))

testa_html_table_gera("Teste", linhas, cabecalho)

sys.stderr.write("Testes terminados normalmente.");
