#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import comando_buscar_comentarios_de_usuario
import obj_sessao
import util_testes
import obj_usuario
import obj_video

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
  modulo = comando_buscar_comentarios_de_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
# Sessão cujo usuário é o administrador.
ses_adm_id = "S-00000001"
ses_adm = obj_sessao.obtem_objeto(ses_adm_id)

# Teste passando um id do usuário
usr1_id = {'usuario': "U-00000002"}

testa_processa("T1",         str, ses_adm, usr1_id)

# Testa a visualização dos próprios comentários
testa_processa("T2",         str, ses_adm, {})

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
