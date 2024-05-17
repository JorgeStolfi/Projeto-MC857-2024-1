#! /usr/bin/python3
import sys, re
from util_erros import aviso_prog
import util_texto_de_comentario
import util_testes
import html_elem_paragraph

import sys

ok_global = True

modulo = util_texto_de_comentario
funcao = modulo.valida
chave = "fofoca"
for xrot, valido, val in \
    ( # Validos só se {nulo_ok}:
      ( "Nulo",                      False,  None,                               ),
      # Valido em qualquer caso:
      ( "Valido1",                   True,   "Eu sabia!\nNão dá pra confiar...", ),
      ( "Valido3",                   True,   "É mesmo?" + " Quá!"*198,           ),
      ( "Valido4",                   True,   "Gödel disse isso para Tupã",       ),
      ( "Valido5",                   True,   "!"                                 ),
      # Inválido em qualquer caso:         
      ( "BrancoIni",                 False,  " ou home"                          ),
      ( "BrancoFim",                 False,  "ando "                             ),
      ( "NLIni",                     False,  "\nSabendo"                         ),
      ( "NLFim",                     False,  "final.\n"                          ),
      ( "Vazio",                     False,  ""                                  ),
      ( "MuitoLongo",                False,  "Quá!" + " Quá!"*200,               ),
      ( "CaracsInvalidos1",          False,  "Título × Líluto"                   ),
      ( "CaracsInvalidos2",          False,  "😁😊😄"                             ),
      ( "CaracsInvalidos3",          False,  "X-φ ≥ ぁ"                          ),
    ):
  rot_teste = xrot
  ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, False)
  if not ok: ok_global = False
  if val == None: 
    ok = util_testes.testa_funcao_validadora(rot_teste + "_nuloOK", True, modulo, funcao, chave, val, True)
    if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
