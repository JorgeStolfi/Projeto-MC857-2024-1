#! /usr/bin/python3

import util_valida_campo
import util_testes
import html_elem_paragraph
from util_testes import erro_prog

import sys

ok_global = True

def testa_funcao(rotulo, valido, funcao, *args):
  """Chama a {funcao} do módulo {util_valida_campo} com argumentos {(rotulo, *args)}.
  Se o resultado for uma lista vazia, avisa que a função diz que {args} é válido.
  Se o resultado for uma lista de strings não-vazia, avisa que a função diz que 
  {args} é inválido, e escreve os strings na pasta "saida" convertidos para HTML
  no arquivo "util_valida_campo.{rotulo}.html".  
  
  O parâmetro {valido} diz se a {funcao} deveria dizer que o valor {val} em {args}
  é válido ({True}) ou inválido ({False}). Imprime um aviso de erro se o resultado
  de {funcao} discordar deste parâmetro."""
  global ok_global
  
  ok = True # Este teste deu resultado esperado se {True}, innesperado se {False}.
  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"    rotulo = '{rotulo}' args = {str(args)}'\n")
  
  # As funções de {util_valida_campo} não deveriam levantar exceções.
  res = funcao(rotulo, *args)
  if not (type(res) is list or type(res) is tuple):
     sys.stderr.write(f"    ** resultado = '{str(res)}' devia ser lista/tupla\n")
     ok = False
  else:
    if len(res) == 0:
      sys.stderr.write("    resultado vazio - função diz que campo é válido\n")
      if valido:
        sys.stderr.write("    confere!\n")
      else:
        sys.stderr.write("    ** devia dizer que é inválido\n")
        ok = False
    else:
      sys.stderr.write("    resultado não vazio - função diz que campo é inválido\n")
      if valido:
        sys.stderr.write("    ** devia dizer que é válido\n")
        ok = False
      else:
        sys.stderr.write("    confere!\n")
      ht_res = list() # Lista de strings HTML com as mensagens de erro.
      for msg in res:
        if type(msg) != str:
          sys.stderr.write(f"    ** mensagem = '{str(res)}' devia ser string\n")
          ok = False
        else:
          ht_msg = html_elem_paragraph.gera(None, msg);
          ht_res.append(ht_msg)
      modulo = util_valida_campo
      frag = True # Resultado é só um fragmento de página?
      pretty = False # Deve formatar o HTML para facilitar view source?
      util_testes.escreve_resultado_html(modulo, rotulo, ht_res, frag, pretty)
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")
  
# Tests:

func_booleano = util_valida_campo.booleano
testa_funcao("bool_T_ok",   True,  func_booleano, True, True)  # Valor {True}.
testa_funcao("bool_T_ok",   True,  func_booleano, False, True) # Valor {False}.

testa_funcao("bool_N_ok",   True,  func_booleano, None, True)  # Valor {None}, {none_ok=True}.  
testa_funcao("bool_N_bad" , False, func_booleano, None, False) # Valor {None}, {none_ok=False}.

func_id = util_valida_campo.identificador
testa_funcao("id_A_ok",   True,   func_id, "M-12345678",  "M", True)  # Identificador válido.

testa_funcao("id_B_bad",  False,  func_id, "X-12345678",  "M", True)  # Letra errada.
testa_funcao("id_C_bad",  False,  func_id, "M-5678",      "M", True)  # Poucos dígitos.
testa_funcao("id_D_bad",  False,  func_id, "M-123456789", "M", True)  # Muitos dígitos.
testa_funcao("id_E_bad",  False,  func_id, "M_123456789", "M", True)  # Hifen errado.
testa_funcao("id_F_bad",  False,  func_id, "M- 123f5678", "M", True)  # caracteres inválidos.

testa_funcao("id_N_ok",   True,   func_id, None,          "M", True)  # Valor {None}, {none_ok=True}. 
testa_funcao("id_N_bad",  False,  func_id, None,          "M", False) # Valor {None}, {none_ok=False}.

func_nome = util_valida_campo.nome_de_usuario
testa_funcao("nome_A_ok",   True,   func_nome, "José A. São-Bóiça O'Hara",  True)  # Nome válido.
testa_funcao("nome_B_bad",  False,  func_nome, "Pitomba 1234",              True)  # Caracs invalidos.
testa_funcao("nome_C_bad",  False,  func_nome, "Elon X-φ ≥ 17",             True)  # Caracs invalidos.
testa_funcao("nome_D_bad",  False,  func_nome, "Pedro",                     True)  # Muito curto.
testa_funcao("nome_E_bad",  False,  func_nome, "X"+("a"*60),                True)  # Muito longo.

testa_funcao("nome_N_ok",   True,   func_nome, None,                        True)  # Valor {None}, {none_ok=True}.
testa_funcao("nome_N_bad",  False,  func_nome, None,                        False) # Valor {None}, {none_ok=False}.

func_senha = util_valida_campo.senha
testa_funcao("senha_A_ok",   True,   func_senha, "123(meia)4",          True)  # Senha válida.
testa_funcao("senha_B_bad",  False,  func_senha, "123",                 True)  # Muito curta.
testa_funcao("senha_C_bad",  False,  func_senha, "111111111",           True)  # Muito repetida.
testa_funcao("senha_D_bad",  False,  func_senha, "Segredo",             True)  # Só letras.
testa_funcao("senha_E_bad",  False,  func_senha, "X"+("a"*60),          True)  # Muito longa.

testa_funcao("senha_N_ok",   True,   func_senha, None,                  True)  
testa_funcao("senha_N_bad",  False,  func_senha, None,                  False) # Valor {None}, {none_ok=True}. 

func_email = util_valida_campo.email
testa_funcao("email_A_ok",   True,   func_email, "quem_123@ic.u-camp.br", True)  # Email válido.
testa_funcao("email_B_bad",  False,  func_email, "123@456@onde.br",       True)  # Duas "@".
testa_funcao("email_C_bad",  False,  func_email, "nenhures",              True)  # Nenhuma "@".
testa_funcao("email_D_bad",  False,  func_email, "tomate@beringela",      True)  # Host sem ".".
testa_funcao("email_E_bad",  False,  func_email, "X"+("a"*60)+"@gov.br",  True)  # Muito longa.

testa_funcao("email_N_ok",   True,   func_email, None,                  True)  # Valor {None}, {none_ok=True}. 
testa_funcao("email_N_bad",  False,  func_email, None,                  False) # Valor {None}, {none_ok=False}.

func_data = util_valida_campo.data
testa_funcao("data_A_ok",   True,   func_data, "2024-04-05 20:10:05 UTC",   True)  # Data válida.
testa_funcao("data_B_bad",  False,  func_data, "2024/04/05 20:10:05",       True)  # Data em formato inválido.
testa_funcao("data_C_bad",  False,  func_data, "2024-13-32 20:10:05 UTC",   True)  # Data com range (date) inválido.
testa_funcao("data_D_bad",  False,  func_data, "2024-04-05 20:62:05 UTC",   True)  # Data com range (hora) inválido.

testa_funcao("senha_N_ok",   True,   func_data, None,                  True)  
testa_funcao("senha_N_bad",  False,  func_data, None,                  False) # Valor {None}, {none_ok=True}. 
# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  erro_prog("- teste falhou")

