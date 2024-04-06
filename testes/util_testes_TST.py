
import util_testes
import sys
from util_testes import erro_prog, mostra

def testa_escreve_resultado_html(rotulo, ht_res, frag):
  modulo = util_testes
  pretty = True # Deve formatar o HTML para facilitar view source?
  modulo.escreve_resultado_html(modulo, "escreve_resultado_html." + rotulo, ht_res, frag, pretty)

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
sys.stderr.write("  testando {util_testes.mostra}\n")
for p in range(10):
  util_testes.mostra(2*p, ("indentado por %d" % (2*p)))
  
# ----------------------------------------------------------------------
sys.stderr.write("  testando {util_testes.formata_dict}\n")

d1 = { 'coisa': 100, 'treco': 200, 'lhufas': [ 10, 100 ], 'picas': { 'sim': 100, 'nao': 200, 'bah': 123 } }
fd1 = util_testes.formata_dict(d1);
sys.stderr.write("    d1 formatado:\n%s\n" % fd1)

sys.stderr.write("Testes terminados normalmente.\n")
