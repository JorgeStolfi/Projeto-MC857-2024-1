#! /usr/bin/python3
import sys, re
from util_erros import aviso_prog
import util_valida_campo
import util_valida_campo
import util_testes
import html_elem_paragraph

import sys

ok_global = True

def testa_funcao(rot_teste, valido, funcao, *args):
  """Chama a {funcao} do módulo {util_valida_campo} com argumentos {(rot_teste, *args)}.
  Se o resultado for uma lista vazia, avisa que a função diz que {args} é válido.
  Se o resultado for uma lista de strings não-vazia, avisa que a função diz que 
  {args} é inválido, e escreve os strings na pasta "saida" convertidos para HTML
  no arquivo "util_valida_campo.{rot_teste}.html".  
  
  O parâmetro {valido} diz se a {funcao} deveria dizer que o valor {val} em {args}
  é válido ({True}) ou inválido ({False}). Imprime um aviso de erro se o resultado
  de {funcao} discordar deste parâmetro."""
  global ok_global
  
  ok = True # Este teste deu resultado esperado se {True}, innesperado se {False}.
  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"    testando {funcao.__name__}\n")
  sys.stderr.write(f"    rot_teste = '{rot_teste}' args = {str(args)}'\n")
  
  # As funções de {util_valida_campo} não deveriam levantar exceções.

  res = funcao(*args)
  sys.stderr.write(f"    resultado = {str(res)}\n")
  
  if not (type(res) is list or type(res) is tuple):
     sys.stderr.write(f"    ** resultado devia ser lista/tupla\n")
     ok = False
  else:
    if len(res) == 0:
      sys.stderr.write("    resultado vazio - função diz que campo é válido\n")
      if valido:
        sys.stderr.write("    confere!\n")
      else:
        sys.stderr.write("    ** devia dizer que é inválido\n")
        print(f"PROBLEMA AQUI  {rot_teste}\n  {str(res)}\n")

        ok = False
    else:
      sys.stderr.write("    resultado não vazio - função diz que campo é inválido\n")
      if valido:
        sys.stderr.write("    ** devia dizer que é válido\n")
        print(f"PROBLEMA AQUI  {rot_teste}\n  {str(res)}\n")
        ok = False
      else:
        sys.stderr.write("    confere!\n")
      ht_res = list() # Lista de strings HTML com as mensagens de erro.
      for msg in res:
        if type(msg) != str:
          sys.stderr.write(f"    ** mensagem = '{str(res)}' devia ser string\n")
          print(f"PROBLEMA AQUI  {rot_teste}\n {str(res)}\n")

          ok = False
        else:
          ht_msg = html_elem_paragraph.gera(None, msg);
          ht_res.append(ht_msg)
      modulo = util_valida_campo
      frag = True # Resultado é só um fragmento de página?
      pretty = False # Deve formatar o HTML para facilitar view source?
      util_testes.escreve_resultado_html(modulo, rot_teste, ht_res, frag, pretty)
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")

# ==================================# !!! Implementar conforme documentação na interface !!!====================================

func_bool = util_valida_campo.booleano
for val in None, True, False, 410:
  for nulo_ok in False, True:
    valido = type(val) is bool or (val == None and nulo_ok)
    rot_teste = "bool-v" + str(val)[0] + "-n" + str(nulo_ok)[0]
    testa_funcao(rot_teste, valido, func_bool, 'admin', val, nulo_ok)
        
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
          testa_funcao(rot_teste, valido, func_ident, 'produto', val, letra, nulo_ok)
        
# ======================================================================

func_nome = util_valida_campo.nome_de_usuario
for xrot, xvalido, val in \
    ( ( "Nulo",               True,  None,                                     ),
      ( "Valido",             True,  "José da Silvã P. O'Hara Costa-Gravas",   ), 
      ( "ApostInvalido",      False, "José' da Silva P. O'Hara Costa-Gravas",  ),
      ( "ApostInválido",      False, "José da Silva P'. O'Hara Costa-Gravas ", ),
      ( "MuitoCurto",         False, "José", ),
      ( "Incerto",            True,  "Ba'Ana", ),
      ( "Valido",             True,  "Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghij", ),
      ( "MuitoLongo",         False, "José Josefino Josualdo Josismar Josias Josenildo Josafá Josênio", ),
      ( "HifenInvalido",      False, "José-da Silva P. O'Hara Costa-Gravas",    ),
      ( "BrancoInicial",      False, " José da Silva P. O'Hara Costa-Gravas",   ),
      ( "BrancoFinal",        False, "José da Silva P. O'Hara Costa-Gravas ",   ),
      ( "BrancoDuplo",        False, "José da Silva P.  O'Hara Costa-Gravas",   ),
      ( "PontoInválido",      False, "José da Silva P.O'Hara Costa-Gravas ",    ),
      ( "CaracsInvalidos",    False, "Elon X-φ ≥ 17",                           )
    ):
  for nulo_ok in ( False, True ) if (val == None or xrot == "A") else ( False, ):
    if xvalido or ( val != None and not nulo_ok):
      valido = xvalido and (val != None or nulo_ok)
      rot_teste = "nome_" + xrot + "_nulok" + str(nulo_ok)[0] + ("_ok" if valido else "_bad")
      testa_funcao(rot_teste, valido, func_nome, 'padrinho', val, nulo_ok)

