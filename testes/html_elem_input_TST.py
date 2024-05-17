#! /usr/bin/python3

import html_elem_input
import util_testes

import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = html_elem_input
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
   
#                                  res_esp tipo        chave      ident       val_ini             val_min   editavel  dica               cmd           obrig
testa_gera("text_dica_obrig_F",    str,    "text",     "peso",    "idpeso",   None,               None,     True,     "Máximo 50 kg",    "vade_retro", False)
testa_gera("text_vini_obrig_F",    str,    "text",     "peso",    "idpeso",   "30 kg",            None,     True,     None,              "vade_retro", False)
testa_gera("text_rdonly_obrig_F",  str,    "text",     "peso",    None,       "30 kg",            None,     False,    None,              "vade_retro", False)

testa_gera("num_dica_obrig_F",     str,    "number",   "peso",    "idpeso",   None,               None,     True,     "Máximo 50",       "vade_retro", False)
testa_gera("num_vini_obrig_F",     str,    "number",   "peso",    "idpeso",   "30",               None,     True,     None,              "vade_retro", False)
testa_gera("num_vmin_obrig_F",     str,    "number",   "peso",    "idpeso",   "30",               "3",      True,     None,              "vade_retro", False)
testa_gera("num_rdonly_obrig_F",   str,    "number",   "peso",    "idpeso",   "30",               None,     False,    None,              "vade_retro", False)

testa_gera("email_dica_obrig_F",   str,    "email",    "email",   "idmail",   None,               None,     True,     "{user}@{host}",   "do_it",      False)
testa_gera("email_vini_obrig_F",   str,    "email",    "email",   "idmail",   "jose@tatu.gov.br", None,     True,     None,              "do_it",      False)

testa_gera("senha_dica_obrig_F",   str,    "password", "senha",   "idsenha",  None,               None,     True,     "Máximo 2 letras", "do_it",      False)
testa_gera("senha_vini_obrig_F",   str,    "password", "senha",   "idsenha",  "99",               None,     True,     None,              "do_it",      False)

testa_gera("file_obrig_F",         str,    "file",     "arquivo", "idfile",   None,               None,     True,     None,              "do_it",      False)

data1 = "2024-04-19 19:01:00 UTC"

testa_gera("data_dica_obrig_F",     str,    "date",     "niver",   "idniver",  None,               None,     True,     "Aniversário",     "do_it",      False)
testa_gera("data_vini_obrig_F",     str,    "date",     "niver",   "idniver",  data1,              None,     True,     None,              "do_it",      False)

testa_gera("hidden_vini_obrig_F",   str,    "hidden",   "user",    "iduser",   "U-12345678",       None,     False,    None,              "do_it",      False)

testa_gera("text_obrig_T",          str,    "text",     "user",    "iduser",   "U-12345678",       None,     True,     None,              "do_it",      True)
testa_gera("text_obrig_F",          str,    "text",     "user",    "iduser",   "U-12345678",       None,     True,     None,              "do_it",      False)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n");
else:
  aviso_prog("Alguns testes falharam.", True)
