import obj_comentario
import html_linha_resumo_de_comentario

import html_elem_table
import html_elem_div


def gera(lista_ids_com, mostra_autor, mostra_video, mostra_pai):

  # Linhas da tabela: uma lista de listas de fragmentos HTML:
  linhas = [].copy()

  cabecalhos = html_linha_resumo_de_comentario.gera(None, mostra_autor, mostra_video, mostra_pai)
  linhas.append(cabecalhos)
  
  for id_com in lista_ids_com:
    # busca por identificador do comentario no banco
    com = obj_comentario.obtem_objeto(id_com)
    # Gera uma lista de fragmentos HTML com as informacoes desse comentario
    res_campos = html_linha_resumo_de_comentario.gera(com, mostra_autor, mostra_video, mostra_pai)

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)

  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas)

  return ht_tabela
