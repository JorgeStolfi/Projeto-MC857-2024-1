#! /usr/bin/python3

from util_erros import aviso_prog
import util_data
import util_testes
import sys, re

ok_global = True

modulo = util_data
funcao = modulo.valida
chave = "niver"
for xrot, xvalid, val in \
    ( # Valido só se {nulo_ok}:
      ("None",              True,   None,                        ), 
      # Valido:
      ("FullValida",        True,   "2024-04-05 20:10:05 UTC",   ), 
      # Inválido:         
      ("FullComBarras",     False,  "2024/04/05 20:10:05 UTC",   ), 
      ("FullAno1899",       False,  "1899-12-31 20:10:05 UTC",   ), 
      ("FullMes00",         False,  "2024-00-31 20:10:05 UTC",   ), 
      ("FullMes13",         False,  "2024-13-31 20:10:05 UTC",   ), 
      ("FullDia00",         False,  "2024-12-00 20:10:05 UTC",   ), 
      ("FullDia32",         False,  "2024-12-32 20:10:05 UTC",   ), 
      ("FullHora24",        False,  "2024-04-19 24:10:05 UTC",   ), 
      ("FullMinuto60",      False,  "2024-04-19 20:60:05 UTC",   ), 
      ("FullSegundo61",     False,  "2024-04-19 20:10:61 UTC",   ), 
      ("FullZona",          False,  "2024-04-19 20:10:05 BRL",   ), 

      ("PartAno1899",       False,  "1899-12-31",                ), 
      ("PartMes00",         False,  "-00-31 20:",                ), 
      ("PartMes13",         False,  "-13-31",                    ), 
      ("PartDia00",         False,  "2024-12-00",                ), 
      ("PartDia32",         False,  "2024-12-32",                ), 
      ("PartHora24",        False,  "24:10:05 UTC",              ), 
      ("PartMinuto60",      False,  "20:60:05 UTC",              ), 
      ("PartSegundo61",     False,  "20:10:61 UTC",              ), 
      ("PartZona",          False,  "20:10:05 BRL",              ), 

    ):
  for nulo_ok in False, True:
    if val == None or not nulo_ok:
      valido = xvalid and (nulo_ok or val != None)
      rot_teste = "data_" + xrot + "_nuok" + (str(nulo_ok)[0]) + ("_GUD" if valido else "_BAD")
      ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, nulo_ok)
      if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
