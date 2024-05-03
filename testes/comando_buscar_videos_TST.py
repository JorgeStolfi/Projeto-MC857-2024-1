#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import comando_buscar_videos
import obj_sessao
import util_testes
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
  modulo = comando_buscar_videos
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessão cujo usuário é o administrador.
ses_admin1_id = "S-00000001"
ses_admin1 = obj_sessao.obtem_objeto(ses_admin1_id)
assert obj_sessao.de_administrador(ses_admin1), f"sessão {ses_admin1_id} não é de administrador" 

# Um vídeo:
vid1_id = "V-00000002"

# Um usuário com vídeos:
usr1_id = "U-00000002"

# Um usuário sem vídeos:
usr2_id = "U-00000003"

# Testa com busca por identificador de vídeo que existe:
testa_processa("video-exT",  str, ses_admin1, { 'video': vid1_id})

# Testa com busca por identificador de vídeo que não existe:
testa_processa("video-exF",  str, ses_admin1, { 'video': "V-12345678"})

# Testa com busca por autor que existe:
testa_processa("autor-exT-com",  str, ses_admin1, { 'autor': usr1_id })

# Testa com busca por autor que existe mas não tem vídeos:
testa_processa("autor-exT-sem",  str, ses_admin1, { 'autor': usr2_id })

# Testa com busca por autor que não existe:
testa_processa("autor-exF",  str, ses_admin1, { 'autor': "U-12345678" })

# Testa com busca por título completo que existe:
testa_processa("titulo-com-full",  str, ses_admin1, { 'titulo': "Fukushima" })

# Testa com busca por título parcial que existe:
testa_processa("titulo-com-part",  str, ses_admin1, { 'titulo': "uku" })

# Testa com busca por título que não existe:
testa_processa("titulo-com-part",  str, ses_admin1, { 'titulo': "Hobbit" })

if ok_global:
  sys.stderr.write("Testes terminados normalmente.")
else:
  aviso_erro("Alguns testes falharam", True)
