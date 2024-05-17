#! /usr/bin/python3

from util_erros import aviso_prog
import util_inteiro
import util_testes
import sys

ok_global = True

modulo = util_inteiro
funcao = util_inteiro.valida
chave = 'pernas'
val_min = 100
val_max = 500

for val in None, 410, 25, 510, 2.5:
  for nulo_ok in False, True:
    valido = (type(val) is int and val >= val_min and val <= val_max) or (val == None and nulo_ok)
    rot_teste = f"IV_val{val}_nulok{str(nulo_ok)[0]}"
    ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, val_min, val_max, nulo_ok)
    if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