# ======================================================================

func_senha = util_valida_campo.senha
testa_funcao("senha_Valida_ok",          True,   func_senha, 'password', "123(meia)4",          True) 
testa_funcao("senha_MuitoCurta_bad",     False,  func_senha, 'password', "123",                 True) 
testa_funcao("senha_MuitoRepetida_bad",  False,  func_senha, 'password', "111111111",           True) 
testa_funcao("senha_SoLetras_bad",       False,  func_senha, 'password', "Segredo",             True) 
testa_funcao("senha_MuitoLonga_bad",     False,  func_senha, 'password', "X"+("a"*60),          True) 

testa_funcao("senha_None_nulokT_ok",   True,   func_senha, 'password', None, True)  
testa_funcao("senha_None_nulokF_bad",  False,  func_senha, 'password', None, False)

func_email = util_valida_campo.email
testa_funcao("email_Valido_ok",          True,   func_email, 'spam-to', "quem_123@ic.u-camp.br", True) 
testa_funcao("email_DuasArrobas_bad",    False,  func_email, 'spam-to', "123@456@onde.br",       True) 
testa_funcao("email_NenhumaArroba_bad",  False,  func_email, 'spam-to', "nenhures",              True) 
testa_funcao("email_HostSemPonto_bad",   False,  func_email, 'spam-to', "tomate@beringela",      True) 
testa_funcao("email_MuitoLonga_bad",     False,  func_email, 'spam-to', "X"+("a"*64)+"@gov.br",  True) 

testa_funcao("email_None_nulokT_ok",   True,   func_email, 'spam-to', None, True) 
testa_funcao("email_None_nulokF_bad",  False,  func_email, 'spam-to', None, False)

func_data = util_valida_campo.data
testa_funcao("data_Valida_ok",             True,   func_data, 'niver', "2024-04-05 20:10:05 UTC",   True) 
testa_funcao("data_ComBarras_bad",         False,  func_data, 'niver', "2024/04/05 20:10:05",       True) 
testa_funcao("data_Ano1899Invalido_bad",   False,  func_data, 'niver', "1899-12-31 20:10:05 UTC",   True) 
testa_funcao("data_Mes00Invalido_bad",     False,  func_data, 'niver', "2024-00-31 20:10:05 UTC",   True) 
testa_funcao("data_Mes13Invalido_bad",     False,  func_data, 'niver', "2024-13-31 20:10:05 UTC",   True) 
testa_funcao("data_Dia00Invalido_bad",     False,  func_data, 'niver', "2024-12-00 20:10:05 UTC",   True) 
testa_funcao("data_Dia32Invalido_bad",     False,  func_data, 'niver', "2024-12-32 20:10:05 UTC",   True) 
testa_funcao("data_Hora24Invalida_bad",    False,  func_data, 'niver', "2024-04-19 24:10:05 UTC",   True) 
testa_funcao("data_Minuto60Invalido_bad",  False,  func_data, 'niver', "2024-04-19 20:60:05 UTC",   True) 
testa_funcao("data_Segundo61Invalido_bad", False,  func_data, 'niver', "2024-04-19 20:10:61 UTC",   True) 
testa_funcao("data_ZonaINvalida_bad",      False,  func_data, 'niver', "2024-04-19 20:10:05 BRL",   True) 

testa_funcao("data_None_nulokT_ok",   True,   func_data, 'niver', None, True) 
testa_funcao("data_None_nulokF_bad",  False,  func_data, 'niver', None, False)

func_titulo_video = util_valida_campo.titulo_de_video
#positivo
testa_funcao("titulo_valido_ok", True, func_titulo_video, 'titulo', 'Velozes e Furiosos 2', True)
testa_funcao("titulo_validoNone_ok", True, func_titulo_video, 'titulo', None, True)

#Negativo
testa_funcao("titulo_menos10Caracteres_bad", False, func_titulo_video, 'titulo', 'Val', True)
testa_funcao("titulo_mais60_Caracteres_bad", False, func_titulo_video, 'titulo',("a"*62), True)
testa_funcao("titulo_caracterNaoIso_bad", False, func_titulo_video,'titulo', 'Titulo Sem ISO ぁ', True)
testa_funcao("titulo_primeiraLetraMinuscula_bad", False, func_titulo_video,'titulo', 'titulo minusculo comeco', True)
testa_funcao("titulo_finalBranco_bad", False, func_titulo_video, 'titulo','Titulo final branco  ', True)
testa_funcao("titulo_duploBranco_bad", False, func_titulo_video, 'titulo','Titulo duplo  branco', True)

# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
