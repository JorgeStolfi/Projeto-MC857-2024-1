#! /usr/bin/python3

import os,sys,inspect
import db_base_sql 
import db_tabela_generica
import db_tabelas
import obj_video
import obj_raiz
import obj_usuario
import util_testes
from util_testes import erro_prog, mostra, aviso_prog

# ----------------------------------------------------------------------
sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("  Inicializando módulo {usuario}, limpando tabela, criando usuários para teste:\n")
obj_usuario.cria_testes(True)

sys.stderr.write("  Inicializando módulo {video}, limpando tabela:\n")
obj_video.inicializa_modulo(True)

# ----------------------------------------------------------------------
sys.stderr.write("  Obtendo dois usuários para teste:\n")

usr1 = obj_usuario.busca_por_identificador("U-00000001")
usr2 = obj_usuario.busca_por_identificador("U-00000002")
usr4 = obj_usuario.busca_por_identificador("U-00000004")

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_video(rotulo, vid, id_vid, atrs):
  """Testes básicos de consistência do objeto {vid} da classe {obj_video.Classe}, dados
  {id_vid} e atributos esperados {atrs}.  Retorna {True} se não detectou erros."""

  sys.stderr.write("  verificando video %s\n" % rotulo)
  ok = obj_video.verifica_criacao(vid, id_vid, atrs)
  
  if vid != None and type(vid) is obj_video.Classe:
    
    sys.stderr.write("  testando {obtem_usuario()}:\n")
    usr1 = obj_video.obtem_usuario(vid)
    if usr1 != atrs['autor']:
      aviso_prog("retornou " + str(usr1) + ", deveria ter retornado " + str(usr),True)
      ok = False
    
    sys.stderr.write("  testando {obtem_data_de_upload()}:\n")
    data1 = obj_video.obtem_data_de_upload(vid)
    
    sys.stderr.write("  testando {busca_por_arquivo()}:\n")
    id_vid1 = obj_video.busca_por_arquivo(atrs['arq'])
    if id_vid1 != id_vid:
      aviso_prog("retornou " + str(id_vid1) + ", deveria ter retornado " + str(id_vid),True)
      ok = False

  return ok
  
def testa_obj_video_cria_muda(rotulo, valido, modif, id_vid, atrs):
  """Se {modif} é {False}, testa {obj_video.cria(atrs)} e ignora {id_vid}.
  Se {modif} é {True}, testa {obj_video.muda_atributos(vid, atrs)}
  onde {vid} é vídeo com identficador {id_vid}.
  Também testa algumas outras funções no vídeo resultante.
  Em ambos os casos, se {valido} for {true}, espera que a chamada dê certo.
  Se for {False}, espera que dê erro."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  
  ok = True
  ult_id_antes = obj_raiz.ultimo_identificador("videos", "V")
  sys.stderr.write(f"  rotulo = {rotulo} ultimo id antes = {ult_id_antes}\n")
  
  try:
    if modif:
      sys.stderr.write(f"  testando obj_video.muda_atributos id = {id_vid} atrs = {str(atrs)}\n")
      vid = obj_video.busca_por_identificador(id_vid)
      obj_video.muda_atributos(vid, atrs)
    else:
      sys.stderr.write(f"  testando obj_video.cria atrs = {str(atrs)}\n")
      vid = obj_video.cria(atrs)
    ult_id_depois = obj_raiz.ultimo_identificador("videos", "V")
    sys.stderr.write(f"  chamada sem erro - ultimo id depois = {ult_id_depois}\n")
    if not valido:
      sys.stderr.write(f"  ** devia ter falhado!\n")
      ok = False
    if modif:
      assert ult_id_depois == ult_id_antes, "mudou o número de vídeos na tabela"
    else:
      assert ult_id_depois > ult_id_antes, "não mudou o número de vídeos na tabela"
    ok = ok and verifica_video(rotulo, vid, ult_id_depois, atrs)
  except:
    sys.stderr.write("  chamada falhou\n")
    if valido:
      sys.stderr.write(f"  ** devia ter dado certo!\n")
      ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))

  return

# ----------------------------------------------------------------------
# Testando {obj_video.cria}:

# Teste OK:
atrs_cr1 = {
  'autor': usr1,
  'arq': "arq1",
  'titulo': "Video Uno",
}
testa_obj_video_cria_muda("cr1_ok", True, False, None, atrs_cr1)

# Outro teste OK:
atrs_cr2 = {
  'autor': usr4,
  'arq': "arq2",
  'titulo': "Video Due",
}
testa_obj_video_cria_muda("cr2_ok", True, False, None, atrs_cr2)

# Teste com erro (arquivo repetido):
atrs_cr3 = {
  'autor': usr2,
  'arq': "arq2",
  'titulo': "Video Due Bis",
}
testa_obj_video_cria_muda("cr3_bad", False, False, None, atrs_cr3)

# ----------------------------------------------------------------------
# Testando {obj_video.muda_atributos}:

# Teste com erro - alteração de alguns atributos imutáveis:
atrs_md1 = {
  'arq': "Video Ichi",
  'duracao': 4200
}
id_md1 = obj_video.busca_por_arquivo("arq1")
assert id_md1 != None
testa_obj_video_cria_muda("md1_bad", False, True, id_md1, atrs_md1)

# Teste OK - alteração sem mudar nada:
arq_md2 = atrs_cr2['arq']
tit_md2 = atrs_cr2['titulo']
atrs_md2 = {
  'arq': arq_md2,
  'titulo': tit_md2,
}
id_md2 = obj_video.busca_por_arquivo(arq_md2)
assert id_md2 != None
testa_obj_video_cria_muda("md2_bad", True, True, id_md2, atrs_md2)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("  Teste terminou sem detectar erro\n")
else:
  erro_prog("Teste falhou")
