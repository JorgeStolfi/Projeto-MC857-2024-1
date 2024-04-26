#! /usr/bin/python3

# Interfaces usadas por este script:

import html_elem_form
import html_elem_label
import html_elem_input
import html_elem_paragraph
import html_elem_table
import html_elem_button_submit
import html_bloco_tabela_de_campos
import util_testes

import sys

# !!! Reescrever usando util_testes.testa_gera !!!

ok_global = True

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = html_elem_form
  funcao = cria_form_de_teste
  
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

def cria_form_de_teste(multipart):
  """Cria um formulário com vários campos"""

  atrs = {}.copy()
  linhas = [].copy()
  
  # Cria formulário:
  
  linhas.append(("texto sem valor e sem dica",     "text",       "texto1",  True, None, ))

  linhas.append(("texto com valor e sem dica",     "text",       "texto2",  True, None, ))
  atrs['texto2'] = "Valor de {atrs}"

  linhas.append(("texto sem valor e com dica",     "text",       "texto3",  True, "Lorem ipsum", ))

  linhas.append(("texto com valor, readonly",      "text",       "texto4",  False, None, ))
  atrs['texto4'] = "Valor de {atrs}"

  linhas.append(("senha",                          "password",   "senha",   True, None, ))

  linhas.append(("Número com valor, min e dica",   "number",     "pernas1", True, "Min 4", ))
  atrs['pernas1'] = 7
  atrs['pernas1_min'] = 4

  linhas.append(("Número com min+dica, sem valor", "number",     "pernas2", True, "Min 4", ))
  atrs['pernas2_min'] = 4

  linhas.append(("campo upload arquivo",           "file",       "upload1", True, "Escolha", ))
  
  linhas.append(("texto longo com dica",           "textarea",   "parag1",  True, "blabla", ))

  linhas.append(("texto longo com valor",          "textarea",   "parag2",  True,  None, ))
  atrs['parag2'] = "Valor de {atrs}\nSegunda linha"

  linhas.append(("texto longo sem valor ou dica",  "textarea",   "parag3",  True,  None, ))
 
  linhas.append(("escondido",                      "hidden",     "segredo", False, None, ))
  atrs['segredo'] = "O chefe está roubando da firma"

  # Cria botao de interacao com o ht_form
  ht_botao = html_elem_button_submit.gera("Botao", 'urltest', None, '#55ee55')

  # Monta a tabela com os fragmentos HTML:
  ht_tabela = html_bloco_tabela_de_campos.gera(linhas, atrs)
  
  # Counteudo do formulário:
  ht_campos = \
    ht_tabela + \
    ht_botao

  # Cria formulário:
  ht_form = html_elem_form.gera(ht_campos, multipart)

  return ht_form

for multipart in False, True:
  rot_teste = "mult" + str(multipart)[0]
  testa_gera(rot_teste, str, multipart)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.")
else:
  aviso_erro("Alguns testes falharam", True)
