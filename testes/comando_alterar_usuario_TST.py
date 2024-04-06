#! /usr/bin/python3

import comando_alterar_usuario
import db_tabelas
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes
from util_testes import ErroAtrib

import sys

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Obtem sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")

def testa_comando_alterar_usuario(rotulo, *args):
  """Testa {funcao(*cmd_args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_alterar_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
    
def testa_atualiza_nome_com_sucesso():
  novo_nome = "John First"
  cmd_args = {
      'id_usuario': "U-00000001",
      'nome': novo_nome,
  }
  testa_comando_alterar_usuario("Nom", ses, cmd_args)

  updated_user = obj_usuario.busca_por_identificador("U-00000001")

  assert obj_usuario.obtem_atributo(updated_user, "nome") == novo_nome, "nome não atualizado"

def testa_atualiza_email_com_sucesso():
  email_novo = "banana@nanica.com"
  cmd_args = {
      'id_usuario': "U-00000001",
      'email': email_novo,
  }
  testa_comando_alterar_usuario("Ema", ses, cmd_args)

  updated_user = obj_usuario.busca_por_identificador("U-00000001")

  assert obj_usuario.obtem_atributo(updated_user, "email") == email_novo, "email não atualizado"

def testa_atualiza_email_repetido_falha():
  email_dup = "segundo@gmail.com"
  cmd_args = {
      'id_usuario': "U-00000001",
      'email': email_dup,
  }
  try:
    testa_comando_alterar_usuario("Dup", ses, cmd_args)
  except ErroAtrib as ex:
    msg = ex.atrs[0]
    mostra(4, f"testa_comando_alterar_usuario: erro = \"{str(msg)}\"")
    sys.stderr.write("    (erro esperado)\n")

  updated_user = obj_usuario.busca_por_identificador("U-00000001")
  assert obj_usuario.obtem_atributo(updated_user, "email") != email_dup, "email duplicado aceito"

# Executa os testes

testa_atualiza_nome_com_sucesso()
testa_atualiza_email_com_sucesso()
testa_atualiza_email_repetido_falha()

sys.stderr.write("Testes terminados normalmente.\n")
