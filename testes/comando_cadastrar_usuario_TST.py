#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import obj_usuario
from util_testes import erro_prog, aviso_prog, mostra
import comando_cadastrar_usuario

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def testa_comando_cadastrar_usuario(ses, dados, deveria_cadastrar):
  global ok_global

  sys.stderr.write(f"  ----------------------------------------------------------------------\n")
  sys.stderr.write(f"  cadastrando usuario {dados['nome']} {dados['email']}\n")

  usr_old_id = obj_usuario.busca_por_email(dados["email"])
  usr_old_obj = obj_usuario.busca_por_identificador(usr_old_id)
  usr_old_atrs = obj_usuario.obtem_atributos(usr_old_obj) if usr_old_obj != None else None
  sys.stderr.write(f"  usuario existente = {usr_old_id} atrs = {usr_old_atrs}\n")

  comando_cadastrar_usuario.processa(ses, dados)

  usr_new_id = obj_usuario.busca_por_email(dados["email"])
  usr_new_obj = obj_usuario.busca_por_identificador(usr_new_id)
  usr_new_atrs = obj_usuario.obtem_atributos(usr_new_obj) if usr_new_obj != None else None
  sys.stderr.write(f"  usuario criado = {usr_new_id} atrs = {usr_new_atrs}\n")
  
  if (usr_new_atrs != usr_old_atrs and (not deveria_cadastrar)):
    ok_global = False
    aviso_prog("Cadastrou usuario quando não deveria cadastrar", True)

  if (usr_new_atrs == usr_old_atrs and deveria_cadastrar):
    ok_global = False
    aviso_prog("Não cadastrou usuario quando deveria cadastrar", True)
    
  sys.stderr.write(f"  ----------------------------------------------------------------------\n")

# ----------------------------------------------------------------------
# Testa chamada OK:
dados1 = {
    'nome': "Luiz Primeiro", 
    'senha': "123456789", 
    'conf_senha': "123456789",
    'email': "luiz@primeiro.com",
    'administrador': False,
  }
testa_comando_cadastrar_usuario(None, dados1, True)

# Testa senha não confere:
dados2 = {
    'nome': "Luiz Segundo", 
    'senha': "123456789", 
    'conf_senha': "987654321",
    'email': "luiz@segundo.com",
    'administrador': False,
  }
testa_comando_cadastrar_usuario(None, dados2, False)

# Testa email repetido:
dados3 = {
    'nome': "Luiz Terceiro", 
    'senha': "123456789", 
    'conf_senha': "123456789",
    'email': "luiz@primeiro.com",
    'administrador': True,
  }
testa_comando_cadastrar_usuario(None, dados3, False)

# Testa se o teste anterior com senha-nao-confere entrou:
dados4 = {
    'nome': "Luiz Segundo Bis", 
    'senha': "987654321", 
    'conf_senha': "987654321",
    'email': "luiz@segundo.com",
    'administrador': True,
  }
testa_comando_cadastrar_usuario(None, dados4, True)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  erro_prog("- teste falhou")
