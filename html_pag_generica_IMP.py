import obj_sessao
import obj_usuario

import html_bloco_cabecalho
import html_bloco_menu_geral
import html_bloco_erro
import html_elem_span
import html_estilo_texto
import html_bloco_rodape

import re
import sys

pgn_debug = False

def gera(ses, ht_conteudo, erros):

  titulo = "Oito-Cinco-Sete"
  
  # Cabeçalho de página HTML:
  ht_abre = \
    "<!DOCTYPE HTML>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<link rel=\"icon\" href=\"imagens/favicon.png\" type=\"image/x-icon\"> " +  \
    "<link rel=\"shortcut icon\" href=\"imagens/favicon.png\" type=\"image/x-icon\"> " +  \
    "<link rel=\"icon\" href=\"imagens/favicon-32x32.png\" sizes=\"32x32\"> " +  \
    "<link rel=\"shortcut icon\" href=\"imagens/favicon-32x32.png\" sizes=\"32x32\" type=\"image/png\"> " + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "<title>" + titulo + "</title>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">"  

  # Cabeçalho das páginas:
  ht_cabe = html_bloco_cabecalho.gera(titulo, True)

  # Menu geral no alto da página:
  usr = obj_sessao.obtem_usuario(ses) if ses != None else None
  ht_menu = html_bloco_menu_geral.gera(usr)

  # Mensagens de erro, ou "":
  ht_erros = html_bloco_erro.gera(erros)

  # Rodapé da página:
  ht_roda = html_bloco_rodape.gera()
    
  # Fecha arquivo HTML:
  ht_fecha = \
    "  </body>\n" + \
    "</html>\n"

  # Monta a página:
  pagina = \
    ht_abre + "\n" + \
    ht_cabe + "<br/>\n" + \
    ht_menu + "<br/>\n" + \
    ( ( ht_erros + "<br/>\n" ) if ht_erros != "" else "") + \
    ht_conteudo + "<br/>\n" + \
    ht_roda + "\n" + \
    ht_fecha
  return pagina
