#! /usr/bin/python3

from util_erros import aviso_prog
import util_nome_de_usuario
import util_testes
import sys, re

ok_global = True

modulo = util_nome_de_usuario
funcao = util_nome_de_usuario.valida
chave = "padrinho"

nome_curto_gud = "José Josué"
assert len(nome_curto_gud) == 10
nome_curto_bad = nome_curto_gud[:-1]

nome_longo_gud = "José Josênio Josualdo Josildo Josafá Josias Josimar Josefino"
assert len(nome_longo_gud) == 60
nome_longo_bad = nome_longo_gud + "s"

for xrot, valido, val in \
    ( # Válido:          
      ( "nome_Nulo",               None, None                                         ),
      ( "nome_Valido01",           True, "José da Silvã P. O'Hara Costa-Gravas",      ), 
      ( "nome_Valido02",           True, "P.-Louis Sant'Ana",                         ),
      ( "nome_Valido03",           True, nome_curto_gud,                              ),
      ( "nome_Valido04",           True, nome_longo_gud,                              ),
      # Inválido:         
      ( "nome_MuitoCurto",         False,  nome_curto_bad,                            ),
      ( "nome_MuitoLongo",         False,  nome_longo_bad,                            ),
      ( "nome_BrancoInicial",      False,  " José da Silva P. O'Hara Costa-Gravas",   ),
      ( "nome_BrancoFinal",        False,  "José da Silva P. O'Hara Costa-Gravas ",   ),
      ( "nome_ApostInicial",       False,  "'Hara Costa-Gravas",                      ),
      ( "nome_ApostFinal",         False,  "José da Silva O'",                        ),
      ( "nome_Hifeninicial",       False,  "-Gravas",                                 ),
      ( "nome_HifenFinal",         False,  "Costa-",                                  ),
      ( "nome_PontoInicial",       False,  ".-Louis",                                 ),
      ( "nome_PontoFinal",         False,  "José da S.",                              ),
      ( "nome_CaracsInvalidos",    False,  "Elon X-φ ≥ 17",                           ),
      ( "nome_BrancoDuplo",        False,  "José da Silva P.  O'Hara Costa-Gravas",   ),
      ( "nome_ApostInvalido1",     False,  "José' da Silva P. O'Hara Costa-Gravas",   ),
      ( "nome_ApostInvalido2",     False,  "José da Silva P'. O'Hara Costa-Gravas",   ),
      ( "nome_HifenInvalido1",     False,  "José-da Silva P-. O'Hara Costa-Gravas",   ),
      ( "nome_HifenInvalido2",     False,  "José-da Silva O'Hara Costa-Gravas",       ),
      ( "nome_PontoInvalido2",     False,  "José da Silva P.O'Hara Costa-Gravas ",    ),
    ):
  nulo_oks = ( False, ) if val != None else ( False, True, )
  for nulo_ok in nulo_oks:
    ok = util_testes.testa_funcao_validadora(xrot, valido, modulo, funcao, chave, val, nulo_ok)
    if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
