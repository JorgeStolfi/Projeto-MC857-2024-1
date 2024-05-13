#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import comando_buscar_usuarios
import obj_sessao
import util_testes
import obj_usuario

import sys

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global

  modulo = comando_buscar_usuarios
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessão cujo usuário é o administrador.
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)
assert obj_sessao.de_administrador(sesA), f"sessão {sesA_id} não é de administrador" 

# Sessão cujo usuário é comum (não) administrador.
sesC_id = "S-00000003"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert not obj_sessao.de_administrador(sesC), f"sessão {sesC_id} é de administrador" 

for ses in None, sesA, sesC:

  admin = obj_sessao.de_administrador(ses) if ses != None else False
  rad = "sesN_" if ses == None else f"ses{str(admin)[0]}_"

  # Testa com busca por identificador_que existe:
  args_id_usr = {'usuario': "U-00000002"}
  testa_processa(rad + "usuario",    str, ses, args_id_usr)

  # Testa com busca por email que existe:
  args_email = {'email': "primeiro@gmail.com"}
  testa_processa(rad + "email_ok",   str, ses, args_email)

  # Testa com busca por email que não existe:
  args_email_no = {'email': "naoexiste@email.com"}
  testa_processa(rad + "email_no",   str, ses, args_email_no)

  # --- Testes abaixo devem retornar somente "João Segundo" ---

  # Testa com busca por nome que existe:
  args_nome = {'nome': "João Segundo"}
  testa_processa(rad + "nome",             str, ses, args_nome)

  # Testa com busca por primeiro nome:
  args_primeiro_nome = {'nome': "João"}
  testa_processa(rad + "primeiro_nome",    str, ses, args_primeiro_nome)

  # Testa com busca por sobrenome:
  args_sobrenome = {'nome': "Segundo"}
  testa_processa(rad + "sobrenome",        str, ses, args_sobrenome)

  # Testa com nome aproximado:
  args_nome_aproximado = {'nome': "joão segundo"}
  testa_processa(rad + "nome_aproximado",  str, ses, args_nome_aproximado)

  # --- Testes abaixo devem retornar somente "João Segundo" ---

  # Teste abaixo deve retornar todos usuários que começam com "Jo"
  # (José Primeiro, João Segundo, Josenildo Quinto, Joaquim Oitavo e Jonas Nono)
  args_nome_parcial = {'nome': "jo"}
  testa_processa(rad + "nome_parcial",  str, ses, args_nome_parcial)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.")
else:
  aviso_prog("Alguns testes falharam", True)
