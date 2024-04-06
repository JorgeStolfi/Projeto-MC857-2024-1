#! /usr/bin/python3

# Interfaces usadas por este script:

import html_elem_form
import html_elem_label
import html_elem_input
import html_elem_table
import html_elem_button_submit
import util_testes

import sys

def testa_form_simples(rot_teste, modulo, rotulo, tipo, nome, val_ini, val_min, editavel, dica, cmd, obrigatorio):
  """Testa {html_elem_form.gera} com um formulário consistindo de um único
  campo texto e um botão "submit":"""

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_elem_table.gera(linhas, ["TIPO", "ELEMENTO"])

  # Cria botao de interacao com o ht_form
  ht_botao = html_elem_button_submit.gera("Botao", 'urltest', None, '#55ee55', obrigatorio)

  # Counteudo do formulário:
  ht_campos = \
    ht_table + \
    ht_botao

  # Cria formulário:
  ht_form = html_elem_form.gera(ht_campos)
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.escreve_resultado_html(html_elem_form, "completo", ht_form, frag, pretty)
  
  # cria campo de texto com valor inicial
  ht_rotulo = html_elem_label.gera("campo de texto", ": ")
  ht_campo = html_elem_input.gera(None, "text", "texto1", "blabla", None, True, None, None, False)

  # cria campo de texto sem valor inicial, com dica
  ht_rotulo = html_elem_label.gera("campo de texto", ": ")
  ht_campo = html_elem_input.gera(None, "text", "texto2", None, None, True, "Lorem ipusm", None, False)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo de senha
  ht_rotulo = html_elem_label.gera("campo de senha", ": ")
  ht_campo = html_elem_input.gera(None, "password", "senha", None, None, True, None, None, False)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo numerico
  ht_rotulo = html_elem_label.gera("campo numerico", ": ")
  ht_campo = html_elem_input.gera(None, "number", "pernas", "17", "5", True, None, None, False)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo escondido
  ht_rotulo = html_elem_label.gera("campo escondido", ": ")
  ht_campo = html_elem_input.gera(None, "hidden", "segredo", "boo", None, True, None, None, False)
  linhas.append((ht_rotulo, ht_campo,))

def testa_form_tabela(rot_teste):
  linhas = [].copy()
  
  # cria campo de texto com valor inicial
  ht_rotulo = html_elem_label.gera("campo de texto", ": ")
  ht_campo = html_elem_input.gera(None, "text", "texto1", "blabla", None, True, None, None, False)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo de texto sem valor inicial, com dica
  ht_rotulo = html_elem_label.gera("campo de texto", ": ")
  ht_campo = html_elem_input.gera(None, "text", "texto2", None, None, True, "Lorem ipusm", None, False)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo de senha
  ht_rotulo = html_elem_label.gera("campo de senha", ": ")
  ht_campo = html_elem_input.gera(None, "password", "senha", None, None, True, None, None, False)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo numerico
  ht_rotulo = html_elem_label.gera("campo numerico", ": ")
  ht_campo = html_elem_input.gera(None, "number", "pernas", "17", "5", True, None, None, False)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo escondido
  ht_rotulo = html_elem_label.gera("campo escondido", ": ")
  ht_campo = html_elem_input.gera(None, "hidden", "segredo", "boo", None, True, None, None, False)
  linhas.append((ht_rotulo, ht_campo,))

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_elem_table.gera(linhas, ["TIPO", "ELEMENTO"])

  # Cria botao de interacao com o ht_form
  ht_botao = html_elem_button_submit.gera("Botao", 'url test', None, '#55ee55')

  # Counteudo do formulário:
  ht_campos = \
    ht_table + \
    ht_botao

  # Cria formulário:
  ht_form = html_elem_form.gera(ht_campos)
  
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.escreve_resultado_html(html_elem_form, rot_teste, ht_form, frag, pretty)

testa_form_tabela("tabela")

sys.stderr.write("Testes terminados normalmente.")
