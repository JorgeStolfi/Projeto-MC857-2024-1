#! /usr/bin/python3

import html_elem_input
import util_testes

import sys

def testa_gera(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_elem_input
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args)
   
testa_gera("text_dica",   "Peso", "text", "peso", None,    None, True,  "Máximo 50 kg", "vade_retro")
testa_gera("text_vini",   "Peso", "text", "peso", "30 kg", None, True,  None,           "vade_retro")
testa_gera("text_rdonly", "Peso", "text", "peso", "30 kg", None, False, None,           "vade_retro")

testa_gera("num_dica",   "Peso (kg)", "number", "peso", None, None,  True, "Máximo 50", "vade_retro")
testa_gera("num_vini",   "Peso (kg)", "number", "peso", "30", None,  True, None,        "vade_retro")
testa_gera("num_vmin",   "Peso (kg)", "number", "peso", "30", "3",   True, None,        "vade_retro")
testa_gera("num_rdonly", "Peso (kg)", "number", "peso", "30", None,  False,None,        "vade_retro")

testa_gera("email_dica",  "Email", "email", "email", None,               None,  True, "{user}@{host}", "do_it")
testa_gera("email_vini",  "Email", "email", "email", "jose@tatu.gov.br", None,  True, None,            "do_it")

testa_gera("senha_dica",  "Senha", "password", "senha", None, None,  True, "Máximo 2 letras", "do_it")
testa_gera("senha_vini",  "Senha", "password", "senha", "99", None,  True, None,              "do_it")

testa_gera("hidden_vini",  None, "hidden", "user", "U-12345678", None, False, None,   "do_it")

testa_gera("text_obrigatorio",  None, "text", "user", "U-12345678", None, True, None,   "do_it", True)
testa_gera("text_not_obrigatorio",  None, "text", "user", "U-12345678", None, True, None,   "do_it", False)
testa_gera("text_not_obrigatorio_default",  None, "text", "user", "U-12345678", None, True, None,   "do_it")

sys.stderr.write("Testes terminados normalmente.");