#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import comando_buscar_sessoes
import obj_sessao
import obj_usuario
import util_testes
from util_erros import aviso_prog

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
  modulo = comando_buscar_sessoes
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

rad = "busca_sessao_"

# Testa com busca sem estar logado:
ses = None
args_id_usr = {'dono': "U-00000001"}
testa_processa(rad + "deslogado",    str, ses, args_id_usr)

# Sessão cujo usuário é o administrador.
ses_id = "S-00000001"
ses = obj_sessao.obtem_objeto(ses_id)
assert obj_sessao.de_administrador(ses), f"sessão {ses_id} não é de administrador" 

# Testa com busca por dono de duas sessões:
args_id_usr = {'dono': "U-00000001"}
testa_processa(rad + "dono", str, ses, args_id_usr)

# Testa com busca por sessão por id:
args_sessao = {'sessao': "S-00000003"}
testa_processa(rad + "sessao", str, ses, args_sessao)

# Testa com busca por toda sessão aberta:
args_aberta = {'aberta': "on"}
testa_processa(rad + "aberta", str, ses, args_aberta)

# Testa com busca por data específica:
args_criacao = {'criacao': "2024-01-06 08:33:25 UTC"}
testa_processa(rad + "criacao", str, ses, args_criacao)

# Testa com busca por intervalo de data:
args_intervalo = {'data_min': "2024-01-02 08:33:25 UTC", 'data_max': "2024-01-04 08:33:25 UTC"}
testa_processa(rad + "intervalo", str, ses, args_intervalo)

# Testa com busca por cookie:
args_cookie = {'cookie': "DEFGHIJKLMN"}
testa_processa(rad + "cookie", str, ses, args_cookie)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
