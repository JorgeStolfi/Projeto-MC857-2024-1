
import util_testes
import util_erros
from util_erros import ErroAtrib

import sys

ok_global = True # {False} se algum teste de alguma função falhou.

def testa_funcao(rot_teste, funcao, valido, res_esperado, *args):
  """Testa a {funcao} com argumentos {args}.  Se {valido} é {True},
  espera que a função devolva o resultado {res_esperado}, mesmo que {None}.
  Se {valido} é {False}, espera que ela levante uma exceção cujo
  nome é {res_esperado}.  Em todo caso, escreve um arquivo 
  "testes/saida/util_erros.{funcao}.{rot_teste}.html" com o resultado."""
  
  global ok_global
  ok = True # {False} se algum teste desta função falhou.

  sys.stderr.write("-"*70 + "\n")

  modulo = util_erros
  nome_mod = modulo.__name__
  nome_fn = funcao.__name__
  levantou = False # {True} se levantou erro.
  try:
    sys.stderr.write(f"  testando {nome_mod}.{nome_fn}({str(args)})\n")
    res = funcao(*args)
  except AssertionError as ex:
    levantou = True
    res = "AssertionError"
  except ErroAtrib as ex:
    levantou = True
    res = "ErroAtrib"

  if levantou:
    ht_res = f"levantou exeção {res}"
    sys.stderr.write(f"  levantou exceção {res}\n")
    if valido:
      sys.stderr.write(f"  ** deveria retornar {res_esperado} normalmente!\n")
      ok = False
    elif res != res_esperado:
      sys.stderr.write(f"  ** deveria levantar exceção {res_esperado}!\n")
      ok = False
    else:
      sys.stderr.write(f"  OK!\n")
  else:
    ht_res = str(res)
    if len(ht_res) > 60: ht_res = ht_res[:60] + "[...]"
    sys.stderr.write(f"  resultado = {ht_res}\n")
    if not valido:
      sys.stderr.write(f"  ** deveria levantar erro {str(res_esperado)}!\n")
      ok = False
    elif res != res_esperado:
      sys.stderr.write(f"  ** deveria devolver {str(res_esperado)}!\n")
      ok = False
    else:
      sys.stderr.write(f"  OK!\n")
      
  func_rot = nome_fn + "." + rot_teste
  frag = True   # Resultado é só um fragmento de página?
  pretty = True # Deve formatar o HTML para facilitar view source?
  util_testes.escreve_resultado_html(modulo, func_rot, ht_res, frag, pretty)

  if not ok:
    util_erros.aviso_prog("teste falhou", True)
    ok_global = False

  sys.stderr.write("-"*70 + "\n")
  return
  
# ----------------------------------------------------------------------
sys.stderr.write("  testando {util_testes.mostra}\n")
for p in range(10):
  testa_funcao("MO",   util_erros.mostra,      True, None, 2*p, f"indentado {2*p}")
 
testa_funcao("ER",   util_erros.erro_prog,  False, "AssertionError", "Tomate é Fruta")

testa_funcao("AV-F", util_erros.aviso_prog, True,  None,             "Maçã não é Fruta", False)
testa_funcao("AV-T", util_erros.aviso_prog, True,  None,             "Caju não é fruta", True)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
