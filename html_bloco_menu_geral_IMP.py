import html_elem_button_simples
import html_elem_span
import html_elem_button_submit
import html_elem_input
import html_elem_form

from util_testes import erro_prog

# Outros módulos importados por esta implementação:
from datetime import datetime, timezone
import re
import sys

def gera(logado, nome_usuario, admin):
  ht_menu = gera_linha(gera_botoes_linha_1(logado, nome_usuario, admin))
  if admin:
    ht_menu += gera_linha(gera_botoes_linha_2())
  return ht_menu

def gera_linha(botoes):
  """Monta uma linha do menu geral, dada uma lista de fragmentos HTML que
  descrevem os botões."""
  html = "<nav>"
  for bt in botoes:
    if bt != None and bt != "":
      html += "  " + bt
  html += "</nav>"
  return html

def gera_botoes_linha_1(logado, nome_usuario, admin):
  """Gera uma lista de fragmentos de HTML que descrevem os botões da linha 1 do menu
  geral.  Estes botões são mostrados para todos os usuários, mas
  dependem do tipo de usuário (normal ou administrador) e se o
  usuário está logado."""

  # Botões da primeira linha que sempre aparecem:
  ht_bt_principal = html_elem_button_simples.gera("Principal", 'principal', None, '#60a3bc')

  botoes = ( ht_bt_principal, )
  if logado:
    # Gera outros botões de usuario normal logado
    botoes += gera_botoes_linha_1_logado(nome_usuario, admin)
  else:
    # Gera outros botões de usuário deslogado:
    botoes += gera_botoes_linha_1_deslogado()
  return botoes

def gera_botoes_linha_1_logado(nome_usuario, admin):
  """Gera uma lista de fragmentos HTML com os botões da linha 1 do menu
  geral, para um usuário que está logado."""
  botoes_sempre = (
      html_elem_button_simples.gera("Minha Conta", 'solicitar_pag_alterar_usuario', None, '#eeeeee'),
      html_elem_button_simples.gera("Minhas Sessões", 'ver_sessoes', None, '#eeeeee'),
      html_elem_button_simples.gera("Sair", 'fazer_logout', None, '#eeeeee'),
      gera_nome_usuario(nome_usuario)
    )
  if admin:
    botoes_sempre += (
      html_elem_button_simples.gera("Buscar usuários", 'solicitar_pag_buscar_usuarios', None, '#eeeeee'),
      html_elem_button_simples.gera("Buscar Videos", 'solicitar_pag_buscar_videos', None, '#eeeeee'),
    )
    botoes_videos = ( )
  else:
    botoes_videos = (
      html_elem_button_simples.gera("Meus Videos", 'ver_videos', None, '#eeeeee'),
    )
  return botoes_sempre + botoes_videos

def gera_botoes_linha_1_deslogado():
  """Gera uma lista de fragmentos HTML com os botões da linha 1 do menu
  geral, para um usuário que não está logado."""
  botoes = (
    html_elem_button_simples.gera("Entrar", 'solicitar_pag_login', None, '#55ee55'),
    html_elem_button_simples.gera("Cadastrar", 'solicitar_pag_cadastrar_usuario', None, '#eeeeee'),
  )
  return botoes

def gera_botoes_linha_2():
  """Gera uma lista de fragmentos de HTML com os botões da linha 2 do menu
  geral.  Estes botões são mostrados apenas se o usuário está logado
  e é um administrador."""

  ht_busca_obj_input = html_elem_input.gera(None, "text", "id_objeto", None, None, True, "Id do objeto", None)
  ht_busca_obj_bt = html_elem_button_submit.gera("Checar Objeto", "ver_objeto", None, '#ffdd22')
  ht_busca_obj_form = html_elem_form.gera(ht_busca_obj_input + ht_busca_obj_bt)
  botoes = ( ht_busca_obj_form, )
  return botoes

def gera_nome_usuario(nome_usuario):
  """Gera o texto "Oi {nome}" para o menu geral."""
  res = html_elem_span.gera(None, "Oi " + nome_usuario)
  return res