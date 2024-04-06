#! /usr/bin/python3

import sys
import util_identificador
from util_testes import ErroAtrib, erro_prog, mostra

ok_global = True  # Vira {False} se houver erro.

def testa_funcoes_de_para_indice(rotulo, let, indice, ident):
  """Testa as funções {util_identificador.de_indice(let,indice)} e 
  {util_identificador.para_indice(let, ident)}, verificando se o resultado
  de uma é o argumento da outra.  Se algum teste der errado,
  imprime uma mensagem de erro, e desliga a variável global {ok_global}."""
  global ok_global
  ok = True # Estado deste teste.
  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"  teste {rotulo} let = '{let}' indice = {str(indice)} ident = '{str(ident)}'\n")
  
  # Paranóia: verifica tipo dos argumentos do teste:
  if not type(indice) is int:
    erro_prog("Tipo de {indice} não é {int}")
  elif indice < 1 or indice > 99999999:
    erro_prog("Valor de {indice} fora dos limites")
    
  if not type(ident) is str:
    erro_prog("Tipo de {indice} não é {str}")
  elif len(ident) != 10:
    erro_prog("Comprimento de {ident} incorreto")
 
  if let != ident[0]:
    erro_prog("Letra {let} não bate com {ident}")

  # Testa a função {de_indice()}:
  ident_cmp = util_identificador.de_indice(let, indice)
  sys.stderr.write("  {de_indice('%s',%d)} = '%s'\n" % (let,indice,ident_cmp))
  if ident != ident_cmp:
    sys.stderr.write("  ** devia ser %s\n" % ident)
    ok = False
  
  # Testa a função {para_indice()}:
  indice_cmp = util_identificador.para_indice(let, ident)
  sys.stderr.write("  {para_indice('%s','%s')} = %d\n" % (let,ident,indice_cmp))
  if indice != indice_cmp:
    sys.stderr.write("  ** devia ser %d\n" % indice)
    ok = False
    
  if ok:
    sys.stderr.write("  Teste OK\n")
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")
  
let1 = "X"
indice1 = 123456
ident1 = "X-00123456"
testa_funcoes_de_para_indice("id_A", let1, indice1, ident1)

# ----------------------------------------------------------------------

def testa_funcao_de_lista_de_indices(rotulo, let, indices, idents):
  """Testa a função {util_identificador.de_lista_de_indices} na lista de inteiros {indices},
  verificando se o resultado é a lista de identificadores {idents}.  Se algum teste der errado,
  imprime uma mensagem de erro e desliga a variável global {ok_global}."""
  global ok_global
  sys.stderr.write(f"  {'~'*70}\n")
  sys.stderr.write(f"  Teste {rotulo} (lista) let = '{let}' indices = {str(indices)} idents = {str(idents)}\n")
  ok = True # Estado deste teste.

  # Paranóia: verifica tipo dos argumentos do teste:
  if indices != None and type(indices) != list and type(indices) != tuple:
    erro_prog("Argumento {indices} = %s devia ser None ou lista/tupla" % str(indices))
  if type(idents) != list and type(idents) != tuple:
    erro_prog("Argumento {idents} = %s devis ser lista/tupla" % str(idents))
  if indices == None: indices = () # Para simplificar a lógica.
  if len(indices) != len(idents):
    erro_prog("Tamanhos das listas não batem")

  # Testa {de_lista_de_indices()}:
  idents_cmp = util_identificador.de_lista_de_indices(let, indices)
  sys.stderr.write("  {de_lista_de_indices('%s',%s)} = %s\n" % (let,str(indices),str(idents_cmp)))
  if type(idents_cmp) != list and type(idents_cmp) != tuple:
    sys.stderr.write("  ** devia ser lista/tupla\n")
    ok = False
  else:
    for ident_cmp, ident in zip(idents_cmp, idents):
      if ident != ident_cmp:
        sys.stderr.write("    ** elemento = '%s' devia ser '%s'\n" % (ident_cmp, ident))
        ok = False
  if ok:
    sys.stderr.write("  Teste OK\n")
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'~'*70}\n")
 
let1L = "Z"
indices1L = [ 111, 222, 333, 444 ]
idents1L = [ "Z-00000111", "Z-00000222", "Z-00000333", "Z-00000444"]
testa_funcao_de_lista_de_indices("id_1L", let1L, indices1L, idents1L)

let2L = "N"
indices2L = ()
idents2L = ()
testa_funcao_de_lista_de_indices("id_2L", let2L, indices2L, idents2L)

let3L = "Q"
indices3L = None
idents3L = ()
testa_funcao_de_lista_de_indices("id_3L", let3L, indices3L, idents3L)

# ----------------------------------------------------------------------

def testa_funcao_unico_elemento(rotulo, idents):
  """Testa a função {util_identificador.unico_elemento} na lista de identificadores {idents},
  verificando se devolve {None}, devolve {idents[0]}, ou levanta erro {AssertionError}
  conforme a lista tenha 0, 1, ou mais de 1 elemento.  Se algum teste der errado,
  imprime uma mensagem de erro e desliga a variável global {ok_global}."""
  global ok_global
  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"  Teste {rotulo} idents = {str(idents)}\n")
  ok = True # Estado deste teste.

  # Paranóia: verifica tipo dos argumentos do teste:
  if idents != None and type(idents) != list and type(idents) != tuple:
    erro_prog("Argumento {idents} = %s devis ser {None} ou lista/tupla" % str(idents))

  # Testa {unico_elemento()}:
  sys.stderr.write("  {unico_elemento(%s)} =" % str(idents));
  try:
    ident_cmp = util_identificador.unico_elemento(idents)
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

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  erro_prog("Teste falhou")
