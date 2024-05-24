#! /usr/bin/python3

import comando_recalcular_nota
import db_base_sql
import db_obj_tabela
import db_tabelas_do_sistema
import obj_comentario
import obj_raiz
import obj_sessao
import obj_usuario
import obj_video
import util_dict
import util_testes
from util_erros import ErroAtrib, aviso_prog

import re
import sys

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)
# obj_comentario.liga_diagnosticos(True)
# obj_raiz.liga_diagnosticos(True)
# db_base_sql.liga_diagnosticos(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, ses, com, vid, valido, nota_esp):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, e grava esse resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  
  sys.stderr.write("\n\n") 
  ses_id = obj_sessao.obtem_identificador(ses) if ses != None else None
  com_id = obj_comentario.obtem_identificador(com) if com != None else None
  vid_id = obj_video.obtem_identificador(vid) if vid != None else None
  sys.stderr.write(f"  testa_processa ses = {ses_id} com = {com_id} vid = {vid_id} valido = {valido}\n") 
  
  # Executa o comando:
  modulo = comando_recalcular_nota
  funcao = comando_recalcular_nota.processa
  if com != None:
    cmd_args = { 'comentario': obj_comentario.obtem_identificador(com) }
    if not valido: nota_esp = obj_comentario.obtem_atributo(com, 'nota')
  elif vid != None:
    cmd_args = { 'video': obj_video.obtem_identificador(vid) }
    if not valido: nota_esp = obj_video.obtem_atributo(vid, 'nota')
  else:
    assert False, "Hã?"
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, str, frag, pretty, ses, cmd_args)

  # Confere nota:
  if com != None:
    nota_nova = obj_comentario.obtem_atributo(com, 'nota')
  elif vid != None:
    nota_nova = obj_video.obtem_atributo(vid, 'nota')
  else:
    assert False, "Pô?"
  if abs(nota_nova - nota_esp) > 0.001:
    sys.stderr.write(f"  ** Nota recalculada = {nota_nova} não é a esperada = {nota_esp}\n")
    ok = False
  else:
    sys.stderr.write("  CONFERE!\n")

  ok_global = ok_global and ok
  return ok

# Comentário de teste, autor usuário comum:
com1_id = "C-00000002"
com1 = obj_comentario.obtem_objeto(com1_id)
assert com1 != None
com1_autor = obj_comentario.obtem_autor(com1) # U-00000002
assert not obj_usuario.eh_administrador(com1_autor)
com1_resp_ids = obj_comentario.busca_por_campo('pai', com1)
com1_resp_ids.sort()
assert com1_resp_ids == [ "C-00000005", "C-00000007", "C-00000010" ], f"com1_resp_ids = {com1_resp_ids}"
com1_nota_org = obj_comentario.obtem_atributo(com1, 'nota')
com1_votos = [ 0, 3, 1 ] # Devia verificar...
com1_notas = [ 2.00, 1.00, 3.50 ] # Devia verificar...
com1_nota_esp = \
  ( 2*2.00**2 + com1_votos[0]*com1_notas[0]**2 + com1_votos[1]*com1_notas[1]**2 + com1_votos[2]*com1_notas[2]**2 ) / \
  ( 2.00**2 + com1_notas[0]**2 + com1_notas[1]**2 + com1_notas[2]**2 )
com1_nota_esp = float(int(com1_nota_esp * 100)/100)
assert com1_nota_esp != com1_nota_org

# Vídeo de teste, autor usuário comum:
vid1_id = "V-00000004"
vid1 = obj_video.obtem_objeto(vid1_id)
assert vid1 != None
vid1_autor = obj_video.obtem_autor(vid1) # U-00000004
assert not obj_usuario.eh_administrador(vid1_autor)
vid1_comt_ids = obj_comentario.busca_por_campo('video', vid1)
vid1_comt_ids.sort()
assert vid1_comt_ids == [ "C-00000017", "C-00000018" ], f"vid1_resp_ids = {vid1_resp_ids}"
vid1_nota_org = obj_video.obtem_atributo(vid1, 'nota')
vid1_votos = [ 1, 4 ] # Devia verificar...
vid1_notas = [ 3.00, 2.00 ] # Devia verificar...
vid1_nota_esp = \
( 2*2.00**2 + vid1_votos[0]*vid1_notas[0]**2 + vid1_votos[1]*vid1_notas[1]**2 ) / \
( 2.00**2 + vid1_notas[0]**2 + vid1_notas[1]**2)
vid1_nota_esp = float(int(vid1_nota_esp * 100)/100)
assert vid1_nota_esp != vid1_nota_org
  
assert vid1_autor != com1_autor

# Uma sessão de administrador:
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)
assert sesA != None
assert obj_sessao.de_administrador(sesA)

# Uma sessão de usuário comum, autor de {com1}:
sesC_id = "S-00000003"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert sesC != None and obj_sessao.aberta(sesC)
sesC_dono = obj_sessao.obtem_dono(sesC) # U-00000002
assert not obj_sessao.de_administrador(sesC)
assert sesC_dono == com1_autor

# Uma sessão de usuário comum, autor de {vid1}:
sesV_id = "S-00000007" # 
sesV = obj_sessao.obtem_objeto(sesV_id)
assert sesV != None and obj_sessao.aberta(sesV)
sesV_dono = obj_sessao.obtem_dono(sesV) # U-00000004
assert not obj_sessao.de_administrador(sesV)
assert sesV_dono == vid1_autor

assert sesV_dono != sesC_dono

sys.stderr.write("\n")

for ses_tag, ses in ("N", None), ("A", sesA), ("C", sesC), ("V", sesV):
  xses = f"_ses{ses_tag}"
  ses_dono = obj_sessao.obtem_dono(ses) if ses != None else None
  
  valido = ses == sesA
  
  # Reseta a nota para cada teste:
  obj_comentario.muda_atributos(com1, { 'nota': com1_nota_org })
  com_esp = com1_nota_esp if valido else obj_comentario.obtem_atributo(com1, 'nota')
  testa_processa("C1" + xses, ses, com1, None, valido, com_esp )

  # Reseta a nota para cada teste:
  obj_video.muda_atributos(vid1, { 'nota': vid1_nota_org })
  vid_esp = vid1_nota_esp if valido else obj_video.obtem_atributo(vid1, 'nota')
  testa_processa("V1" + xses, ses, None, vid1, valido, vid1_nota_esp )

if ok_global:
  sys.stderr.write("Teste terminado normalmente\n")
else:
  aviso_prog("Alguns testes falharam.", True)
