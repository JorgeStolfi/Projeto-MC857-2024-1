#! /usr/bin/python3

from util_erros import aviso_prog
import util_dict
import util_testes
import sys, re

ok_global = True

sys.stderr.write("!!! Testar as funções !!!\n")
ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
