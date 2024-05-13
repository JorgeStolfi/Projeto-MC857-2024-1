#! /usr/bin/python3

from util_erros import aviso_prog
import util_email
import util_testes
import sys, re

import sys

ok_global = True

modulo = util_email
funcao = modulo.valida
chave = 'fofoca'
for xrot, xvalid, val, nulo_ok in \
    ( 
      ( "NoneT",             True,   None,                     True,  ), 
      ( "NoneF",             False,  None,                     False, ), 
      ( "Valido",            True,   "Alfa.%Omega@gmail.com",  True,  ),
      ( "FaltaAt",           False,  "Alfa.Omega",             True,  ),
      ( "DuploAt",           False,  "Alfa@Mu@Omega",          True,  ),
      ( "CaracsInvalidos1",  False,  "Fulano@Bel%Trano",       True,  ),
      ( "CaracsInvalidos2",  False,  "Ful/ano@Bel.Trano",      True,  ),
      ( "CaracsInvalidos3",  False,  "Fulano@Bel×Trano",       True,  ),
      ( "MuitoLonga",        False,  "X"+("a"*60),             True,  ),
    ):
  valido = xvalid and (nulo_ok or val != None)
  rot_teste = "email_" + xrot + "_nuok" + (str(nulo_ok)[0]) + ("_GUD" if valido else "_BAD")
  padrao_ok = False # !!! Testar com {True} e com "*{val}*" !!!
  ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, nulo_ok, padrao_ok)  
  if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
