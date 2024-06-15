#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import comando_baixar_video
import obj_sessao
import util_testes
import obj_video
from util_erros import erro_prog, aviso_prog

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
  modulo = comando_baixar_video
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessão cujo usuário é o administrador.
ses_A1_id = "S-00000001"
ses_A1 = obj_sessao.obtem_objeto(ses_A1_id)
assert obj_sessao.de_administrador(ses_A1), f"sessão {ses_A1_id} não é de administrador" 

# Um vídeo:
vid1_id = "V-00000002"

# Teste para baixar um video inválido
inicio = "1"
fim = "2"
testa_processa("VideoInvalido", str, ses_A1, { 'video': None, 'inicio': inicio, 'fim': fim })

# Testa baixar trecho inicio != fim por identificador de vídeo que existe:
inicio = "1"
fim = "2"
testa_processa("BaixarTrechoComSucesso", str, ses_A1, { 'video': vid1_id, 'inicio': inicio, 'fim': fim })

# Testa baixar quadro inicio = fim por identificador de vídeo que existe:
inicio = "1"
fim = "1"
testa_processa("BaixarQuadroComSucesso", str, ses_A1, { 'video': vid1_id, 'inicio': inicio, 'fim': fim })

# Testa baixar quadro fim = None por identificador de vídeo que existe:
inicio = "1"
fim = None
testa_processa("BaixarQuadroComSucessoPorFimNone", str, ses_A1, { 'video': vid1_id, 'inicio': inicio, 'fim': fim })

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
