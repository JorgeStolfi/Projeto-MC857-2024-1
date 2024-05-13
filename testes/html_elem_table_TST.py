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
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

def cria_tabela():
  val = [None]*3
  val[0] = html_elem_input.gera("text", 'veiculo', "ident0", None, None, True, "Me edite!", None, False)
  val[1] = html_elem_button_simples.gera("OK", 'pag_principal', None, '#55ee55')
  val[2] = html_elem_paragraph.gera(None, "As armas e os barões assinalados<br/>Que da ocidental praia lusitana")

  linhas = []
  ht_lab_cab = "<th style=\"background:green; padding: 10px 20px 30px 40px;\">" + "Coluna 1" + "</th>" 
  ht_val_cab = "<th>" + "Coluna 2" + "</th>" 
  cabecalhos = ( ht_lab_cab, ht_val_cab )
  linhas.append(cabecalhos)

  for i in range(3):
    ht_lab = "<td style=\"background:green;\">" + html_elem_label.gera(f"Teste {i:03d}", ":") + "</td>"
    ht_val = "<td style=\"font-size: 20px;\">" + val[i] + "</td>"
    linhas.append((ht_lab, ht_val))

  ht_tab = html_elem_table.gera(linhas)
  return ht_tab

testa_gera("Teste", str)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.");
else:
  aviso_prog("Alguns testes falharam", True)
