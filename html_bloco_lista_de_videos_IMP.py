import obj_video
import html_linha_resumo_de_video
import html_elem_table
import html_elem_div
import html_bloco_titulo
import sys
def reshape(image,size):
  pass

def gera(vid_ids, mostra_autor):
  
  # Linhas da tabela:
  linhas = []
  
  cabecalhos = html_linha_resumo_de_video.gera(None, mostra_autor)
  linhas.append(cabecalhos)
  
  for vid_id in vid_ids:
    # busca por identificador do video no banco
    vid = obj_video.obtem_objeto(vid_id)

    thumb = f'/thumbs/{vid_id}.png'

    vid.atrs.update({'thumb':thumb})
   
    # Gera uma lista de fragmentos HTML com as informacoes desse video
    linha_vid = html_linha_resumo_de_video.gera(vid, mostra_autor)

    # Adiciona essa lista à lista de linhas para a tabela HTML.
    linhas.append(linha_vid)

  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas, None)

  return ht_tabela
