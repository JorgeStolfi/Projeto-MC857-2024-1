#! /usr/bin/python3

import util_video
import db_base_sql 
import util_testes

from util_erros import ErroAtrib, erro_prog, mostra, aviso_prog

import os
import sys

# ----------------------------------------------------------------------
sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)


# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

# ----------------------------------------------------------------------
def roda_teste(rot_teste, vid_id, conteudo):
  """Testes básicos das funções do módulo para o identificador de vídeo {vid_id}, com o {conteudo} (bytes)dado. Retorna {True} se não detectou erros."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  
  ok = True
   
  try:
    duracao, largura, altura, NQ = util_video.grava_arquivos(vid_id,conteudo)
    ok = verifica_arquivos(rot_teste, vid_id, conteudo, duracao, largura, altura, NQ)
  except ErroAtrib as ex:
    sys.stderr.write(f"  chamada falhou com ErroAtrib ex = {str(ex)}\n")
    sys.stderr.write(f"  ** devia ter dado certo!\n")
    ok = False

  except AssertionError as ex:
    sys.stderr.write(f"  chamada falhou com AssertionError ex = {str(ex)}\n")
    sys.stderr.write(f"  ** devia ter dado certo!\n")
    ok = False

  if ok:
    sys.stderr.write("  CONFERE!\n")
  else:
    aviso_prog("  teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))

  return ok

def verifica_arquivos(rot_teste, vid_id, conteudo, duracao, largura, altura, NQ):
  """Verifica se os arquivos de {vid_id} foram criados."""
  
  ok = True
  
  if not util_video.verifica_arquivo(vid_id):
    sys.stderr.write("**  {util_video.verifica_arquivo} falhou\n")
    ok = False
    
  conteudo_arq = open(f"videos/{vid_id}.mp4", "rb").read()
  if conteudo_arq != conteudo:
    sys.stderr.write("**  conteúdo do arquivo não bate\n")
    ok = False
 
  if NQ != 6:
    sys.stderr.write("**  número de quadros NQ não bate\n")
    ok = False
  
  if not util_video.verifica_capa(vid_id):
    sys.stderr.write("**  {util_video.verifica_capa} falhou\n")
    ok = False
 
  if not util_video.verifica_quadros(vid_id):
    sys.stderr.write("**  {util_video.verifica_quadros} falhou\n")
    ok = False

  return ok

# ----------------------------------------------------------------------
# Testando {obj_video.cria}:

# Teste que deve dar OK:
cr1_indice = 101
cr1_id = f"V-{cr1_indice:08d}"
cr1_bytes = open("videos/V-00000002.mp4", 'rb').read()

roda_teste("cr1_ok", cr1_id, cr1_bytes)

# Testando extrai_trecho
def roda_extrai_trecho(vid_id,inicio,fim):
  """Teste da funcao extrai trecho."""

  ok = True
   
  if not util_video.verifica_arquivo(vid_id):
    sys.stderr.write("**  {util_video.verifica_arquivo} falhou\n")
    ok = False

  try:
    util_video.extrai_trecho(vid_id, inicio, fim)
  except ErroAtrib as ex:
    sys.stderr.write(f"  chamada falhou com ErroAtrib ex = {str(ex)}\n")
    sys.stderr.write(f"  ** devia ter dado certo!\n")
    ok = False

  except AssertionError as ex:
    sys.stderr.write(f"  chamada falhou com AssertionError ex = {str(ex)}\n")
    sys.stderr.write(f"  ** devia ter dado certo!\n")
    ok = False

  if ok:
    sys.stderr.write("  CONFERE!\n")
  else:
    aviso_prog("  teste falhou",True)
    ok_global = False

  return ok

roda_extrai_trecho("V-00000002", 2.0, 4.0)
roda_extrai_trecho("V-00000009", 3.0, 7.0)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("  Teste terminou sem detectar erro\n")
else:
  aviso_prog("Algum teste falhou", True)

