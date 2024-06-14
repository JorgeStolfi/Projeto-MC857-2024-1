import obj_raiz
import obj_video
import obj_usuario
import obj_comentario

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql

import util_identificador
import util_data
import util_booleano
import util_titulo_de_video
from util_erros import ErroAtrib, erro_prog, mostra

import cv2
import os
import re
import time
import random

from datetime import datetime, timezone
from math import log, gcd, sin
import os
import subprocess
import json
import sys

util_video_debug = True

def grava_arquivos(vid_id, conteudo):

  global util_video_debug
  
  sys.stderr.write(f"    criando os arquivos do vídeo {vid_id}...\n")

  # Nome do arquivo de vídeo:
  arq_video = f"videos/{vid_id}.mp4"

  if conteudo != None:
    # Grava o conteúdo em disco:
    wr = open(arq_video, 'wb')
    wr.write(conteudo)
    wr.close()
  else:
    assert os.path.exists(arq_video), f"Item 'conteudo' ausente e arquivo {arq_video} não existe"
  
  duracao, largura, altura = obtem_dimensoes_do_arquivo(arq_video)
 
  extrai_capa(vid_id)
  
  NQ = extrai_quadros_indice(vid_id, duracao,largura,altura)

  return duracao, largura, altura, NQ

def verifica_arquivo(vid_id):

  global util_video_debug

  arq_video = f"videos/{vid_id}.mp4"
  ok = os.path.exists(arq_video)
  if not ok: aviso_prog(f"arquivo {arq_video} não foi criado", True)
  return ok

def obtem_dimensoes_do_arquivo(arq_video):

  global util_video_debug

  assert os.path.exists(arq_video), f"arquivo {arq_video} não existe"

  command = [
    "ffprobe",
    "-v", 
    "error", 
    "-select_streams",
    "v:0",
    "-show_entries",
    "stream=width,height,duration",  # Incluindo duração
    "-of",
    "json",
    arq_video
    ]

  result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  data = json.loads(result.stdout)
  # sys.stderr.write(f"@*@    data = {data}\n")

  duracao = int(float(data["streams"][0]["duration"]) * 1000)  # Convertendo para milissegundos
  largura = int(data["streams"][0]["width"])
  altura = int(data["streams"][0]["height"])
  return duracao, largura, altura

def extrai_capa(vid_id):

  global util_video_debug
  
  arq_video = f"videos/{vid_id}.mp4"
  assert os.path.exists(arq_video), f"arquivo {arq_video} não existe"

  diretorio = "capas"
  if not os.path.exists(diretorio): os.makedirs(diretorio)
  arq_capa = f"{diretorio}/{vid_id}.png"

  if os.path.exists(arq_capa):
    if util_video_debug: sys.stderr.write(f"    capa {arq_capa} já existe\n")
  else:
    if util_video_debug: sys.stderr.write(f"    extraindo a capa {arq_capa}...\n")
    # Carrega o video na memória !!! Inteiro? Que desperdício !!!
    fluxo = cv2.VideoCapture(arq_video)
    # Obtém o frame 0 do vídeo:
    successo, capa = fluxo.read()
    assert successo, "captura de frame falhou"
    fluxo.release()
    cv2.imwrite(arq_capa, capa)

def verifica_capa(vid_id):

  global util_video_debug

  arq_capa = f"capas/{vid_id}.png"
  ok = os.path.exists(arq_capa)
  if not ok: aviso_prog(f"arquivo {arq_capa} não foi criado", True)
  return ok

def extrai_quadros_indice(vid_id,duracao,largura,altura):

  global util_video_debug
 
  arq_video = f"videos/{vid_id}.mp4"
  assert os.path.exists(arq_video), f"arquivo {arq_video} não existe"

  NQ = 6  # Por enquanto.

  diretorio = "quadros"
  if not os.path.exists(diretorio): os.makedirs(diretorio)

  altura_qdr = 48
  largura_qdr = int(altura_qdr*largura/altura + 0.5)
  largura_qdr += (largura_qdr % 2) # Porque o {ffmpeg} não aceita ímpar.

  for iq in range(NQ):
    arq_quadro = f'{diretorio}/{vid_id}-{iq:03d}.png'
    if os.path.exists(arq_quadro):
      if util_video_debug: sys.stderr.write(f"    quadro-índice {arq_quadro} já existe\n")
    else:
      if iq == NQ-1:
        # Tem que pegar um pouco antes do fim para {ffmpeg} funcionar:
        tempo = round(duracao/1000 - 0.050, 3)
      else:
        tempo = round(duracao*iq/(NQ - 1)/1000,3)
      if util_video_debug: sys.stderr.write(f"    extraindo o quadro {arq_quadro} t = {tempo}s\n")
      sys.stderr.flush()
      comando_ffmpeg = [
          'ffmpeg', 
          '-y', 
          '-ss', str(tempo), 
          '-i', arq_video, 
          '-vframes', '1', 
          '-q:v', '2',
          '-vf', f'scale={largura_qdr}:{altura_qdr}',
          arq_quadro
      ]
      if util_video_debug: xcmd = " ".join(comando_ffmpeg); sys.stderr.write(f"  comando = «{xcmd}»\n")
      res = subprocess.run(comando_ffmpeg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
      assert res.returncode == 0, f"erro ao executar ffmpeg"
  return NQ

def verifica_quadros(vid_id):

  global util_video_debug
  
  if util_video_debug: sys.stderr.write(f"verificando quadros-indice de {vid_id}..\n")
  NQ = 6
  ok = True
  for iq in range(NQ):
    arq_quadro = f'quadros/{vid_id}-{iq:03d}.png'
    if not os.path.exists(arq_quadro):
      aviso_prog(f"arquivo {arq_quadro} não foi criado", True)
      ok = False
  return ok

def extrai_trecho(vid_id,inicio,fim):
  assert type(inicio) is float
  assert type(fim) is float
  assert 0 <= inicio and fim >= inicio + 0.001, "intervalo de tempo inválido"
  sys.stderr.write("** !!! a função {util_video.extrai_trecho} não está implementada !!!\n")

  # Resultado tapa-buraco:
  recho_arq = f"videos/{vid_id}.mp4"

  return trecho_arq

def extrai_quadro(vid_id,tempo):
  assert type(tempo) is float
  assert tempo >= 0, "tempo inválido"
  sys.stderr.write("** !!! a função {util_video.extrai_quadro} não está implementada !!!\n")

  # Resultado tapa-buraco:
  quadro_arq = f"quadros/{vid_id}-002.png"

  return quadro_arq
