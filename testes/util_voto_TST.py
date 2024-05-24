#! /usr/bin/python3

from util_erros import aviso_prog
import util_voto
import util_testes
import sys

ok_global = True

modulo = util_voto
funcao = util_voto.valida
chave = 'opiniao'

for val in None, True, -1, 0, 1.0, "2", 3.1, 3, 4, :
  rot_teste = f"IV_val{str(val)}"
  if val != None:
    if isinstance(val, int) or isinstance(val,str):
      valido = int(val) >= 0 and int(val) <= 4
    elif isinstance(val, float):
      valido = (val == int(val)) and val >= 0 and val <= 4
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
