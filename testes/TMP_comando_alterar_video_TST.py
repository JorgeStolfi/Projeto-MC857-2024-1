#! /usr/bin/python3

import comando_alterar_video
import obj_video
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes
import db_tabelas_do_sistema
from util_erros import erro_prog

import sys

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, compara com {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_alterar_video
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Obtem sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")
assert obj_sessao.de_administrador(ses)
ses_nao_admin = obj_sessao.busca_por_identificador('S-00000003')
assert not obj_sessao.de_administrador(ses_nao_admin)

# Obtem um vídeo de teste
video = obj_video.busca_por_autor("U-00000001")[0]
assert video != None

# Obtem o usuario admin
usr = obj_usuario.busca_por_identificador("U-00000001")
assert usr != None

# Acesso à página com uma sessão None (inválida)
testa_processa("Sessao-None", str, None, { 'video': 'V-00000001' })

# Acesso à página com uma sessão fechada
ses_fechada = obj_sessao.busca_por_identificador("S-00000003")
testa_processa("Sessao-Fechada", str, ses_fechada, { 'video': 'V-00000001' })

# Acesso à página sem enviar o identificador do vídeo
testa_processa("Sem-Especificar-Video", str, ses, {})

# Administrador editando vídeo de autoria de outro usuário
testa_processa("Usr_Admin_Video_De_Outro_Usuario", str, ses, { 'video': 'V-00000002' })

# Não administrador editando o vídeo de sua própria autoria
testa_processa("Usr_Nao_Admin_Video_Proprio", str, ses_nao_admin, { 'video': 'V-00000002' })

# Não administrador editando o vídeo de autoria de um outro usuário
testa_processa("Usr_Nao_Admin_Video_Outro_Usuario", str, ses_nao_admin, { 'video': 'V-00000003' })

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  erro_prog("Alguns testes falharam")
