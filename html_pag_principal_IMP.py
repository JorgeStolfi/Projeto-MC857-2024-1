import obj_sessao
import obj_usuario
import html_pag_generica
import html_elem_span
import html_elem_div
import html_elem_video
from util_erros import erro_prog, mostra

# Outras interfaces usadas por este módulo:
from datetime import datetime, timezone
import re, sys

def gera(ses, erros):
  cor_texto = "#000488"
  cor_fundo = "#eeeeee"
  estilo = \
    f"font-family: Courier; font-size: 16px; font-weight: normal; padding: 5px; " + \
    f"text-align: left; color: {cor_texto}; background-color: {cor_fundo}"

  if ses !=None:
    usr = obj_sessao.obtem_usuario(ses)
    atrs = obj_usuario.obtem_atributos(usr)
    nome = atrs['nome']
    texto1 = "Olá <b>"+nome+"</b>!"
    bloco_texto1 = html_elem_div.gera(estilo, texto1)
  else:
    texto1 = None
    bloco_texto1 = ""

  texto2 = "Bem vindo(a) ao nosso site de videos!"
  bloco_texto2 = html_elem_div.gera(estilo, texto2)

  bloco_video = html_elem_div.gera(None, html_elem_video.gera("virus.mp4", "virus", 400))

  now = datetime.now(timezone.utc)
  data = now.strftime("%Y-%m-%d %H:%M:%S %z")
  texto3 = "<hr/><i>DATA CORRENTE </i><b>" + data + "</b><br/>TUDO EM ORDEM NESTE SERVIDOR<hr/>"
  bloco_texto3 = html_elem_div.gera(estilo, texto3)

  conteudo = bloco_texto1 + bloco_texto2 + bloco_video + bloco_texto3
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
