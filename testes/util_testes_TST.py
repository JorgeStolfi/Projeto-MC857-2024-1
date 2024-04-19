
import util_testes
import sys
from util_erros import ErroAtrib, erro_prog, mostra

ok_global = True

def testa_escreve_resultado_html(rot_teste, ht_res, frag):
  modulo = util_testes
  pretty = True # Deve formatar o HTML para facilitar view source?
  modulo.escreve_resultado_html(modulo, "escreve_resultado_html." + rot_teste, ht_res, frag, pretty)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {util_testes.escreve_resultado_html}\n")
testa_escreve_resultado_html("frag_vazio",  [],                   True); 
testa_escreve_resultado_html("frag_string", "Banana",             True); 
testa_escreve_resultado_html("frag_list",   ["Banana","Bacate",], True); 
pag1 = \
    "<!DOCTYPE HTML>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "</head>\n" + \
    "<body>\n" + \
    "Página de teste\n" + \
    "</body>\n" + \
    "</html>\n"  
testa_escreve_resultado_html("pag",   pag1, False); 
 
# ----------------------------------------------------------------------
sys.stderr.write("  testando {util_testes.formata_dict}\n")

d1 = { 'coisa': 100, 'treco': 200, 'lhufas': [ 10, 100 ], 'picas': { 'sim': 100, 'nao': 200, 'bah': 123 } }
fd1 = util_testes.formata_dict(d1);
sys.stderr.write("    d1 formatado:\n%s\n" % fd1)

# ----------------------------------------------------------------------

def testa_funcao_unico_elemento(rot_teste, idents):
  """Testa a função {util_testes.unico_elemento} na lista de identificadores {idents},
  verificando se devolve {None}, devolve {idents[0]}, ou levanta erro {AssertionError}
  conforme a lista tenha 0, 1, ou mais de 1 elemento.  Se algum teste der errado,
  imprime uma mensagem de erro e desliga a variável global {ok_global}."""
  global ok_global
  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"  Teste {rot_teste} idents = {str(idents)}\n")
  ok = True # Estado deste teste.

  # Paranóia: verifica tipo dos argumentos do teste:
  if idents != None and type(idents) != list and type(idents) != tuple:
    erro_prog("Argumento {idents} = %s devis ser {None} ou lista/tupla" % str(idents))

  # Testa {unico_elemento()}:
  sys.stderr.write("  {unico_elemento(%s)} =" % str(idents));
  try:
    ident_cmp = util_testes.unico_elemento(idents)
    sys.stderr.write(" %s\n" % str(ident_cmp))
    aborted = False
  except ErroAtrib as ex:     
    sys.stderr.write("\n")
    sys.stderr.write("  deu {ErroAtrib} com %s\n" % str(ex))
    ident_cmp = None
    aborted = True
  if idents == None or len(idents) == 0:
    if ident_cmp != None or aborted:
      sys.stderr.write("  ** devia ser {None}\n")
      ok = False
  elif len(idents) == 1:
    if type(ident_cmp) != str:
      sys.stderr.write("  ** devia ser string\n")
      ok = False
    elif ident_cmp != idents[0] or aborted:
      sys.stderr.write("  ** devia ser %s\n" % idents[0])
      ok = False
  else:
    if not aborted:
      sys.stderr.write("  ** devia ter dado {ErroAtrib}\n")
      ok = False
  if ok:
    sys.stderr.write("  Teste OK\n")
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")

idents1u = [ ]
testa_funcao_unico_elemento("id_u1_bom", idents1u)

idents2u = [ "W-00000111", ]
testa_funcao_unico_elemento("id_u2_bom", idents2u)

idents3u = None
testa_funcao_unico_elemento("id_u3_bom", idents3u)

idents4u = [ "Z-00000111", "Z-00000222", ]
testa_funcao_unico_elemento("id_u4_mau", idents4u)

sys.stderr.write("Testes terminados normalmente.\n")
