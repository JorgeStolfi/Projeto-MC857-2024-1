import obj_comentario
import html_linha_resumo_de_comentario

import html_elem_table
import html_elem_div
import html_estilo_cabecalho_de_tabela


def gera(lista_ids_com, mostra_autor, mostra_video):
  # Linha de cabeçalho:
  est_cab = html_estilo_cabecalho_de_tabela.gera()
  # !!! Apresentar TODOS os campos, considerando {mostra_autor} e {mostra_video}. !!! 
  cabs_raw = ['Video', 'Autor',  'Data', 'Comentário',  'Texto', 'Link']
  hts_cabecalho = [].copy()
  for cb in cabs_raw:
    if cb == 'Autor':
      if mostra_autor:
        hts_cabecalho.append(html_elem_div.gera(est_cab, cb))
    elif cb == 'Video':
      if mostra_video:
        hts_cabecalho.append(html_elem_div.gera(est_cab, cb))
    else:
      hts_cabecalho.append(html_elem_div.gera(est_cab, cb))

  # Linhas da tabela - uma lista de listas de fragmentos HTML:
  hts_linhas = [].copy()
  for id_com in lista_ids_com:
    # busca por identificador do comentario no banco
    com = obj_comentario.busca_por_identificador(id_com)
    # Gera uma lista de fragmentos HTML com as informacoes desse comentario
    res_campos = html_linha_resumo_de_comentario.gera(com, mostra_autor, mostra_video)

    # Adiciona essa lista à lista de hts_linhas para a tabela HTML:
    hts_linhas.append(res_campos)

  # Gera a tabela HTML a partir da lista de hts_linhas
  ht_tabela = html_elem_table.gera(hts_linhas, hts_cabecalho)

  return ht_tabela
