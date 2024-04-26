#! /usr/bin/python3

import obj_comentario

import db_base_sql 
import obj_usuario
import obj_video
import util_testes
from util_erros import erro_prog, mostra, aviso_prog

import sys

# ----------------------------------------------------------------------
sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("  Inicializando módulos {usuario} e {video}, limpando tabelas:\n")
obj_usuario.cria_testes(True)
obj_video.cria_testes(True)

sys.stderr.write("  Inicializando módulo {comentario}, limpando tabela, criando comentários para teste:\n")
obj_comentario.inicializa_modulo(True)
obj_comentario.cria_testes(True)

ok_global = True # Vira {False} se um teste falha.

def verifica_comentario(rot_teste, com, ident, atrs):
  """Testes básicos de consistência do objeto {com} da classe {obj_comentario.Classe}, dados
  {ident} e os atributos {atrs} esperados."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write("  teste %s, comentário %s\n" % (rot_teste, ident))
  ok = obj_comentario.verifica_criacao(com, ident, atrs)
  
  if com == None:
    aviso_prog("objeto é {None}, devia ser {%s}" % ident)
  else:
    if type(com) is not obj_comentario.Classe:
      aviso_prog("objeto não é {obj_comentario.Classe}")

    sys.stderr.write("  testando {obj_comentario.obtem_identificador(com)}:\n")
    ident_fun = obj_comentario.obtem_identificador(com)
    if ident_fun != ident:
      aviso_prog("retornou " + str(ident_fun) + ", deveria ter retornado " + str(ident),True)
      ok = False

    sys.stderr.write("  testando {obj_comentario.obtem_atributos(com)}:\n")
    atrs_fun = obj_comentario.obtem_atributos(com)
    if atrs_fun != atrs:
      aviso_prog("retornou " + str(atrs_fun) + ", deveria ter retornado " + str(atrs),True)
      ok = False

    for chave in 'video', 'autor', 'data', 'pai', 'texto':
      sys.stderr.write("  testando {obj_comentario.obtem_atributo(com,%s)}:\n" % chave)
      val_fun = obj_comentario.obtem_atributo(com, chave)
      val_esp = atrs_fun[chave]
      if val_fun != val_esp:
        aviso_prog("retornou " + str(val_fun) + ", deveria ter retornado " + str(val_esp),True)
        ok = False

  sys.stderr.write("  testando {obj_comentario.busca_por_dentificador(%s)}:\n" % ident)
  com_esp = com
  com_fun = obj_comentario.busca_por_identificador(ident)
  if com_fun != com_esp:
    aviso_prog("retornou " + str(com_fun) + ", deveria ter retornado " + str(com_esp),True)
    ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

def verifica_busca_multipla(rot_teste, chave, val, idents):
  """Testes de consistência das funções de busca que devolvem listas de identificadores, dados
  a chave de busca {chave}, o valor de busca {val}, e a lista de identificadores {idents} esperados."""
  sys.stderr.write("  testando {obj_comentario.busca_por_%s(\"%s\")}:\n" % (chave, val))

  ok = True
  if chave == 'video':
    idents_fun = obj_comentario.busca_por_video(val)
  elif chave == 'autor':
    idents_fun = obj_comentario.busca_por_autor(val)
  else:
    assert False, "** função inexistente"

  if sorted(idents_fun) != sorted(idents):
    aviso_prog("retornou " + str(idents_fun) + ", deveria ter retornado " + str(idents),True)
    ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return


# ----------------------------------------------------------------------
sys.stderr.write("  Obtendo alguns comentários para teste:\n")

com1 = obj_comentario.busca_por_identificador("C-00000001")
com2 = obj_comentario.busca_por_identificador("C-00000002")
com3 = obj_comentario.busca_por_identificador("C-00000003")
com4 = obj_comentario.busca_por_identificador("C-00000004")
com5 = obj_comentario.busca_por_identificador("C-00000005")
com6 = obj_comentario.busca_por_identificador("C-00000006")

sys.stderr.write("  Obtendo alguns vídeos para teste:\n")

vid1 = obj_video.busca_por_identificador("V-00000001")
vid2 = obj_video.busca_por_identificador("V-00000002")
vid2 = obj_video.busca_por_identificador("V-00000002")

sys.stderr.write("  Obtendo alguns usuários para teste:\n")

usr1 = obj_usuario.busca_por_identificador("U-00000001")
usr2 = obj_usuario.busca_por_identificador("U-00000002")
usr3 = obj_usuario.busca_por_identificador("U-00000003")

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.cria} sem pai:\n")
vid_cr0 = obj_video.busca_por_identificador("V-00000003")
usr_cr0 = obj_usuario.busca_por_identificador("U-00000005")
data_cr0 = "2024-04-06 23:59:00 UTC"
pai_cr0 = None
atrs_cr0 = { 'video': vid_cr0, 'autor': usr_cr0, 'data': data_cr0, 'pai': pai_cr0, 'texto': "Que coisa!" }
cmt_cr0 = obj_comentario.cria(atrs_cr0)
indice_cr0 = 7 # Depende de {obj_comentario.cria_testes}.
ident_cr0 = f"C-{indice_cr0:08d}"
verifica_comentario("cr0", cmt_cr0, ident_cr0, atrs_cr0)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.cria} com pai:\n")
vid_cr1 = vid_cr0
usr_cr1 = obj_usuario.busca_por_identificador("U-00000002")
data_cr1 = "2024-04-06 23:59:01 UTC"
pai_cr1 = cmt_cr0
atrs_cr1 = { 'video': vid_cr1, 'autor': usr_cr1, 'data': data_cr1, 'pai': pai_cr1, 'texto': "Não diga!" }
cmt_cr1 = obj_comentario.cria(atrs_cr1)
indice_cr1 = indice_cr0 + 1
ident_cr1 = f"C-{indice_cr1:08d}"
verifica_comentario("cr1", cmt_cr1, ident_cr1, atrs_cr1)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.busca_por_video()}:\n")
# Depende de {obj_comentario.cria_testes}.
id_vid_bv1 = "V-00000001"
verifica_busca_multipla("bv1", 'video', id_vid_bv1, ( "C-00000001", "C-00000002", "C-00000005", ))

id_vid_bv2 = "V-00000003"
verifica_busca_multipla("bv2", 'video', id_vid_bv2, ( "C-00000004", "C-00000006", ident_cr0, ident_cr1, ))

id_vid_bv3 = "V-00000004"
verifica_busca_multipla("bv3", 'video', id_vid_bv3, ())

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.busca_por_autor()}:\n")
id_usr_bu1 = "U-00000003"
verifica_busca_multipla("bu1", 'autor', id_usr_bu1, ( "C-00000004", "C-00000005", "C-00000006", ))

id_usr_bu2 = "U-00000005"
verifica_busca_multipla("bu2", 'autor', id_usr_bu2, ( ident_cr0, ))

id_usr_bu3 = "U-00000004"
verifica_busca_multipla("bu3", 'autor', id_usr_bu3, ( ))

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
