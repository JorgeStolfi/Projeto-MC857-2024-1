#! /usr/bin/python3

import util_identificador
import util_testes
from util_erros import ErroAtrib, erro_prog, mostra
import sys, re

ok_global = True  # Vira {False} se houver erro.

# ======================================================================
# Testa funções de conversão simples:

def testa_funcoes_de_para_indice(rot_teste, let, indice, ident):
  """Testa as funções {util_identificador.de_indice(let,indice)} e 
  {util_identificador.para_indice(let, ident)}, verificando se o resultado
  de uma é o argumento da outra.  Se algum teste der errado,
  imprime uma mensagem de erro, e desliga a variável global {ok_global}."""
  global ok_global
  ok = True # Estado deste teste.
  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"  teste {rot_teste} let = '{let}' indice = {str(indice)} ident = '{str(ident)}'\n")
  
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

# ======================================================================
# Testa funções de conversão de listas:

def testa_funcao_de_lista_de_indices(rot_teste, let, indices, idents):
  """Testa a função {util_identificador.de_lista_de_indices} na lista de inteiros {indices},
  verificando se o resultado é a lista de identificadores {idents}.  Se algum teste der errado,
  imprime uma mensagem de erro e desliga a variável global {ok_global}."""
  global ok_global
  sys.stderr.write(f"  {'~'*70}\n")
  sys.stderr.write(f"  Teste {rot_teste} (lista) let = '{let}' indices = {str(indices)} idents = {str(idents)}\n")
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


# ======================================================================
# Testa função de validação:

modulo = util_identificador
funcao = modulo.valida
chave = 'produto'
for letra in "C", "ZZ":
  for num in "-00000000", "-000000001", "-99999999", "-0123456", "0123456789", "-0123X567" "_01234567", " -01234567", "- 01234567":
    for val in f"{letra}{num}", f"Z{num}", None, 418:
      for nulo_ok in ( False, True ) if ( val == None or val == "C-00000000" ) else ( False, ):
        if (val != None and val != 418) or (num == "-00000000" and letra == "C"):
          rot_teste = "ident_val" + str(val) + "_" + letra + "_nuok" + str(nulo_ok)[0]
          rot_teste = re.sub(r' ', "%20", rot_teste)
          if val == None:
            valido = nulo_ok
          elif type(val) is not str:
            valido = False
          else:
            valido = \
              re.match(r"^[A-Z]$", letra) and \
              re.match(r"^[A-Z][-][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", val) and \
              val[0] == letra
          ok = util_testes.testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, val, letra, nulo_ok)
          if not ok: ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
