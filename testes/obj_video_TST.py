#! /usr/bin/python3

import os,sys,inspect
import db_base_sql 
import db_tabela_generica
import db_tabelas
import obj_video
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
  {id_vid} e atributos esperados {atrs}."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write("  verificando video %s\n" % rotulo)
  ok = obj_video.verifica_criacao(vid, id_vid, atrs)
  
  if vid != None and type(vid) is obj_video.Classe:
    
    sys.stderr.write("  testando {obtem_usuario()}:\n")
    usr1 = obj_video.obtem_usuario(vid)
    if usr1 != atrs['usr']:
      aviso_prog("retornou " + str(usr1) + ", deveria ter retornado " + str(usr),True)
      ok = False
    
    sys.stderr.write("  testando {obtem_data_de_upload()}:\n")
    data1 = obj_video.obtem_data_de_upload(vid)
    if data1 != atrs['data']:
      aviso_prog("retornou " + str(data1) + ", deveria ter retornado " + str(data),True)
      ok = False
    
    sys.stderr.write("  testando {busca_por_arquivo()}:\n")
    id_vid1 = obj_video.busca_por_arquivo(atrs['arq'])
    if id_vid1 != id_vid:
      aviso_prog("retornou " + str(id_vid1) + ", deveria ter retornado " + str(id_vid),True)
      ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_video.cria}:\n")
vid1_atrs = {
  'usr': usr1,
  'arq': "arq1",
  'titulo': "Video Uno",
  'data': "2024-03-09 19:07:49.14 UTC",
  'duracao': 3100,
  'largura': 540,
  'altura': 330,
}
vid1 = obj_video.cria(vid1_atrs)
vid1_indice = 1
vid1_id = "V-00000001"
verifica_video("v1", vid1, vid1_id, vid1_atrs)

sys.stderr.write("  testando {obj_video.cria}:\n")
vid2_atrs = {
  'usr': usr4,
  'arq': "arq2",
  'titulo': "Video Due",
  'data': "2024-03-09 19:07:49.15 UTC",
  'duracao': 3200,
  'largura': 512,
  'altura': 512,
}
vid2 = obj_video.cria(vid2_atrs)
vid2_indice = 2
vid2_id = "V-00000002"
verifica_video("v2", vid2, vid2_id, vid2_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_video.muda_atributos}:\n")

# Alteração de alguns atributos:
vid1_mods = {
  'arq': "Video Ichi",
  'duracao': 4200
}
obj_video.muda_atributos(vid1, vid1_mods)
vid1_d_atrs = vid1_atrs
for k, v in vid1_mods.items():
  vid1_d_atrs[k] = v
verifica_video("v1_mod", vid1, vid1_id, vid1_d_atrs) 

# Alteração nula:
if type(vid2) is obj_video.Classe:
  obj_video.muda_atributos(vid2, vid2_atrs) # Não deveria mudar os atributos
  verifica_video("v2_mod", vid2, vid2_id, vid2_atrs)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("  Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
