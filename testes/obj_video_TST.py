#! /usr/bin/python3

import obj_video
import db_base_sql 
import obj_raiz
import obj_usuario
import util_testes

from util_erros import ErroAtrib, erro_prog, mostra, aviso_prog

import os
import sys

# ----------------------------------------------------------------------
sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("  Inicializando módulo {usuario}, limpando tabela, criando usuários para teste:\n")
obj_usuario.cria_testes(True)


sys.stderr.write("  Inicializando módulo {video}, limpando tabela, criando vídeos para teste:\n")
obj_video.inicializa_modulo(True)
obj_video.liga_diagnosticos(True)
obj_video.cria_testes(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_video(rot_teste, vid, vid_id_esp, atrs_esp):
  """Testes básicos de consistência do objeto {vid} da classe {obj_video.Classe}, dados
  {vid_id_esp} e atributos esperados {atrs_esp}.  Retorna {True} se não detectou erros."""
  
  ok = True
  
  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write(f"  teste {rot_teste}, vídeo {vid_id_esp}")
  atrs_esp_str = str(util_testes.trunca_valor(atrs_esp, 2000, 50))
  sys.stderr.write(f" atrs_esp = {atrs_esp_str}\n")
  ok = obj_video.verifica_criacao(vid, vid_id_esp, atrs_esp)
  
  if vid == None:
    sys.stderr.write("  ** objeto é {None}\n")
    ok = False
  elif not isinstance(vid, obj_video.Classe):
      sys.stderr.write("  ** objeto não é {obj_video.Classe}\n")
      ok = False
  else:   
    sys.stderr.write("  testando {obj_video.obtem_identificador(vid)}:\n")
    vid_id_fun = obj_video.obtem_identificador(vid)
    if vid_id_fun != vid_id_esp:
      sys.stderr.write(f"  ** retornou {str(vid_id_fun)}, deveria ter retornado {str(vid_id_esp)}\n")
      ok = False

    sys.stderr.write("  testando {obj_video.obtem_objeto(vid_id)}:\n")
    vid_fun = obj_video.obtem_objeto(vid_id_esp)
    if vid_fun != vid:
      sys.stderr.write(f"  ** retornou {str(vid_fun)}, deveria ter retornado {str(vid)}\n")
      ok = False

    sys.stderr.write("  testando {obj_video.obtem_atributos(vid)}:\n")
    atrs_fun = obj_video.obtem_atributos(vid)
    for chave in atrs_fun.keys():
      val_fun = atrs_fun[chave]
      if chave in atrs_esp:
        val_esp = atrs_esp[chave]
        if val_fun!= val_esp:
          sys.stderr.write(f"  ** retornou '{chave}':\"{val_fun}\", deveria ter retornado \"{val_esp}\"\n")
          ok = False

    for chave in atrs_fun.keys():
      if chave != 'conteudo' and chave in atrs_esp:
        val_esp = atrs_esp[chave]

        sys.stderr.write("  testando {obj_video.obtem_atributo(vid,%s)}, esperado \"%s\":\n" % (chave, str(val_esp)))
        val_fun = atrs_fun[chave]
        if val_fun != val_esp:
          sys.stderr.write(f"  ** retornou {str(val_fun)}, deveria ter retornado {str(val_esp)}\n")
          ok = False

        if chave == 'autor':
          sys.stderr.write("  testando {obtem_autor(vid)}:\n")
          val_fun = obj_video.obtem_autor(vid)
        else:
          val_fun = "NECAS"
        if val_fun != "NECAS" and val_fun != val_esp:
          sys.stderr.write(f"  ** retornou {str(val_fun)}, deveria ter retornado {str(val_esp)}\n")
          ok = False
 
    for chave, val in atrs_fun.items():
      if chave != 'conteudo':
        # Buscas por objeto (como autor) devem usar o ID:
        if isinstance(val, obj_raiz.Classe):
          val = obj_raiz.obtem_identificador(val)
        sys.stderr.write(f"  testando {'{'}busca_por_campo('{chave}', {val}){'}'}:\n")
        id_list_vid1 = obj_video.busca_por_campo(chave, val)
        if not vid_id_esp in id_list_vid1:
          aviso_prog("retornou " + str(id_list_vid1) + ", devia ter " + str(vid_id_esp),True)
          ok = False

  return ok

# ----------------------------------------------------------------------
def testa_obj_video_cria_muda(rot_teste, valido, modif, vid_id, atrs):
  """{modif} é {False}, testa {obj_video.cria(atrs)}.
  Se {modif} é {True}, testa {obj_video.muda_atributos(vid, atrs)}
  onde {vid} é vídeo com identficador {vid_id}.
  
  Se {valido} é {True}, espera que a operação tenha sucesso. No caso de 
  criação, verifica se o identificador resultante é {vid_id}.
  Se {valido} é {False}, espera que a operação falhe.
  Também testa algumas outras funções no vídeo resultante.
  Em ambos os casos, se {valido} for {true}, espera que a chamada dê certo.
  Se for {False}, espera que dê erro."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  
  ok = True
  ult_id_antes = obj_video.ultimo_identificador()
  sys.stderr.write(f"  rot_teste = {rot_teste} ultimo id antes = {ult_id_antes}\n")
  
  try:

    atrs_esp_str = str(util_testes.trunca_valor(atrs, 2000, 50))
    if modif:
      sys.stderr.write(f"  testando obj_video.muda_atributos id = {vid_id} atrs = {atrs_esp_str}\n")
      vid = obj_video.obtem_objeto(vid_id)
      assert vid != None, f"video {vid_id} não existe"
      obj_video.muda_atributos(vid, atrs)
    else:
      sys.stderr.write(f"  testando obj_video.cria atrs = {atrs_esp_str}\n")
      vid = obj_video.cria(atrs)
      vid_id = obj_video.obtem_identificador(vid)
      ok = obj_video.verifica_criacao(vid, vid_id, atrs)
    ult_id_depois = obj_video.ultimo_identificador()
    sys.stderr.write(f"  chamada sem erro - ultimo id depois = {ult_id_depois}\n")
    if not valido:
      sys.stderr.write(f"  ** devia ter falhado!\n")
      ok = False
    if modif:
      assert ult_id_depois == ult_id_antes, "  mudou o número de vídeos na tabela"
    else:
      assert ult_id_depois > ult_id_antes, "  não mudou o número de vídeos na tabela"
    
    vid_id_esp = vid_id if modif else ult_id_depois
    ok = ok and verifica_video(rot_teste, vid, vid_id_esp, atrs)

  except ErroAtrib as ex:
    sys.stderr.write(f"  chamada falhou com ErroAtrib ex = {str(ex)}\n")
    if valido:
      sys.stderr.write(f"  ** devia ter dado certo!\n")
      ok = False

  except AssertionError as ex:
    sys.stderr.write(f"  chamada falhou com AssertionError ex = {str(ex)}\n")
    if valido:
      sys.stderr.write(f"  ** devia ter dado certo!\n")
      ok = False

  if ok:
    sys.stderr.write("  CONFERE!\n")
  else:
    aviso_prog("  teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))

  return ok

sys.stderr.write("  Obtendo dois usuários para teste:\n")

usr1 = obj_usuario.obtem_objeto("U-00000001")
usr2 = obj_usuario.obtem_objeto("U-00000002")
usr4 = obj_usuario.obtem_objeto("U-00000004")

# ----------------------------------------------------------------------
# Testando {obj_video.cria}:

# Teste que deve dar OK:
cr1_indice = int(obj_video.ultimo_identificador()[2:]) + 1
cr1_id = f"V-{cr1_indice:08d}"
cr1_bytes = open("videos/V-00000002.mp4", 'rb').read()
cr1_atrs = {
  'autor': usr1,
  'titulo': "Video Uno e Unico",
  'nota': 2.0,
  'vistas': 0,
  'conteudo': cr1_bytes,
  'bloqueado': False,
}
testa_obj_video_cria_muda("cr1_ok", True, False, None, cr1_atrs)

# Outro teste que deve dar OK:
cr2_indice = int(obj_video.ultimo_identificador()[2:]) + 1
cr2_id = f"V-{cr2_indice:08d}"
cr2_bytes = open("videos/V-00000003.mp4", 'rb').read()
cr2_atrs = {
  'autor': usr4,
  'titulo': "Video Due e Duplo",
  'nota': 2.0,
  'vistas': 0,
  'conteudo': cr2_bytes,
  'bloqueado': False,
}
testa_obj_video_cria_muda("cr2_ok", True, False, None, cr2_atrs)

# ----------------------------------------------------------------------
# Testando {obj_video.muda_atributos}:

# Teste OK - alteração de título:
md0_vid_id = "V-00000001"
md0_vid = obj_video.obtem_objeto(md0_vid_id)
assert md0_vid != None
md0_tit = "Não gostei do título!"
md0_atrs = {
  'titulo': md0_tit,
}
testa_obj_video_cria_muda("md0_tit", True, True, md0_vid_id, md0_atrs)
assert obj_video.obtem_atributo(md0_vid, 'titulo') == md0_tit

# Teste com erro - alteração de alguns atributos imutáveis:
md1_vid_id = cr1_id
md1_vid = obj_video.obtem_objeto(md1_vid_id)
assert md1_vid != None
md1_dur = obj_video.obtem_atributo(md1_vid, 'duracao')
md1_atrs = {
  'duracao': md1_dur + 100,
}
testa_obj_video_cria_muda("md1_bad", False, True, md1_vid_id, md1_atrs)
assert obj_video.obtem_atributo(md1_vid, 'duracao') == md1_dur

# Teste OK - alteração sem mudar nada:
md2_vid_id = cr2_id
md2_vid = obj_video.obtem_objeto(md2_vid_id)
md2_tit = obj_video.obtem_atributo(md2_vid, 'titulo') 
md2_atrs = {
  'titulo': md2_tit,
}
md2_vid_id = util_testes.unico_elemento(obj_video.busca_por_campo('titulo', md2_tit))
assert md2_vid_id != None
testa_obj_video_cria_muda("md2_nul", True, True, md2_vid_id, md2_atrs)

# Outro teste com erro - alteração de autor:
md3_vid_id = cr1_id
md3_vid = obj_video.obtem_objeto(md3_vid_id)
assert md3_vid != None
md3_autor = obj_video.obtem_autor(md3_vid)
assert md3_autor != usr4
md3_atrs = {
  'autor': usr4,
}
testa_obj_video_cria_muda("md3_bad", False, True, md3_vid_id, md3_atrs)
assert obj_video.obtem_autor(md3_vid) == md3_autor

# Teste OK - alteração de nota:
md4_vid_id = cr2_id
md4_vid = obj_video.obtem_objeto(md4_vid_id)
assert md4_vid != None
md4_nota = 2.718281828
md4_atrs = {
  'nota': md4_nota
}
testa_obj_video_cria_muda("md4_nota", True, True, md4_vid_id, md4_atrs)
assert obj_video.obtem_atributo(md4_vid, 'nota') == md4_nota

# Teste OK - alteração de 'bloqueado':
md5_vid_id = cr2_id
md5_vid = obj_video.obtem_objeto(md5_vid_id)
assert md5_vid != None
md5_bloqueado = True
md5_atrs = {
  'bloqueado': md5_bloqueado
}
testa_obj_video_cria_muda("md5_bloqueado", True, True, md5_vid_id, md5_atrs)
assert obj_video.obtem_atributo(md5_vid, 'bloqueado') == md5_bloqueado

# Teste OK - alteração de nota:
md6_vid_id = cr2_id
md6_vid = obj_video.obtem_objeto(md6_vid_id)
assert md6_vid != None
md6_vistas = 10000
md6_atrs = {
  'vistas': md6_vistas
}
testa_obj_video_cria_muda("md6_vistas", True, True, md6_vid_id, md6_atrs)
assert obj_video.obtem_atributo(md6_vid, 'vistas') == md6_vistas

# ----------------------------------------------------------------------
# Outros testes:


# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("  Teste terminou sem detectar erro\n")
else:
  aviso_prog("Algum teste falhou", True)

