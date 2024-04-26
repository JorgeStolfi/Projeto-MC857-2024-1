import html_elem_button_simples
import html_elem_span
import html_elem_button_submit
import html_elem_input
import html_elem_form

from util_erros import erro_prog

# Outros módulos importados por esta implementação:
import re
import sys

bmu_debug = False

def gera(logado, nome_usuario, admin):
  ht_menu = \
    gera_linha(gera_botoes_de_busca(admin)) + \
    gera_linha(gera_botoes_linha_principal(logado, nome_usuario, admin))
  if admin:
    ht_menu += gera_linha(gera_botoes_linha_admin())
  return ht_menu

def gera_linha(botoes):
  """Monta uma linha do menu geral, dada uma lista de fragmentos HTML que
  descrevem os botões."""
  if bmu_debug: sys.stderr.write("    > gera_linha\n")
  html = "<nav>"
  for bt in botoes:
    if bmu_debug: sys.stderr.write("      bt = %s\n" % str(bt))
    if bt != None and bt != "":
      html += "  " + bt
  html += "</nav>\n"
  if bmu_debug: sys.stderr.write("    < gera_linha: html = %s\n" % str(html))
  return html

# Cada função abaixo devolve uma lista de fragmentos HTML, cada um 
# descrevendo um botão (ou outro elemento de uma linha de menu).

def gera_botoes_de_busca(admin):
  """Gera uma lista de fragmentos de HTML que descrevem os botões 
  de busca do menu: "Buscar usuários", "Buscar vídeos", "Buscar comentários", 
  "Buscar sessões". Este último só aparece se o usuário for administrador."""
  
  cor_bt_busca = "#eeccff"

  if bmu_debug: sys.stderr.write("    > gera_botoes_de_busca\n")

  # Botões da primeira linha que sempre aparecem:
  ht_bt_usr = html_elem_button_simples.gera("Buscar usuários",    'solicitar_pag_buscar_usuarios',     None, cor_bt_busca)
  ht_bt_vid = html_elem_button_simples.gera("Buscar videos",      'solicitar_pag_buscar_videos',       None, cor_bt_busca)
  ht_bt_com = html_elem_button_simples.gera("Buscar Comentários", 'solicitar_pag_buscar_comentarios',  None, cor_bt_busca)

  hts_botoes = [ ht_bt_usr, ht_bt_vid, ht_bt_com ]

  if admin:
    # Buscar sessões só para administrador
    ht_bt_ses = html_elem_button_simples.gera("Buscar Sessões",     'solicitar_pag_buscar_sessoes',      None, cor_bt_busca)
    hts_botoes.append(ht_bt_ses)
  if bmu_debug: sys.stderr.write("    < gera_botoes_de_busca: hts_botoes = %s\n" % str(hts_botoes))
  return hts_botoes

def gera_botoes_linha_principal(logado, nome_usuario, admin):
  """Gera uma lista de fragmentos de HTML que descrevem os botões da linha principal do menu
  geral.  Estes botões são mostrados para todos os usuários, mas
  dependem do tipo de usuário (normal ou administrador) e se o
  usuário está logado."""

  if bmu_debug: sys.stderr.write("    > gera_botoes_linha_principal\n")

  # Botões da primeira linha que sempre aparecem:
  
  cor_bt_home = "#60a3bc"

  ht_bt_principal = html_elem_button_simples.gera("Principal", 'pag_principal', None, cor_bt_home)
  hts_botoes = [ ht_bt_principal ]

  if logado:
    # Gera outros botões de usuario normal logado
    hts_botoes += gera_botoes_linha_principal_logado(nome_usuario, admin)
  else:
    # Gera outros botões de usuário deslogado:
    hts_botoes += gera_botoes_linha_principal_deslogado()
  if bmu_debug: sys.stderr.write("    < gera_botoes_linha_principal: hts_botoes = %s\n" % str(hts_botoes))
  return hts_botoes

def gera_botoes_linha_principal_deslogado():
  """Gera uma lista de fragmentos HTML com os botões da linha principal do menu
  geral que só aparecem para para um usuário que não está logado."""

  if bmu_debug: sys.stderr.write("    > gera_botoes_linha_principal_deslogado\n")

  cor_bt_login = "#55ff55"
  cor_bt_novo =  "#88eeff"

  hts_botoes = (
    html_elem_button_simples.gera("Entrar",     'solicitar_pag_login',             None, cor_bt_login),
    html_elem_button_simples.gera("Cadastrar",  'solicitar_pag_cadastrar_usuario', None, cor_bt_novo),
  )
  if bmu_debug: sys.stderr.write("    < gera_botoes_linha_principal_deslogado: hts_botoes = %s\n" % str(hts_botoes))
  return hts_botoes

def gera_botoes_linha_principal_logado(nome_usuario, admin):
  """Gera uma lista de fragmentos HTML com os botões da linha princpal do menu
  geral, que só aparecem para um usuário que está logado."""
  
  if bmu_debug: sys.stderr.write("    > gera_botoes_linha_principal_logado\n")

  cor_bt_meus = "#eeffee"
  cor_bt_sair = "#ffcc88"
  
  hts_botoes = (
      html_elem_button_simples.gera("Minha Conta",        'ver_usuario',                   None, cor_bt_meus),
      html_elem_button_simples.gera("Minhas Sessões",     'buscar_sessoes_de_usuario',     None, cor_bt_meus), 
      html_elem_button_simples.gera("Meus Videos",        'buscar_videos_de_usuario',      None, cor_bt_meus),
      html_elem_button_simples.gera("Meus Comentários",   'buscar_comentarios_de_usuario', None, cor_bt_meus),
      html_elem_button_simples.gera("Subir Video",        'solicitar_pag_upload_video',    None, cor_bt_meus),
      html_elem_button_simples.gera("Sair", 'fazer_logout', None, cor_bt_sair),
      gera_nome_usuario(nome_usuario, admin)
    )
  if bmu_debug: sys.stderr.write("    < gera_botoes_linha_principal_logado: hts_botoes = %s\n" % str(hts_botoes))
  return hts_botoes

def gera_botoes_linha_admin():
  """Gera uma lista de fragmentos de HTML com os botões da linha do menu
  geral que só aparece se o usuário está logado
  e é um administrador."""
  
  if bmu_debug: sys.stderr.write("    > gera_botoes_linha_admin\n")

  cor_bt_busca = "#eeccff"

  ht_busca_obj_input = html_elem_input.gera("text", "objeto", None, None, None, True, "Id do objeto", None, False)
  ht_busca_obj_bt =    html_elem_button_submit.gera("Checar Objeto", "ver_objeto", None, cor_bt_busca)
  ht_busca_obj_form = html_elem_form.gera(ht_busca_obj_input + ht_busca_obj_bt, False)
  hts_botoes = [ ht_busca_obj_form, ]
  if bmu_debug: sys.stderr.write("    < gera_botoes_linha_admin: hts_botoes = %s\n" % str(hts_botoes))
  return hts_botoes

def gera_nome_usuario(nome_usuario, admin):
  """Gera o texto "Oi {nome}" para o menu geral.  O parâmetro {admin} diz se é administrador."""
  res = html_elem_span.gera(None, "Oi " + nome_usuario)
  return res
