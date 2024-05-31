import obj_comentario
import html_linha_resumo_de_comentario

import html_elem_table
import html_elem_div

def gera(com_ids, para_admin, mostra_autor, mostra_video, mostra_pai, mostra_nota):

  # Linhas da tabela: uma lista de listas de fragmentos HTML:
  linhas = []

  cabecalhos = html_linha_resumo_de_comentario.gera \
    ( None, para_admin, mostra_autor, mostra_video, mostra_pai, mostra_nota)
  linhas.append(cabecalhos)
  
  for com_id in com_ids:
    # busca por identificador do comentario no banco
    com = obj_comentario.obtem_objeto(com_id)
    # Gera uma lista de fragmentos HTML com as informacoes desse comentario
    res_campos = html_linha_resumo_de_comentario.gera(com, para_admin, mostra_autor, mostra_video, mostra_pai, mostra_nota)

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)

  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas, "width: 100%")

  return ht_tabela
