#! /usr/bin/python3

from util_erros import aviso_prog
import util_booleano
import util_testes
import sys

ok_global = True

modulo = util_booleano
funcao = modulo.valida
chave = 'admin'
for val in None, True, False, 410:
  for nulo_ok in False, True:
    valido = type(val) is bool or (val == None and nulo_ok)
    rot_teste = "bool_val" + str(val)[0] + "_nulok" + str(nulo_ok)[0]
    ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, nulo_ok)
    if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
