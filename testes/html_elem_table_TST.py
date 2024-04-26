#! /usr/bin/python3

import html_bloco_erro
import html_elem_table
import html_elem_label
import html_elem_input
import html_elem_paragraph
import html_elem_button_simples
import util_testes

import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_elem_table
  funcao = cria_tabela
  frag = True  # Resultado é só um fragmento de página?
  pretty = False  # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

def cria_tabela():
  cabecalho=("Coluna 1", "Coluna 2")

  ht_val = [None]*3
  ht_val[0] = html_elem_input.gera("text", 'veiculo', "ident0", None, None, True, "Me edite!", None, False)
  ht_val[1] = html_elem_button_simples.gera("OK", 'pag_principal', None, '#55ee55')
  ht_val[2] = html_elem_paragraph.gera(None, "As armas e os barões assinalados<br/>Que da ocidental praia lusitana")

  linhas = [].copy()

  for i in range(3):
    ht_lab = html_elem_label.gera(f"Teste {i:03d}", ":")
    linhas.append((ht_lab, ht_val[i]))

  ht_tab = html_elem_table.gera(linhas, cabecalho)
  return ht_tab

testa_gera("Teste", str)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.");
else:
  aviso_erro("Alguns testes falharam", True)
