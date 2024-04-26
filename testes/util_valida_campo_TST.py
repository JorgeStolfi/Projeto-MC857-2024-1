#! /usr/bin/python3
import sys, re
from util_erros import aviso_prog
import util_valida_campo
import util_testes
import html_elem_paragraph

import sys

ok_global = True

# !!! Reescrever usando util_testes.testa_funcao !!!

def testa_funcao_validadora(rot_teste, valido, funcao, *args):
  """Chama a {funcao} do módulo {util_valida_campo} com argumentos {*args},
  e verifica o resultado.  Se {valido} é {True}, espera uma lista vazia;
  se {valido} é {False}, espera uma lista de uma ou mais strings.
  Também escreve o resultado, convertido para HTML, na pasta "saida",
  arquivo "util_valida_campo.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = util_valida_campo
  html = False   # Resultados string jã são HTML?
  frag = False   # Resultados string são só fragmentos de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  res_esp = [] if valido else list
  ok = util_testes.testa_funcao(rot_teste, modulo, funcao, res_esp, html, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# ==================================# !!! Implementar conforme documentação na interface !!!====================================

func_bool = util_valida_campo.booleano
for val in None, True, False, 410:
  for nulo_ok in False, True:
    valido = type(val) is bool or (val == None and nulo_ok)
    rot_teste = "bool-v" + str(val)[0] + "-n" + str(nulo_ok)[0]
    testa_funcao_validadora(rot_teste, valido, func_bool, 'admin', val, nulo_ok)
        
# ======================================================================

func_ident = util_valida_campo.identificador
for letra in "C", "ZZ":
  for num in "-00000000", "-000000001", "-99999999", "-0123456", "0123456789", "-0123X567" "_01234567", " -01234567", "- 01234567":
    for val in f"{letra}{num}", f"Z{num}", None, 418:
      for nulo_ok in ( False, True ) if ( val == None or val == "C-00000000" ) else ( False, ):
        if (val != None and val != 418) or (num == "-00000000" and letra == "C"):
          rot_teste = "ident-" + str(val) + "-" + letra + "-n" + str(nulo_ok)[0]
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
          testa_funcao_validadora(rot_teste, valido, func_ident, 'produto', val, letra, nulo_ok)
        
func_data = util_valida_campo.data
testa_funcao_validadora("data_Valida_ok",             True,   func_data, 'niver', "2024-04-05 20:10:05 UTC",   True) 
testa_funcao_validadora("data_ComBarras_bad",         False,  func_data, 'niver', "2024/04/05 20:10:05",       True) 
testa_funcao_validadora("data_Ano1899Invalido_bad",   False,  func_data, 'niver', "1899-12-31 20:10:05 UTC",   True) 
testa_funcao_validadora("data_Mes00Invalido_bad",     False,  func_data, 'niver', "2024-00-31 20:10:05 UTC",   True) 
testa_funcao_validadora("data_Mes13Invalido_bad",     False,  func_data, 'niver', "2024-13-31 20:10:05 UTC",   True) 
testa_funcao_validadora("data_Dia00Invalido_bad",     False,  func_data, 'niver', "2024-12-00 20:10:05 UTC",   True) 
testa_funcao_validadora("data_Dia32Invalido_bad",     False,  func_data, 'niver', "2024-12-32 20:10:05 UTC",   True) 
testa_funcao_validadora("data_Hora24Invalida_bad",    False,  func_data, 'niver', "2024-04-19 24:10:05 UTC",   True) 
testa_funcao_validadora("data_Minuto60Invalido_bad",  False,  func_data, 'niver', "2024-04-19 20:60:05 UTC",   True) 
testa_funcao_validadora("data_Segundo61Invalido_bad", False,  func_data, 'niver', "2024-04-19 20:10:61 UTC",   True) 
testa_funcao_validadora("data_ZonaINvalida_bad",      False,  func_data, 'niver', "2024-04-19 20:10:05 BRL",   True) 

testa_funcao_validadora("data_None_nulokT_ok",   True,   func_data, 'niver', None, True) 
testa_funcao_validadora("data_None_nulokF_bad",  False,  func_data, 'niver', None, False)

func_titulo_video = util_valida_campo.titulo_de_video
#positivo
testa_funcao_validadora("titulo_valido_ok",      True,   func_titulo_video, 'titulo', 'Velozes e Furiosos 2', True)
testa_funcao_validadora("titulo_validoNone_ok",  True,   func_titulo_video, 'titulo', None,                   True)

#Negativo
testa_funcao_validadora("titulo_menos10Caracteres_bad",      False, func_titulo_video, 'titulo', 'Val', True)
testa_funcao_validadora("titulo_mais60_Caracteres_bad",      False, func_titulo_video, 'titulo', ("a"*62), True)
testa_funcao_validadora("titulo_caracterNaoIso_bad",         False, func_titulo_video, 'titulo', 'Titulo Sem ISO ぁ', True)
testa_funcao_validadora("titulo_primeiraLetraMinuscula_bad", False, func_titulo_video, 'titulo', 'titulo minusculo comeco', True)
testa_funcao_validadora("titulo_finalBranco_bad",            False, func_titulo_video, 'titulo', 'Titulo final branco  ', True)
testa_funcao_validadora("titulo_duploBranco_bad",            False, func_titulo_video, 'titulo', 'Titulo duplo  branco', True)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
