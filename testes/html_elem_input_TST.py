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
   
testa_gera("text_dica_obrig_F",   "Peso", "text", "peso", None,    None, True,  "Máximo 50 kg", "vade_retro", False)
testa_gera("text_vini_obrig_F",   "Peso", "text", "peso", "30 kg", None, True,  None,           "vade_retro", False)
testa_gera("text_rdonly_obrig_F", "Peso", "text", "peso", "30 kg", None, False, None,           "vade_retro", False)

testa_gera("num_dica_obrig_F",   "Peso (kg)", "number", "peso", None, None,  True, "Máximo 50", "vade_retro", False)
testa_gera("num_vini_obrig_F",   "Peso (kg)", "number", "peso", "30", None,  True, None,        "vade_retro", False)
testa_gera("num_vmin_obrig_F",   "Peso (kg)", "number", "peso", "30", "3",   True, None,        "vade_retro", False)
testa_gera("num_rdonly_obrig_F", "Peso (kg)", "number", "peso", "30", None,  False,None,        "vade_retro", False)

testa_gera("email_dica_obrig_F",  "Email", "email", "email", None,               None,  True, "{user}@{host}", "do_it", False)
testa_gera("email_vini_obrig_F",  "Email", "email", "email", "jose@tatu.gov.br", None,  True, None,            "do_it", False)

testa_gera("senha_dica_obrig_F",  "Senha", "password", "senha", None, None,  True, "Máximo 2 letras", "do_it", False)
testa_gera("senha_vini_obrig_F",  "Senha", "password", "senha", "99", None,  True, None,              "do_it", False)

testa_gera("hidden_vini_obrig_F",  None, "hidden", "user", "U-12345678", None, False, None,   "do_it", False)

testa_gera("text_obrig_T",  None, "text", "user", "U-12345678", None, True, None,   "do_it", True)
testa_gera("text_obrig_F",  None, "text", "user", "U-12345678", None, True, None,   "do_it", False)

sys.stderr.write("Testes terminados normalmente.");
