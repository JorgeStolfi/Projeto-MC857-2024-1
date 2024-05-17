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
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok


# Sessao de usuário  administrador:
sesA1_id = "S-00000006"
sesA1 = obj_sessao.obtem_objeto(sesA1_id)
assert sesA1 != None
assert obj_sessao.aberta(sesA1)
assert obj_sessao.de_administrador(sesA1)
usrA1 = obj_sessao.obtem_dono(sesA1)
usrA1_id = obj_usuario.obtem_identificador(usrA1)
assert usrA1_id == "U-00000008"

# Sessão de usuário comum:
sesC1_id = "S-00000003"
sesC1 = obj_sessao.obtem_objeto(sesC1_id)
assert sesC1 != None
assert obj_sessao.aberta(sesC1)
assert not obj_sessao.de_administrador(sesC1)
usrC1 = obj_sessao.obtem_dono(sesC1)
usrC1_id = obj_usuario.obtem_identificador(usrC1)
assert usrC1_id == "U-00000002"

ses_dic = { 'N': None, 'A': sesA1, 'C': sesC1, }

# Um vídeo de {usrC1}:
vidC1_id = "V-00000002"
vidC1 = obj_video.obtem_objeto(vidC1_id)
assert vidC1 != None
assert obj_video.obtem_autor(vidC1) == usrC1

# Um vídeo de outro usuário, nenhum dos dois:
vidC2_id = "V-00000004"
vidC2 = obj_video.obtem_objeto(vidC2_id)
assert vidC2 != None
assert obj_video.obtem_autor(vidC2) != usrC1
assert obj_video.obtem_autor(vidC2) != usrA1

vid_dic = { 'C1': vidC1_id, 'C2': vidC2_id, }

erros_vaz = []
erros_tri = ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]

erros_dic = { 'N': None, 'V': erros_vaz, 'E': erros_tri, }

for ses_tag, ses in ses_dic.items():
  for vid_tag, vid_id in vid_dic.items():
    rot_teste = f"C_ses{ses_tag}_vid{vid_tag}"
    testa_processa(rot_teste,  str,  ses, { 'video': vid_id } )

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
