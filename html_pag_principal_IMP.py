import obj_sessao
import obj_usuario
import html_pag_generica
import html_elem_span
import html_elem_div
import html_elem_video
import html_estilo_titulo
from util_erros import erro_prog, mostra

# Outras interfaces usadas por este módulo:
from datetime import datetime, timezone
import re, sys

def gera(ses, erros):
  if  ses == None:
    texto1 = "Bem vinde ao nosso site de videos!"
    estilo1 = html_estilo_titulo.gera("#b00000")
    bloco_texto1 = html_elem_div.gera(estilo1, texto1)
  else:
    bloco_texto1 = ""

  bloco_video = html_elem_div.gera(None, html_elem_video.gera("V-00000001", 400))

  conteudo = bloco_texto1 + bloco_video
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
