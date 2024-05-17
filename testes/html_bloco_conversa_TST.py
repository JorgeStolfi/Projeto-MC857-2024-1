#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import html_bloco_conversa
import obj_sessao
import obj_usuario
import obj_video
import obj_comentario
import db_base_sql
import db_tabelas_do_sistema
import util_testes
import util_identificador
from util_erros import aviso_prog

import sys

from obj_usuario import obtem_atributos, obtem_identificador

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_bloco_conversa
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
# Um usuário administrador:
usrA_id = "U-00000001"
usrA = obj_usuario.obtem_objeto(usrA_id)
assert usrA != None
assert obj_usuario.eh_administrador(usrA)

# Um usuário comum:
usrC_id = "U-00000002"
usrC = obj_usuario.obtem_objeto(usrC_id)
assert usrC != None
assert not obj_usuario.eh_administrador(usrC)

# Vídeo existente:
vid1_id = "V-00000001"
vid1 = obj_video.obtem_objeto(vid1_id)
assert vid1 != None
vid1_raizes = obj_comentario.busca_por_video(vid1_id, True)
vid1_conversa = obj_comentario.obtem_conversa(vid1_raizes, 15, 3)

# Comentário existente:
com1_id = "C-00000001"
com1 = obj_comentario.obtem_objeto(com1_id)
assert com1 != None
com1_raizes = obj_comentario.busca_por_pai(com1_id)
com1_conversa = obj_comentario.obtem_conversa(com1_raizes, 15, 3)

for ses_tag, ses_dono in ("N", None,), ("A", usrA,), ("C", usrC,):
  xses = f"_ses{ses_tag}"
  testa_gera("V1" + xses, str, vid1_conversa, ses_dono)
  testa_gera("C1" + xses, str, com1_conversa, ses_dono)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
