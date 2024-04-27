import obj_video
import html_linha_resumo_de_video
import html_elem_table
import html_elem_div
import html_estilo_cabecalho_de_tabela
import html_bloco_titulo

def gera(lista_ids_vid):
  # Linha de cabeçalho:
  est_cab = html_estilo_cabecalho_de_tabela.gera()
  cabs_raw = ['Título', 'Data', 'Duração', 'Largura', 'Altura']
  cabecalho = [].copy()
  for cb in cabs_raw:
    cabecalho.append(html_elem_div.gera(est_cab, cb))

  linhas = [].copy()
  for id_vid in lista_ids_vid:
    # busca por identificador do video no banco
    vid = obj_video.busca_por_identificador(id_vid)

    # Gera uma lista de fragmentos HTML com as informacoes desse video
    res_campos = html_linha_resumo_de_video.gera(vid)

    # Adiciona essa lista à lista de linhas para a tabela HTML.
    # Selecionamos apenas os elementos que queremos.
    # Nesse caso, todos de res_campos exceto ht_usr, que é o usuário e não devemos mostrar.
    # Dessa forma mantemos a informação completa em html_linha_resumo_de_video e res_campos caso seja necessário eventualmente.
    linhas.append(res_campos[1:])

  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas, cabecalho)

  return ht_tabela
