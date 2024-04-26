#! /usr/bin/python3

import comando_alterar_usuario
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes
from util_erros import ErroAtrib

import sys

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_alterar_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
# Obtem sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")
  
def testa_atualiza_nome_com_sucesso():
  novo_nome = "John First"
  cmd_args = {
      'usuario': "U-00000001",
      'nome': novo_nome,
  }
  testa_processa("Nome-OK", str, ses, cmd_args)
  updated_user = obj_usuario.busca_por_identificador("U-00000001")
  assert obj_usuario.obtem_atributo(updated_user, "nome") == novo_nome, "nome não atualizado"

def testa_atualiza_email_com_sucesso():
  email_novo = "banana@nanica.com"
  cmd_args = {
      'usuario': "U-00000001",
      'email': email_novo,
  }
  testa_processa("Email-OK", str, ses, cmd_args)
  updated_user = obj_usuario.busca_por_identificador("U-00000001")
  assert obj_usuario.obtem_atributo(updated_user, "email") == email_novo, "email não atualizado"

def testa_atualiza_email_repetido_falha():
  email_dup = "segundo@gmail.com"
  cmd_args = {
    'usuario': "U-00000001",
    'email': email_dup,
  }
  testa_processa("Email-Dup", str, ses, cmd_args)

  updated_user = obj_usuario.busca_por_identificador("U-00000001")
  assert obj_usuario.obtem_atributo(updated_user, "email") != email_dup, "email duplicado aceito"

# Executa os testes

testa_atualiza_nome_com_sucesso()
testa_atualiza_email_com_sucesso()
testa_atualiza_email_repetido_falha()

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
