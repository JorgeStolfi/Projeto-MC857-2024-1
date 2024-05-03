#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import obj_usuario
from util_erros import erro_prog, aviso_prog, mostra
import comando_cadastrar_usuario

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

ok_global = True # Vira {False} se um teste falha.

# ======================================================================
def testa_msg_campo_obrigatorio(nome_do_campo):
  global ok_global

  sys.stderr.write(f"  ----------------------------------------------------------------------\n")
  sys.stderr.write(f"  testando mensagem de campo obrigatóro para {nome_do_campo}\n")

  resposta = comando_cadastrar_usuario.msg_campo_obrigatorio(nome_do_campo)

  sys.stderr.write(f"  mensagem retornada = {resposta}\n")

  if (resposta != "O campo %s é obrigatório." % nome_do_campo):
    ok_global = False
    aviso_prog("Mensagem retornada errada", True)

  sys.stderr.write(f"  ----------------------------------------------------------------------\n")

nome_campo_1 = "Nome"
testa_msg_campo_obrigatorio(nome_campo_1)

nome_campo_2 = "Senha"
testa_msg_campo_obrigatorio(nome_campo_2)

# ======================================================================
def testa_processa(rot_teste, ses, cmd_args, deveria_cadastrar):
  """Testa {comando_cadastrar_usuario.processa(ses, cmd_args})}.
  O resultado deve ser um string (página). Verifica se o usuário
  foi realmente cadastrado: se {deveria_cadastrar} é {True}
  espera que sim, se for {False} espera que não. Grava a página 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  
  ok = True
  
  modulo = comando_cadastrar_usuario
  funcao = processa
  
  # Verifica se já existe usuário com esse email:
  usr_old_id = obj_usuario.busca_por_email(cmd_args["email"])
  usr_old = obj_usuario.obtem_objeto(usr_old_id) if usr_old_id != None else None
  usr_old_atrs = obj_usuario.obtem_atributos(usr_old) if usr_old != None else None
  if usr_old_id != None:
    sys.stderr.write(f"  usuario existente com esse email = {usr_old_id} atrs = {usr_old_atrs}\n")

  res_esp = str
  frag = False
  pretty = True
  ok = ok and util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, ses, cmd_args) 

  usr_new_id = obj_usuario.busca_por_email(cmd_args["email"])
  usr_new = obj_usuario.obtem_objeto(usr_new_id) if usr_new_id != None else None
  usr_new_atrs = obj_usuario.obtem_atributos(usr_new) if usr_new != None else None
  if usr_new_id != None:
    sys.stderr.write(f"  usuario criado = {usr_new_id} atrs = {usr_new_atrs}\n")
    if not 
  
  if usr_old_id != None:
    if usr_new_id != usr_old_id:
      aviso_prog(f"Cadastrou dois usuários com mesmo email\n")
      ok = False
    else:
      if deveria_cadastrar:
        erro_prog(f"Parâmetro {'{'}deveria_cadastrar{'{'} = {deveria_cadastrar} inconsistente\n")
        ok = False
  else:
    if usr_new_id != None and not deveria_cadastrar:
      aviso_prog("Cadastrou usuario quando não deveria cadastrar", True)
      ok = False
    elif usr_new_id == None and deveria_cadastrar:
      aviso_prog("Não cadastrou usuario quando deveria cadastrar", True)
      ok = False

  ok_global = ok_global and ok
  return ok  

# Limpar as tabelas antes de executar os testes
obj_usuario.inicializa_modulo(True)

# ----------------------------------------------------------------------
# Testa chamada OK:
cmd_args1 = {
    'nome': "Luiz Primeiro", 
    'senha': "a!23456789", 
    'conf_senha': "a!23456789",
    'email': "luiz@primeiro.com",
    'administrador': False,
  }
testa_processa("T1-gud", None, cmd_args1, True)

# Testa senha não confere:
cmd_args2 = {
    'nome': "Luiz Segundo", 
    'senha': "123456789", 
    'conf_senha': "987654321",
    'email': "luiz@segundo.com",
    'administrador': False,
  }
testa_processa("T2-bad", None, cmd_args2, False)

# Testa email repetido:
cmd_args3 = {
    'nome': "Luiz Primeiro Funcional",
    'senha': "123456789",
    'conf_senha': "123456789",
    'email': "luiz@primeiro.com",
    'administrador': True,
  }
testa_processa("T3-bad", None, cmd_args3, False)

# Testa se o teste anterior com senha-nao-confere entrou:
cmd_args4 = {
    'nome': "Luiz Segundo Bis", 
    'senha': "98765432!a", 
    'conf_senha': "98765432!a",
    'email': "luiz@segundo.com",
    'administrador': True,
  }
testa_processa("T4-gud", None, cmd_args4, True)

# Testa senha fraca (somente números)
cmd_args5 = {
    'nome': "Luiz Quinto", 
    'senha': "12345678", 
    'conf_senha': "12345678",
    'email': "luiz@quinto.com",
    'administrador': False,
  }
testa_processa("T5-bad", None, cmd_args5, False)

# Testa senha fraca (somente números e letras)
cmd_args6 = {
    'nome': "Luiz Sexto", 
    'senha': "12345abcde", 
    'conf_senha': "12345abcde",
    'email': "luiz@sexto.com",
    'administrador': False,
  }
testa_processa("T6-bad", None, cmd_args6, False)

# Testa senha fraca (muito curta)
cmd_args7 = {
    'nome': "Luiz Sétimo", 
    'senha': "123", 
    'conf_senha': "123",
    'email': "luiz@sehtimo.com",
    'administrador': False,
  }
testa_processa("T7-bad", None, cmd_args7, False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
