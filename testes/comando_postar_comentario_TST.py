#! /usr/bin/python3

import obj_comentario

import db_base_sql
import obj_usuario
import obj_sessao
import obj_video
from util_erros import erro_prog, aviso_prog, mostra
import comando_postar_comentario

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

ok_global = True # Vira {False} se um teste falha.

# ----------------------------------------------------------------------
# Função de teste:

def testa_comando(ses, cmd_args, deveria_postar):
  global ok_global

  sys.stderr.write(f"  ----------------------------------------------------------------------\n")
  sys.stderr.write(f"  postando comentário {str(cmd_args)}\n")

  ult_id_old = obj_comentario.ultimo_identificador()
  sys.stderr.write(f"  ultimo comentário antes = {ult_id_old}\n")

  comando_postar_comentario.processa(ses, cmd_args)

  ult_id_new = obj_comentario.ultimo_identificador()
  sys.stderr.write(f"  ultimo comentário depois = {ult_id_new}\n")
  
  if ult_id_new != ult_id_old:
    com_new_obj = obj_comentario.busca_por_identificador(ult_id_new)
    com_new_atrs = obj_comentario.obtem_atributos(com_new_obj) if com_new_obj != None else None
    sys.stderr.write(f"  comentario postado = {com_new_id} atrs = {str(com_new_atrs)}\n")
    if deveria_postar:
      sys.stderr.write("OK\n")
    else:
      sys.stderr.write("** Postou comentario quando não deveria postar\n")
      ok_global = False
  else:
    sys.stderr.write(f"  comentario não postado\n")
    if deveria_postar:
      sys.stderr.write("** Não comentario quando deveria postar\n")
      ok_global = False
    else:
      sys.stderr.write("OK\n")
    
  sys.stderr.write(f"  ----------------------------------------------------------------------\n")

# Limpar as tabelas antes de executar os testes
obj_comentario.inicializa_modulo(True)

# ----------------------------------------------------------------------
# Testa chamada OK:
dados1 = {
    'nome': "Luiz Primeiro", 
    'senha': "123456789", 
    'conf_senha': "123456789",
    'email': "luiz@primeiro.com",
    'administrador': False,
  }
testa_comando(None, dados1, True)

# Testa senha não confere:
dados2 = {
    'nome': "Luiz Segundo", 
    'senha': "123456789", 
    'conf_senha': "987654321",
    'email': "luiz@segundo.com",
    'administrador': False,
  }
testa_comando(None, dados2, False)

# Testa email repetido:
dados3 = {
    'nome': "Luiz Terceiro", 
    'senha': "123456789", 
    'conf_senha': "123456789",
    'email': "luiz@primeiro.com",
    'administrador': True,
  }
testa_comando(None, dados3, False)

# Testa se o teste anterior com senha-nao-confere entrou:
dados4 = {
    'nome': "Luiz Segundo Bis", 
    'senha': "987654321", 
    'conf_senha': "987654321",
    'email': "luiz@segundo.com",
    'administrador': True,
  }
testa_comando(None, dados4, True)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
