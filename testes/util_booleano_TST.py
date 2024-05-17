#! /usr/bin/python3

from util_erros import aviso_prog
import util_booleano
import util_testes
import sys

ok_global = True

modulo = util_booleano
funcao_valida = util_booleano.valida
funcao_converte = util_booleano.converte
chave = 'admin'
for val_in, val_out, xvalid in \
   ( ( None,   None,  False, ),
     ( True,   True,  True,  ),
     ( False,  False, True,  ),
     ( "true", True,  True,  ),
     ( "off",  False, True,  ),
     ( "y",    True,  True,  ),
     ( "no",   False, True,  ),
     ( "1",    True,  True,  ),
     ( "vero", True,  False, ),
     ( 0,      False, True,  ), 
     ( 1,      True,  True,  ), 
     ( 3.14,   False, False, ),
   ):
  for nulo_ok in False, True:
    valido = xvalid or (val_in == None and nulo_ok)
    rot_teste = f"B_val{val_in}_nulok{str(nulo_ok)[0]}"
    ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao_valida, chave, val_in, nulo_ok)
    if not ok: ok_global = False
    if valido:
      html = False; frag = False; pretty = False
      ok = util_testes.testa_funcao(rot_teste, modulo, funcao_converte, val_out, html, frag, pretty, val_in)
      if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
