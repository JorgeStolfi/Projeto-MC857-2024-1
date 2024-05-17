
import util_testes
import util_erros
from util_erros import ErroAtrib
from util_testes import testa_funcao

import sys

ok_global = True # {False} se algum teste de alguma função falhou.

modulo = util_erros

for p in range(10):
  testa_funcao("MO",   modulo, modulo.mostra,     None,             False,False,False,  2*p, f"indentado {2*p}")
 
testa_funcao("ER",   modulo, modulo.erro_prog,  "AssertionError", False,False,False, "Tomate é Fruta")

testa_funcao("AV-F", modulo, modulo.aviso_prog, None,             False,False,False, "Maçã não é Fruta", False)
testa_funcao("AV-T", modulo, modulo.aviso_prog, None,             False,False,False, "Caju não é fruta", True)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
