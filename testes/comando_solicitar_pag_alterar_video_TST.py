#! /usr/bin/python3

import comando_solicitar_pag_alterar_video
import db_tabelas_do_sistema
import obj_sessao
import obj_video
import db_base_sql
import util_testes
import obj_usuario
import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_solicitar_pag_alterar_video
  funcao = modulo.processa
  frag = False  
  pretty = True 
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

id_ses = "S-00000001"
ses1 = obj_sessao.busca_por_identificador(id_ses)

id_ses = "S-00000003"
ses2 = obj_sessao.busca_por_identificador(id_ses)

# Sessão de usuário administrador
testa_processa("admin",  str, ses1, {'video': 'V-00000001'})

# Sessão de criador do vídeo, não necessariamente admin
testa_processa("criador-do-video",  str, ses1, {'video': 'V-00000001'})

# Sessão de usuário comum que não criou o vídeo
testa_processa("comum-nao-criador",  str, ses2, {'video': 'V-00000001'})

# Sessão sem usuário logado
testa_processa("deslogado",  str, None, {'video': 'V-00000001'})

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
