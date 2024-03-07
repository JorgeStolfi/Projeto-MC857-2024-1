#! /usr/bin/python3

# Interfaces usadas por este script:

import html_elem_form
import html_elem_label
import html_elem_input
import html_elem_table
import html_elem_button_submit
from util_testes import testa_modulo_html

import sys

def cria_form_completo():
  linhas = [].copy()
  
  # cria campo de texto com valor inicial
  ht_rotulo = html_elem_label.gera("campo de texto", ": ")
  ht_campo = html_elem_input.gera(None, "text", "texto1", "blabla", None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo de texto sem valor inicial, com dica
  ht_rotulo = html_elem_label.gera("campo de texto", ": ")
  ht_campo = html_elem_input.gera(None, "text", "texto2", None, None, True, "Lorem ipusm", None)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo de senha
  ht_rotulo = html_elem_label.gera("campo de senha", ": ")
  ht_campo = html_elem_input.gera(None, "password", "senha", None, None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo numerico
  ht_rotulo = html_elem_label.gera("campo numerico", ": ")
  ht_campo = html_elem_input.gera(None, "number", "pernas", "17", "5", True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo escondido
  ht_rotulo = html_elem_label.gera("campo escondido", ": ")
  ht_campo = html_elem_input.gera(None, "hidden", "segredo", "boo", None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_elem_table.gera(linhas, ["TIPO", "ELEMENTO"])

  # cria botao de interacao com o formulario
  ht_botao = html_elem_button_submit.gera("Botao", 'url test', None, '#55ee55')

  # counteudo do formulario
  ht_campos = \
    ht_table + \
    ht_botao

  # cria formulario de teste
  formulario = html_elem_form.gera(ht_campos)
  return formulario

form_completo = cria_form_completo()
testa_modulo_html(html_elem_form, "completo", form_completo, True, False)
