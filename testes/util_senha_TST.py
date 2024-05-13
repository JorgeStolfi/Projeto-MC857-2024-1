#! /usr/bin/python3

from util_erros import aviso_prog
import util_senha
import util_testes
import sys, re

import sys

ok_global = True

modulo = util_senha
funcao = modulo.valida
chave = 'segredo'
for xrot, xvalid, val, nulo_ok in \
    ( 
      ( "Valida",            True,   "123(meia)4", True,  ),
      ( "MuitoCurta",        False,  "123",        True,  ),
      ( "MuitoRepetida",     False,  "111111111",  True,  ),
      ( "SoLetras",          False,  "Segredo",    True,  ),
      ( "MuitoLonga",        False,  "X"+("a"*60), True,  ),
      ( "NoneT",             True,   None,         True,  ), 
      ( "NoneF",             False,  None,         False, ), 
    ):
  valido = xvalid and (nulo_ok or val != None)
  rot_teste = "senha_" + xrot + "_nuok" + (str(nulo_ok)[0]) + ("_GUD" if valido else "_BAD")
  ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, nulo_ok)  
  if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
