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
for xrot, valido_ex, valido_pt, val in \
    ( # Validos só se {nulo_ok}:
      ( "Nulo",                      True,   True,  None,                               ),
      # Valido como exato ou padrão:
      ( "Valido1",                   True,   True,  "Eu sabia!\nNão dá pra confiar...", ),
      ( "Valido3",                   True,   True,  "É mesmo?" + " Quá!"*198,           ),
      ( "Valido4",                   True,   True,  "Gödel disse isso para Tupã",       ),
      ( "Valido5",                   True,   True,  "!"                                 ),
      # Valido só como padrão:          
      ( "BrancoIni",                 False,  False, " ou home"                          ),
      ( "BrancoFim",                 False,  False, "ando "                             ),
      ( "NLIni",                     False,  False, "\nSabendo"                         ),
      ( "NLFim",                     False,  False, "final.\n"                          ),
      # Inválido em qualquer caso:         
      ( "Vazio",                     False,  False, ""                                  ),
      ( "MuitoLongo",                False,  False, "Quá!" + " Quá!"*200,               ),
      ( "CaracsInvalidos1",          False,  False, "Título × Líluto"                   ),
      ( "CaracsInvalidos2",          False,  False, "😁😊😄"                             ),
      ( "CaracsInvalidos3",          False,  False, "X-φ ≥ ぁ"                          ),
    ):
  ok = util_testes.testa_funcao_validadora_nulo_padrao(modulo, funcao, xrot, chave, valido_ex, valido_pt, val)
  if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
