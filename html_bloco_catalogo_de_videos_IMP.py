import obj_video
import html_linha_catalogo_de_videos
import html_elem_table
import html_elem_div
import html_bloco_titulo
import html_elem_button_simples
import sys


def gera_form_botoes_de_ordenacao():
  cor_bt_ordem = "#eeccff"

  ht_bt_melhores = html_elem_button_simples.gera("Melhores", 'ver_grade_de_videos', { 'ordem': "-nota" }, cor_bt_ordem)
  ht_bt_piores = html_elem_button_simples.gera("Piores", 'ver_grade_de_videos', { 'ordem': "+nota" }, cor_bt_ordem)

  ht_bt_mais_antigos = html_elem_button_simples.gera("Mais antigos", 'ver_grade_de_videos', { 'ordem': "-data" }, cor_bt_ordem)
  ht_bt_mais_recentes = html_elem_button_simples.gera("Mais recentes", 'ver_grade_de_videos', { 'ordem': "+data" }, cor_bt_ordem)

  ht_bt_mais_vistos = html_elem_button_simples.gera("Mais vistos", 'ver_grade_de_videos', { 'ordem': "+vistas" }, cor_bt_ordem)
  ht_bt_menos_vistos = html_elem_button_simples.gera("Menos vistos", 'ver_grade_de_videos', { 'ordem': "-vistas" }, cor_bt_ordem)

  ht_bt_aleatorios = html_elem_button_simples.gera("Aleatórios", 'ver_grade_de_videos', {}, cor_bt_ordem)

  ht_botoes = \
    ht_bt_melhores + " " + \
    ht_bt_piores + "<br/>" + \
    ht_bt_mais_recentes + " " + \
    ht_bt_mais_antigos + "<br/>" + \
    ht_bt_mais_vistos + " " + \
    ht_bt_menos_vistos + "<br/>" + \
    ht_bt_aleatorios
  
  return ht_botoes


def gera(vid_ids, mostra_autor):
  
  # Generate order buttons and place them at the top
  ht_botoes_ordenacao = gera_form_botoes_de_ordenacao()

  # Linhas da tabela:
  linhas = []
  
  for vid_id in vid_ids:
    # busca por identificador do video no banco
    vid = obj_video.obtem_objeto(vid_id)

    # Gera uma lista de fragmentos HTML com as informacoes desse video
    linha_vid = html_linha_catalogo_de_videos.gera(vid, mostra_autor)

    # Adiciona essa lista à lista de linhas para a tabela HTML.
    linhas.append(linha_vid)

  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas, None)

  ht_bloco = ht_botoes_ordenacao + ht_tabela
  return ht_bloco