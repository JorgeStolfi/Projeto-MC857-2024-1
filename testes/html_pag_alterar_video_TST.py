#! /usr/bin/env python3

import html_pag_alterar_video
import db_tabelas_do_sistema
import obj_video
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_pag_alterar_video
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = True # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Sessao de usuário  administrador:
sesA1_id = "S-00000006"
sesA1 = obj_sessao.busca_por_identificador(sesA1_id)
assert sesA1 != None
assert obj_sessao.aberta(sesA1)
assert obj_sessao.de_administrador(sesA1)
usrA1 = obj_sessao.obtem_usuario(sesA1)
usrA1_id = obj_usuario.obtem_identificador(usrA1)
assert usrA1_id == "U-00000008"

# Sessão de usuário comum:
sesC1_id = "S-00000003"
sesC1 = obj_sessao.busca_por_identificador(sesC1_id)
assert sesC1 != None
assert obj_sessao.aberta(sesC1)
assert not obj_sessao.de_administrador(sesC1)
usrC1 = obj_sessao.obtem_usuario(sesC1)
usrC1_id = obj_usuario.obtem_identificador(usrC1)
assert usrC1_id == "U-00000002"

ses_dic = { 'A': sesA1, 'C': sesC1, }

# Um vídeo de {usrC1}:
vidC1_id = "V-00000002"
vidC1 = obj_video.busca_por_identificador(vidC1_id)
assert vidC1 != None
assert obj_video.obtem_campo(vidC1, 'autor') == usrC1

# Um vídeo de outro usuário, nenhum dos dois:
vidC2_id = "V-00000004"
vidC2 = obj_video.busca_por_identificador(vidC2_id)
assert vidC2 != None
assert obj_video.obtem_campo(vidC2, 'autor') != usrC1
assert obj_video.obtem_campo(vidC2, 'autor') != usrA1

vid_dic = { 'C1': vidC1_id, 'C2': vidC2_id, }

erros_vaz = []
erros_tri = ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]

erros_dic = { 'N': None, 'V': erros_vaz, 'E': erros_tri, }

for st, ses in ses_dic.items():
  for vt, id_vid in vid_dic.items():
    for et, erros in erros_dic.items():
      if ses == sesA1 or (ses == sesC1 and id_vid == vidC1_id)
        vid = obj_video.busca_por_identificador(id_vid)
        atrs_tot = obj_video.obtem_atributos(vid)
        atrs_som = { 'titulo': "Alteradus", }
        atrs_dic = { 'N': {}, 'T': atrs_tot, 'S': atrs_som, }
        for at, atrs in atrs_dic.items():
          rot_teste = f"ses{st}-vid{vt}-atrs{at}-erros{et}"
          testa_gera(rot_teste, ses, id_vid, atrs, erros)

sys.stderr.write("Testes terminados normalmente.\n")
