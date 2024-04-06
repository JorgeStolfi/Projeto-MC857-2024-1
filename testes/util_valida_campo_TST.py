#! /usr/bin/python3
import sys, re
from util_testes import erro_prog, aviso_prog
import util_valida_campo
import util_valida_campo
import util_testes
import html_elem_paragraph
from util_testes import erro_prog

import sys

ok_global = True

def validaBoolean(result, rotulo, nulo_ok, val):
  global ok_global
  ok = True

  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"Testando a função boolean\n")
  sys.stderr.write(f"Rotulo: {rotulo}\n")
  sys.stderr.write(f"nulo_ok: {nulo_ok}\n")
  sys.stderr.write(f"val: {val} e tipo {type(val)}\n")

  if nulo_ok:
    if val == None and result != []:
      aviso_prog(f"o erro {result} não esta correto pois a varivel é nula", True)
      ok = False
  else:
    if val ==None and result == []:
      aviso_prog(f"o erro {result} não esta correto a variavel não pode ser nula", True)
      ok = False
    if type(val) is not bool and result == []:
      aviso_prog(f"Resultado {result} incorreto pois variavel não é booleana", True)
      ok = False
    if(type) is bool and result != []:
      aviso_prog(f"Resultado {result} incorreto pois variavel é booleana", True)
      ok = False

  if ok:
    sys.stderr.write("Status: ok")
  else:
    sys.stderr.write("Status: not ok")
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")

def validaIdentificador(result, rotulo, nulo_ok,Letra, val):
  global ok_global
  ok = True

  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"Testando a função Indentificador\n")
  sys.stderr.write(f"Rotulo: {rotulo} \n")
  sys.stderr.write(f"nulo_ok: {nulo_ok} \n")
  sys.stderr.write(f"Letra : {Letra} \n")
  sys.stderr.write(f"val: {val} e tipo {type(val)} \n")
  if nulo_ok:
    if val == None and result != []:
      aviso_prog(f"o erro {result} não esta correto pois a varivel é nula", True)
      ok = False
  else:
    #Negativos

    if result ==[]:
      if type(val) is not str:
        aviso_prog(f"Resultado {result} incorreto pois a val {val} não é uma string", True)
        ok = False
      else:
        n=len(val)
        if n >= 1:
          if val ==None:
            aviso_prog(f"o erro {result} não esta correto a variavel não pode ser nula", True)
            ok = False
          if Letra != None and val[0]!=Letra :
            aviso_prog(f"Resultado {result} incorreto pois a letra {Letra} e diferente do primeiro digito {val[0]}", True)
            ok = False
          if (not re.match(r'^[A-Z]-[0-9]*$', val) or n != 10) :
            aviso_prog(f"Resultado {result} incorreto pois a val {val} e está fora do padrão", True)
            ok = False

    elif result != []:
      if Letra != None and type(val) is str and  val[0] == Letra:
        aviso_prog(f"Resultado {result} incorreto pois a letra {Letra} e igual ao primeiro digito {val[0]}", True)
        ok = False
      if Letra == None and type(val) is str and (re.match(r'^[A-Z]-[0-9]*$', val) and n == 10):
        aviso_prog(f"Resultado {result} incorreto pois a letra é none e a val {val} está dentro dos padrões", True)
        ok = False
    elif result != []:
      aviso_prog(f"Resultado {result} incorreto pois a val {val} está fora do padrão", True)
      ok = False
  if ok:
    sys.stderr.write("Status: ok")
  else:
    sys.stderr.write("Status: not ok")
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")


def validanome_de_usuario(result, rotulo, nulo_ok, val):
  global ok_global
  ok = True

  sys.stderr.write(f"Testando a função Nome de usuário\n")
  sys.stderr.write(f"Rotulo: {rotulo}\n")
  sys.stderr.write(f"nulo_ok: {nulo_ok}\n")
  sys.stderr.write(f"val: {val} e tipo {type(val)}\n")

  if nulo_ok:
    if val == None and result != []:
      aviso_prog(f"o erro {result} não esta correto pois a varivel é nula", True)
      ok = False
  else:
    if type(val) is not str and result == []:
      aviso_prog(f"Resultado {result} incorreto pois a val {val} não é uma string", True)
      ok = False

    if result == []:
      padrao = r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s.'-]+$"
      if val ==None:
        aviso_prog(f"o erro {result} não esta correto a variavel não pode ser nula", True)
        ok = False
      if type(str) is str:
        n = len(val)
        if n < 10:
          aviso_prog(f"Resultado {result} incorreto pois a val {val} tem menos de 10 caracteres", True)
          ok = False
        if n > 60:
          aviso_prog(f"Resultado {result} incorreto pois a val {val} tem mais de 60 caracteres", True)
          ok = False

      if not re.match(padrao, val):
        aviso_prog(f"Resultado {result} incorreto pois a val {val} contem caracteres númericos e/ou especiais", True)
        ok = False
    if result != []:
      if type(val) is str:
        n = len(val)
        if  10 <= n <= 60 and re.match(padrao, val):
          aviso_prog(f"Resultado {result} incorreto pois a val {val} está nos padrões", True)
          ok = False
  if ok:
    sys.stderr.write("Status: ok")
  else:
    sys.stderr.write("Status: not ok")
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")

