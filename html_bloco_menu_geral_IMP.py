import html_elem_button_simples
import html_elem_span
import html_elem_button_submit
import html_elem_input
import html_elem_form
import html_bloco_bemvindo
import obj_sessao
import obj_usuario

from util_erros import erro_prog, aviso_prog

# Outros módulos importados por esta implementação:
import re
import sys

bmu_debug = False

def gera(usr):
  usr_admin = obj_usuario.eh_administrador(usr) if usr != None else False
  
  hts_linhas = []
  
  # Mensagem de boas-vindas:
  hts_linhas.append(html_bloco_bemvindo.gera(usr))
  hts_linhas.append("<br/>")
  hts_linhas.append(gera_linha(gera_botoes_de_busca(usr)))
  hts_linhas.append(gera_linha(gera_botoes_linha_principal(usr)))
  if usr_admin:
    hts_linhas.append(gera_linha(gera_botoes_linha_admin(usr)))
  
  ht_menu = "".join(hts_linhas)
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

def gera_botoes_de_busca(usr):
  """Gera uma lista de fragmentos de HTML que descrevem os botões 
  de busca do menu: "Buscar usuários", "Buscar vídeos", "Buscar comentários", 
  "Buscar sessões". 
  
  Os dois primeiros aparecem sempre, mesmo para um usuário que não está
  logado ({usr = None}). O último só aparece se o usuário {usr} não for {None}
  e for um administrador."""
  
  if bmu_debug: sys.stderr.write("    > gera_botoes_de_busca\n")

  #cor_bt_busca = "#eeccff"
  usr_admin = obj_usuario.eh_administrador(usr) if usr != None else False

  hts_botoes = []
  
  # Botões da primeira linha que sempre aparecem:
  ht_bt_busc_usr = html_elem_button_simples.gera("Buscar usuários",    'solicitar_pag_buscar_usuarios',     None, None)
  hts_botoes.append(ht_bt_busc_usr)
  
  ht_bt_busc_vid = html_elem_button_simples.gera("Buscar videos",      'solicitar_pag_buscar_videos',       None, None)
  hts_botoes.append(ht_bt_busc_vid)

  ht_bt_busc_com = html_elem_button_simples.gera("Buscar Comentários", 'solicitar_pag_buscar_comentarios',  None, None)
  hts_botoes.append(ht_bt_busc_com)

  if usr_admin:
    # Buscar sessões só para administrador
    ht_bt_busc_ses = html_elem_button_simples.gera("Buscar Sessões",     'solicitar_pag_buscar_sessoes',      None, None)
    hts_botoes.append(ht_bt_busc_ses)

  if bmu_debug: sys.stderr.write("    < gera_botoes_de_busca: hts_botoes = %s\n" % str(hts_botoes))
  
  return hts_botoes

def gera_botoes_linha_principal(usr):
  """Gera uma lista de fragmentos de HTML que descrevem os botões 
  da linha principal do menu geral.
  
  Estes botões são mostrados para todos os usuários, mas
  dependem do tipo de usuário (normal ou administrador) e se o
  usuário está usr_id.  Os parâmetros {"""

  if bmu_debug: sys.stderr.write("    > gera_botoes_linha_principal\n")

  cor_bt_home = "#60a3bc"

  hts_botoes = []

  # Botões que sempre aparecem:
  ht_bt_principal = html_elem_button_simples.gera("Principal", 'pag_principal', None, None)
  hts_botoes.append(ht_bt_principal)

  # Botões que dependem de estar logado ou não:

  if usr != None:
    # Gera outros botões de usuario normal logado:
    hts_botoes += gera_botoes_linha_principal_logado(usr)
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

  hts_botoes = []
  
  ht_bt_entrar = html_elem_button_simples.gera("Entrar",     'solicitar_pag_login',             None, None)
  hts_botoes.append(ht_bt_entrar)
  
  ht_bt_cadastrar = html_elem_button_simples.gera("Cadastrar",  'solicitar_pag_cadastrar_usuario', None, None)
  hts_botoes.append(ht_bt_cadastrar)

  if bmu_debug: sys.stderr.write("    < gera_botoes_linha_principal_deslogado: hts_botoes = %s\n" % str(hts_botoes))

  return hts_botoes

def gera_botoes_linha_principal_logado(usr):
  """Gera uma lista de fragmentos HTML com os botões da linha principal do menu
  geral, que só aparecem para um usuário {usr} que está logado ({usr != None})."""
  
  if bmu_debug: sys.stderr.write("    > gera_botoes_linha_principal_logado\n")

  # Obtem atributos do usuário:
  assert usr != None
  usr_admin = obj_usuario.eh_administrador(usr)
  usr_nome = obj_usuario.obtem_atributo(usr, 'nome')
  usr_num_ses = len(obj_sessao.busca_por_dono(usr, soh_abertas = True)) # Para botão "Minhas Sessões".

  cor_bt_meus = "#c8fac8"
  cor_bt_sair = "#ffcc88"

  hts_botoes = []
 
  ht_bt_conta = html_elem_button_simples.gera("Minha Conta", 'ver_usuario', None, None)
  hts_botoes.append(ht_bt_conta)

  ht_bt_ses_texto = "Minhas Sessões (%d)" % usr_num_ses
  ht_bt_ses = html_elem_button_simples.gera(ht_bt_ses_texto, 'buscar_sessoes_de_usuario', None, cor_bt_meus)
  hts_botoes.append(ht_bt_ses)

  ht_bt_vid = html_elem_button_simples.gera("Meus Videos", 'buscar_videos_de_usuario', None, None)
  hts_botoes.append(ht_bt_vid)
  
  ht_bt_com = html_elem_button_simples.gera("Meus Comentários", 'buscar_comentarios_de_usuario', None, None)
  hts_botoes.append(ht_bt_com)
  
  ht_bt_upload = html_elem_button_simples.gera("Subir Video", 'solicitar_pag_upload_video', None, None)
  hts_botoes.append(ht_bt_upload)
  
  ht_bt_sair = html_elem_button_simples.gera("Sair", 'fazer_logout', None, None)
  hts_botoes.append(ht_bt_sair)

  if bmu_debug: sys.stderr.write("    < gera_botoes_linha_principal_logado: hts_botoes = %s\n" % str(hts_botoes))
  return hts_botoes

def gera_botoes_linha_admin(usr):
  """Gera uma lista de fragmentos de HTML com os botões da linha do menu
  geral que só aparece se o usuário está usr_id
  e é um administrador."""
  
  if bmu_debug: sys.stderr.write("    > gera_botoes_linha_admin\n")

  cor_bt_busca = "#eeccff"

  ht_busca_obj_input = html_elem_input.gera("text", "objeto", None, None, None, True, "Id do objeto", None, False)
  ht_busca_obj_bt =    html_elem_button_submit.gera("Checar Objeto", "ver_objeto", None, None)
  ht_busca_obj_form = html_elem_form.gera(ht_busca_obj_input + ht_busca_obj_bt, False)
  hts_botoes = [ ht_busca_obj_form, ]
  if bmu_debug: sys.stderr.write("    < gera_botoes_linha_admin: hts_botoes = %s\n" % str(hts_botoes))
  return hts_botoes
