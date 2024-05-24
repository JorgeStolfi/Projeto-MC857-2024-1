#! /usr/bin/python3

from util_erros import aviso_prog
import util_nota
import util_testes
import sys

ok_global = True

modulo = util_nota
funcao = util_nota.valida
chave = 'escore'

for val in None, True, -0.5, 0, 0.4, "0.6", 2, 3, 3.4, 3.6, 4.1, :
  rot_teste = f"IV_val{str(val)}"
  if val != None:
    valido = (isinstance(val, float) or isinstance(val, int) or isinstance(val, str)) and float(val) >= 0 and float(val) <= 4.0
    ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, False)
    if not ok: ok_global = False
  else:
    for nulo_ok in False, True:
      valido = nulo_ok
      xnul = f"_nulok{str(nulo_ok)[0]}"
      ok = util_testes.testa_funcao_validadora(rot_teste + xnul, valido, modulo, funcao, chave, val, nulo_ok)
      if not ok: ok_global = False
      
# !!! devia testar {formata} !!!

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
