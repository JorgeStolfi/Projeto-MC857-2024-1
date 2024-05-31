#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import obj_video
import obj_raiz
import util_testes
from util_erros import erro_prog, aviso_prog, mostra
import comando_fazer_upload_video

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se um teste falha.

def testa_processa(rot_teste, valido, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global

  ult_id_antes = obj_video.ultimo_identificador()
  
  modulo = comando_fazer_upload_video
  funcao = comando_fazer_upload_video.processa
  frag = False
  pretty = False
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, str, frag, pretty, *args)
  
  ult_id_depois = obj_video.ultimo_identificador()
  sys.stderr.write(f"  ultimo id antes = {ult_id_antes} depois = {ult_id_depois}\n")

  if ult_id_depois == ult_id_antes:
    sys.stderr.write(f"  comando não criou novo video\n")
    if valido:
      sys.stderr.write(f"  ** deveria ter criado!\n")
      ok = False
    else:
      sys.stderr.write(f"  como esperado\n")
  else:
    sys.stderr.write(f"  comando criou novo video, id = {ult_id_depois}\n")
    if valido:
      sys.stderr.write(f"  como esperado\n")
      ok = verifica_criacao(rot_teste, ult_id_depois, *args)
    else:
      sys.stderr.write(f"  ** deveria ter falhado!\n")
      ok = False
  
  ok_global = ok_global and ok
  return ok
  
def verifica_criacao(rot_teste, vid_id, ses, cmd_args):
  """Confere atributos do vídeo {vid_id} criado com os dados
  especificados {cmd_args}."""
  global ok_global

  ok = True

  assert ses != None and obj_sessao.aberta(ses)
  ses_id = obj_sessao.obtem_identificador(ses)
  xargs = util_testes.trunca_valor(str(cmd_args), 100, 20)
  sys.stderr.write(f"rot_teste = {rot_teste} verificando vídeo {vid_id} ses = {str(ses_id)} cmd_args = {xargs}\n")
  ses_dono = obj_sessao.obtem_dono(ses)
  assert ses_dono != None

  vid = obj_video.obtem_objeto(vid_id)
  assert vid != None
  vid_atrs = obj_video.obtem_atributos(vid)
  sys.stderr.write(f"  atributos do vídeo criado = {str(vid_atrs)}\n")

  cmd_autor = ses_dono
  cmd_autor_id = obj_usuario.obtem_identificador(cmd_autor)
  vid_autor_id = obj_usuario.obtem_identificador(vid_atrs['autor'])
  if cmd_autor_id != vid_autor_id:
    sys.stderr.write(f"  ** atributo 'autor' não bate: cmd = {cmd_autor_id} criado = {vid_autor_id}")
    ok = False

  assert 'titulo' in cmd_args; 
  cmd_titulo = cmd_args['titulo']
  vid_titulo = vid_atrs['titulo']
  if cmd_titulo != vid_titulo:
    sys.stderr.write(f"  ** atributo 'titulo' não bate: cmd = {cmd_titulo} criado = {vid_titulo}")
    ok = False

  ok_global = ok_global and ok
  return ok

# ----------------------------------------------------------------------
# Algumas sessões para teste:
ses_A1 = obj_sessao.obtem_objeto("S-00000001") # Do administrador.
ses_C1 = obj_sessao.obtem_objeto("S-00000003") # De um plebeu.
ses_C2 = obj_sessao.obtem_objeto("S-00000004") # De outro plebeu.

# Obtém alguns usuários:
usr_admin1 = obj_sessao.obtem_dono(ses_A1)
assert obj_usuario.eh_administrador(usr_admin1)
usr_admin1_id = obj_usuario.obtem_identificador(usr_admin1)

usr_comum1 = obj_sessao.obtem_dono(ses_C1)
assert not obj_usuario.eh_administrador(usr_comum1)
usr_comum1_id = obj_usuario.obtem_identificador(usr_comum1)

usr_comum2 = obj_sessao.obtem_dono(ses_C2)
assert not obj_usuario.eh_administrador(usr_comum2)
assert usr_comum2 != usr_comum1 
usr_comum2_id = obj_usuario.obtem_identificador(usr_comum2)

bytes1 = open("videos/V-00000002.mp4", 'rb').read()

# ----------------------------------------------------------------------
# Testa com dados OK (sem 'autor'):
dados_OK1 = { \
  'titulo': "Bananas cibernéticas",
  'conteudo': bytes1,
}
testa_processa("OK1", True, ses_C1, dados_OK1)

# Outro teste OK (com 'autor' redundante):
dados_OK2 = { \
  'autor': usr_comum2_id,
  'titulo': "Bananas psicossomáticas",
  'conteudo': bytes1,
}
testa_processa("OK2", True, ses_C2, dados_OK2)

# Testa com 'autor' de outra sessão
dados_EautBad = { \
  'autor': usr_comum1_id,
  'titulo': "Pitangas matemáticas",
  'conteudo': bytes1,
}
testa_processa("E_autBad", False, ses_C2, dados_EautBad)

# Testa com usuário não logado:
dados_Enolog = { \
  'autor': usr_comum1_id,
  'titulo': "Goiabas organolépticas",
  'conteudo': bytes1,
}
testa_processa("E_sesNone", False, None, dados_Enolog)

# Testa com atributos espúrios:
dados_Elixo = { \
  'duracao': 10,
  'nota': 3.0,
  'titulo': "Tomates catastróficos",
  'conteudo': bytes1,
}
testa_processa("E_lixo", False, ses_C1, dados_Elixo)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
