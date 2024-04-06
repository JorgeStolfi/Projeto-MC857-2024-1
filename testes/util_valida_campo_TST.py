#! /usr/bin/python3
import sys, re
from util_testes import erro_prog, aviso_prog
import util_valida_campo

ok_global = True #vira false se encontrar um erro

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
