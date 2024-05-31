import html_bloco_grade_de_videos
import obj_sessao
import obj_usuario
import obj_video
import html_pag_generica
import html_bloco_titulo
from util_erros import erro_prog, mostra

import sys

def gera(ses, erros):
  if  ses == None:
    titulo = "Bem vinde ao nosso site de videos!"
    ht_titulo = html_bloco_titulo.gera(titulo)
  else:
    ht_titulo = ""

  ncols = 4  # Colunas da grade.
  nlins = 3  # Linhas da grade.
  nvids = ncols*nlins  # Total de células na grade.

  vid_ids = obj_video.obtem_amostra(nvids)
  
  try:
    ht_grade = html_bloco_grade_de_videos.gera(vid_ids, ncols)
  except ErroAtrib as ex:
    erros += ex.args[0] 

  try:
    ht_grade = html_bloco_grade_de_videos.gera(vid_ids, ncols)
  except ErroAtrib as ex:
    erros += ex.args[0] 
    ht_grade = ""

  ht_conteudo = ht_titulo + ht_grade
  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
