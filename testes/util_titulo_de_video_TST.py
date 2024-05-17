#! /usr/bin/python3
import sys, re
from util_erros import aviso_prog
import util_titulo_de_video
import util_testes
import html_elem_paragraph

import sys

ok_global = True

modulo = util_titulo_de_video
funcao = util_titulo_de_video.valida
chave = "el-titulo"
for xrot, valido, val in \
    ( # Validos só se {nulo_ok}:
      ( "Nulo",                     False,  None,                        ),
      # Valido em qualquer caso:
      ( "Valido1",                  True,   "Velozes e Furiosos 2",      ),
      ( "Valido3",                  True,   "Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghij", ),
      ( "Valido4",                  True,   "Abcdefghij",                ),
      # Inválido em qualquer caso:          
      ( "InícioNaoMaius",           False,  "simbora!"                   ),
      ( "FinalBranco",              False,  "Nada "                      ),
      ( "MuitoCurtoFull9",          False,  "Valinoria"                  ),
      ( "MuitoCurtoParcial3",       False,  "Va"                         ),
      ( "MuitoLongo",               False,  "V" + ("r"*57) + "um!"       ),
      ( "CaracsInvalidos",          False,  "Titulo X-φ ≥ ぁ"            ),
      ( "BrancoDuplo",              False,  "Coisa  coisa"               ),
    ):
  rot_teste = xrot
  ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, False)
  if not ok: ok_global = False
  if val == None:
    ok = util_testes.testa_funcao_validadora(rot_teste, True, modulo, funcao, chave, val, True)
    if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