def validaSenha(result, rotulo, val):
  global ok_global
  ok = True
  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"Testando a função Senha\n")
  sys.stderr.write(f"Rotulo: {rotulo}\n")
  sys.stderr.write(f"val: {val} e tipo {type(val)}\n")

  if type(val) is not str:
    if result ==[]:
      aviso_prog(f"Resultado {result} incorreto pois a val {val} não é string", True)
      ok = False

  else:
    n = len(val)
    if result == []:
      if n < 8:
        aviso_prog(f"Resultado {result} incorreto pois a val {val} tem menos de 8 caracteres", True)
        ok = False
      if n > 16:
        aviso_prog(f"Resultado {result} incorreto pois a val {val} tem mais de 16 caracteres", True)
        ok = False
      if not re.search(r'[A-Z]', val):
        aviso_prog(f"Resultado {result} incorreto pois a val {val} não possui letras maiúsculas", True)
        ok = False
      if not re.search(r'[a-z]', val):
        aviso_prog(f"Resultado {result} incorreto pois a val {val} não possui letras minúsculas", True)
        ok = False
      if not re.search(r'\d', val):
        aviso_prog(f"Resultado {result} incorreto pois a val {val} não possui letras caracteres númericos", True)
        ok = False
      if not re.search(r'[!@#%¨&*()_+{}|:"<>?]]', val):
        aviso_prog(f"Resultado {result} incorreto pois a val {val} não possui letras caracteres especiais", True)
        ok = False
    elif result != []:
      if 8 < n < 16 and re.search(r'[A-Z]', val) and re.search(r'[a-z]', val) and re.search(r'\d', val) and re.search(r'[!@#%¨&*()_+{}|:"<>?]]', val):
        aviso_prog(f"Resultado {result} incorreto pois a val {val} está dentro dos padrões", True)
        ok = False
  if ok:
    sys.stderr.write("Status: ok")
  else:
    sys.stderr.write("Status: not ok")
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")

def validaEmail(result, rotulo, nulo_ok, val):
  global ok_global
  ok = True

  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"Testando a função Nome de usuário\n")
  sys.stderr.write(f"Rotulo: {rotulo}\n")
  sys.stderr.write(f"nulo_ok: {nulo_ok}\n")
  sys.stderr.write(f"val: {val} e tipo {type(val)}\n")
  padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

  if nulo_ok:
    if val == None and result != []:
      aviso_prog(f"o erro {result} não esta correto pois a varivel é nula", True)
      ok = False
  else:
    if result == []:
      if val ==None:
        aviso_prog(f"o erro {result} não esta correto a variavel não pode ser nula", True)
        ok = False
      if type(val) is not str:
        aviso_prog(f"Resultado {result} incorreto pois a val {val} não é uma string", True)
        ok = False
      if not re.match(padrao_email, val):
        aviso_prog(f"Resultado {result} incorreto pois a val {val} está fora dos padrões de email", True)
        ok = False
    elif result != []:
      if type(val) is str and re.match(padrao_email, val) and val != None:
        aviso_prog(f"Resultado {result} incorreto pois a val {val} está dentro dos padrões de email", True)
        ok = False
  if ok:
    sys.stderr.write("Status: ok")
  else:
    sys.stderr.write("Status: not ok")
  ok_global = ok_global and ok
  sys.stderr.write(f"  {'-'*70}\n")

sys.stderr.write(f"  {'-'*70}\n")
sys.stderr.write(f"Inicio dos testes")

#Teste função booleana
rotulo = "Campo booleano"
val = [1, None, True, None]
nulo_ok = [False, False, False, True]
for i in range(len(val)):
  result = util_valida_campo.booleano(rotulo, val[i], nulo_ok[i])
  validaBoolean(result, rotulo, nulo_ok[i], val[i])

#Teste função identificador
rotulo = "identificador"
Letra = ["A", "A", None, None, "A", None, None]
val= ["B-12345678", "A-ABCD", 1, None, "A-12345678", None, "B-12345678"]
nulo_ok = [False, False, False,  False, False, True, False]
for i in range(len(val)):
  result = util_valida_campo.identificador(rotulo, val[i], Letra[i], nulo_ok[i])
  validaIdentificador(result, rotulo, nulo_ok[i],Letra[i],val[i])

#Teste função nome de usuário
rotulo = "Campo Nome de usuario"
val = ['abcd', {'b'*70}, 12, 'Gust2vo', 'Gust@vo', None, "Gustavo Molino", None]
nulo_ok = [False, False, False, False, False, False, False, True]
for i in range(len(val)):
  result = util_valida_campo.nome_de_usuario(rotulo, val[i], nulo_ok[i])
  validanome_de_usuario(result, rotulo, nulo_ok[i], val[i])

#Teste função senhavalidaSenha(result, rotulo, val[i])
rotulo = "Senha"
val = ['abc', 'abcdefghijnlk@#ABDNB', 'abc@12345', 'ABC@12345', 'Abc123456', True, '123Teste@']

for i in range(len(val)):
  result = util_valida_campo.senha(rotulo, val[i])
  validaSenha(result, rotulo, val[i])

#Teste funcao Email
rotulo = "Campo email"
val = [None, 'teste', 1234, 'teste@gmail.com', None]
nulo_ok = [False, False,False,False, True]
for i in range(len(val)):
  result = util_valida_campo.email(rotulo, val[i],nulo_ok[i])
  validaEmail(result, rotulo, nulo_ok[i], val[i])

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
