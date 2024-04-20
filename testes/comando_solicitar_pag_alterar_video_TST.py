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

def testa_comando_solicitar_pag_alterar_video(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = comando_solicitar_pag_alterar_video
  funcao = modulo.processa
  frag = False  
  pretty = True 
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

id_ses = "S-00000001"
ses1 = obj_sessao.busca_por_identificador(id_ses)

id_ses = "S-00000003"
ses2 = obj_sessao.busca_por_identificador(id_ses)

# Sessão de usuário administrador
testa_comando_solicitar_pag_alterar_video("admin", ses1, {'video': 'V-00000001'})

# Sessão de criador do vídeo, não necessariamente admin
testa_comando_solicitar_pag_alterar_video("criador-do-video", ses1, {'video': 'V-00000001'})

# Sessão de usuário comum que não criou o vídeo
testa_comando_solicitar_pag_alterar_video("comum-nao-criador", ses2, {'video': 'V-00000001'})

# Sessão sem usuário logado
testa_comando_solicitar_pag_alterar_video("deslogado", None, {'video': 'V-00000001'})

sys.stderr.write("Testes terminados normalmente.\n")
