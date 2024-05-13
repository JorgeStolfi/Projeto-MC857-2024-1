
import util_testes
import sys
from util_erros import ErroAtrib, erro_prog, mostra

ok_global = True

def testa_escreve_resultado_html(rot_teste, ht_res, frag):
  global ok_global
  global ok_global
  modulo = util_testes
  funcao = modulo.escreve_resultado_html
  pretty = True # Deve formatar o HTML para facilitar view source?
  funcao(modulo, funcao, rot_teste, ht_res, frag, pretty)

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
sys.stderr.write("  testando {util_testes.formata_valor}\n")

def testa_formata_valor(rot_teste, val, html):
  global ok_global
  global ok_global
  modulo = util_testes
  funcao = modulo.formata_valor
  frag = True    # Resultados HTML são só fragmentos?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao(rot_teste, modulo, funcao, str, html,frag,pretty,   val, html, 1000)
  if ok and not html:
    d1f = util_testes.formata_valor(rot_teste, val, html);
    sys.stderr.write("    " + ("~"*70) + "\n")
    sys.stderr.write(f"    d1 formatado como string =\n{d1f}\n")
    sys.stderr.write("    " + ("~"*70) + "\n")
  ok_global = ok_global and ok
  return ok

d1 = { 'coisa': 100, 'treco': 200, 'lhufas': [ 10, 100 ]*500, 'picas': { 'sim': 100, 'nao': "bla "*5000, 'bah': ( 123, 321, )*500 } }
for html in False, True:
  rot_teste = "html" + str(html)[0]
  testa_formata_valor(rot_teste, d1, html)

# ----------------------------------------------------------------------

def testa_unico_elemento(rot_teste, idents, res_esp):
  """Testa a função {util_testes.unico_elemento} na lista de identificadores {idents},
  verificando se devolve {res_esp}.  Se algum teste der errado,
  imprime uma mensagem de erro e desliga a variável global {ok_global}."""
  global ok_global
  modulo = util_testes
  funcao = modulo.unico_elemento
  html = False   # Resultados string já são HTML?
  frag = True    # Resultados HTML são só fragmentos?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao(rot_teste, modulo, funcao, res_esp, html,frag,pretty,   idents)
  ok_global = ok_global and ok
  return 

idents1u = [ ]
testa_unico_elemento("u1_vazia", idents1u, None)

idents2u = [ "W-00000111", ]
testa_unico_elemento("u2_unico", idents2u, idents2u[0])

idents3u = None
testa_unico_elemento("u3_none", idents3u, None)

idents4u = [ "Z-00000111", "Z-00000222", ]
testa_unico_elemento("u4_muitos", idents4u, "ErroAtrib")

idents5u = { 'coisa': "Z-00000222", }
testa_unico_elemento("u4_muitos", idents5u, "ErroAtrib")

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
