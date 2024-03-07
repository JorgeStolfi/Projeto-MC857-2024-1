#! /usr/bin/python3

import html_elem_button_simples
import util_testes

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_elem_button_simples
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("Principal", "Principal", 'principal', None, '#60a3bc')

testa("Entrar",    "Entrar", 'solicitar_pag_login', None, '#55ee55')

testa("Sair",      "Sair", 'fazer_logout', None, '#60a3bc')

testa("simples_Cadastrar", "Cadastrar", 'solicitar_pag_cadastrar_usuario', None, '#60a3bc')

testa("simples_OK",        "OK", 'principal', None, '#55ee55')

testa("url_args_valido",        "Teste com parâmetros de URL válidos", 'principal', {"key1":"val1", "key2": "val2,val3"}, '#55ee55')

testa("url_args_invalido",        "Teste com parâmetros de URL inválidos", 'principal', {"valid_key":"inv&lid_value", "inv&lid_key": "valid_value"}, '#55ee55')
