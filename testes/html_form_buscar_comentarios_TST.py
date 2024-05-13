import html_form_buscar_comentarios
import util_testes

import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_form_buscar_comentarios
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

atrs1 = {'autor': "U-00000002", 'pai': "C-00000001"}

for admin in False, True:
    testa_gera("ComValores-adm" + str(admin)[0], str, atrs1, admin)
    testa_gera("SemValores-adm" + str(admin)[0], str, {}, admin)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.")
else:
  aviso_prog("Alguns testes falharam", True)
