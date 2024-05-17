#! /usr/bin/python3

from util_erros import aviso_prog
import util_email
import util_testes
import sys, re

import sys

ok_global = True

modulo = util_email
funcao = modulo.valida
chave = 'efemail'

cx_ok = ("AZaz.%'/-09"*5) + "-botafora"
assert len(cx_ok) == 64
cx_longa = cx_ok + "Z"

dom_ok = ("AZ09-az."*31) + "oba.com"
assert len(dom_ok) == 255
dom_longo = dom_ok + "a"

dom_pt_longa = "www." + ("AZ09-az"*7) + ".coisas.com"

for xrot, xvalid, val, nulo_ok in \
    ( 
      ( "NoneT",             True,   None,                            True,  ), 
      ( "NoneF",             False,  None,                            False, ), 
      ( "Valido",            True,   "Alfa.%Omega@gmail.com",         True,  ),
      ( "Valido",            True,   cx_ok + "@" + dom_ok,            True,  ),
      ( "FaltaAt",           False,  "Alfa.Omega",                    True,  ),
      ( "DuploAt",           False,  "Alfa@Mu@Omega",                 True,  ),
      ( "CaracsInvalidos1",  False,  "Fulano@Bel%Trano",              True,  ),
      ( "CaracsInvalidos2",  False,  "Ful/ano@Bel.Trano",             True,  ),
      ( "CaracsInvalidos3",  False,  "Fulano@Bel×Trano",              True,  ),
      ( "CxMuitoLonga",      False,  cx_longa + "@" + dom_ok,         True,  ),
      ( "DomMuitoLongo",     False,  cx_ok + "@" + dom_longo,         True,  ),
      ( "DomPtMuitoLonga",   False,  cx_ok + "@" + dom_pt_longa,      True,  ),
    ):
  valido = xvalid and (nulo_ok or val != None)
  rot_teste = "email_" + xrot + "_nuok" + (str(nulo_ok)[0]) + ("_GUD" if valido else "_BAD")
  ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, nulo_ok)  
  if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
