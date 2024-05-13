#! /usr/bin/python3

from util_erros import aviso_prog
import util_nome_de_usuario
import util_testes
import sys, re

ok_global = True

modulo = util_nome_de_usuario
funcao = modulo.valida
chave = "padrinho"
for xrot, valido_ex, valido_pt, val in \
    ( # Valido só se {nulo_ok}:
      ( "nome_Nulo",               True,   True,  None, ),
      # Valido como exato ou padrão:
      ( "nome_Valido01",           True,   True,  "José da Silvã P. O'Hara Costa-Gravas",    ), 
      ( "nome_Valido02",           True,   True,  "P.-Louis Sant'Ana",                       ),
      ( "nome_Valido03",           True,   True,  "Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghij", ),
      ( "nome_Valido04",           True,   True,  "Abcdefghij",                              ),
      # Valido só como padrão:          
      ( "nome_MuitoCurto9",        False,  True,  "José Josias",                             ),
      ( "nome_BrancoInicial",      False,  True,  " José da Silva P. O'Hara Costa-Gravas",   ),
      ( "nome_BrancoFinal",        False,  True,  "José da Silva P. O'Hara Costa-Gravas ",   ),
      ( "nome_ApostInicial",       False,  True,  "'Hara Costa-Gravas",                      ),
      ( "nome_ApostFinal",         False,  True,  "José da Silva O'",                        ),
      ( "nome_Hifeninicial",       False,  True,  "-Gravas",                                 ),
      ( "nome_HifenFinal",         False,  True,  "Costa-",                                  ),
      ( "nome_PontoInicial",       False,  True,  ".-Louis",                                 ),
      ( "nome_PontoFinal",         False,  True,  "José da S.",                              ),
      # Inválido em qualquer caso:         
      ( "nome_MuitoCurto2",        False,  False, "Jo",                                      ),
      ( "nome_CaracsInvalidos",    False,  False, "Elon X-φ ≥ 17",                           ),
      ( "nome_BrancoDuplo",        False,  False, "José da Silva P.  O'Hara Costa-Gravas",   ),
      ( "nome_MuitoLongo",         False,  False, "José Josefino Josualdo Josismar Josias Josenildo Josafá Josênio", ),
      ( "nome_ApostInvalido1",     False,  False, "José' da Silva P. O'Hara Costa-Gravas",   ),
      ( "nome_ApostInvalido2",     False,  False, "José da Silva P'. O'Hara Costa-Gravas",   ),
      ( "nome_HifenInvalido1",     False,  False, "José-da Silva P-. O'Hara Costa-Gravas",   ),
      ( "nome_HifenInvalido2",     False,  False, "José-da Silva O'Hara Costa-Gravas",       ),
      ( "nome_PontoInvalido2",     False,  False, "José da Silva P.O'Hara Costa-Gravas ",    ),
    ):
  ok = util_testes.testa_funcao_validadora_nulo_padrao(modulo, funcao, xrot, chave, valido_ex, valido_pt, val)
  if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
