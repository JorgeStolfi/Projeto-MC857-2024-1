#! /usr/bin/python3
import sys, re
from util_erros import aviso_prog
import util_titulo_de_video
import util_testes
import html_elem_paragraph

import sys

ok_global = True

modulo = util_titulo_de_video
funcao = modulo.valida
chave = "el-titulo"
for xrot, valido_ex, valido_pt, val in \
    ( # Validos só se {nulo_ok}:
      ( "Nulo",                     True,   True,  None,                        ),
      # Valido como exato ou padrão:
      ( "Valido1",                  True,   True,  "Velozes e Furiosos 2",      ),
      ( "Valido3",                  True,   True,  "Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghij", ),
      ( "Valido4",                  True,   True,  "Abcdefghij",                ),
      # Valido só como padrão:          
      ( "InícioNaoMaius",           False,  True,  "simbora!"                   ),
      ( "FinalBranco",              False,  True,  "Nada "                      ),
      ( "MuitoCurtoFull9",          False,  True,  "Valinoria"                  ),
      # Inválido em qualquer caso:         
      ( "MuitoCurtoParcial3",       False,  False, "Va"                         ),
      ( "MuitoLongo",               False,  False, "V" + ("r"*57) + "um!"       ),
      ( "CaracsInvalidos",          False,  False, "Titulo X-φ ≥ ぁ"            ),
      ( "BrancoDuplo",              False,  False, "Coisa  coisa"               ),
    ):
  ok = util_testes.testa_funcao_validadora_nulo_padrao(modulo, funcao, xrot, chave, valido_ex, valido_pt, val)
  if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
