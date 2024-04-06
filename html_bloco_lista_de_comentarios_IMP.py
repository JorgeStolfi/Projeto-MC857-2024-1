import obj_comentario
import html_bloco_resumo_de_comentario

import html_elem_table
import html_elem_div
import html_estilo_cabecalho_de_tabela


def gera(lista_ids_com):
  # Linha de cabeçalho:
  est_cab = html_estilo_cabecalho_de_tabela.gera()
  cabs_raw = ['Autor', 'Comentario']
  cabecalho = [].copy()
  for cb in cabs_raw:
    cabecalho.append(html_elem_div.gera(est_cab, cb))

  linhas = [].copy()
  for id_com in lista_ids_com:
    # busca por identificador do comentario no banco
    comentario = obj_comentario.busca_por_identificador(id_com)
    # Gera uma lista de fragmentos HTML com as informacoes desse comentario
    res_campos = html_bloco_resumo_de_comentario.gera(comentario)

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)

  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas, cabecalho)

  # ht_titulo = html_bloco_cabecalho.gera("Usuários", False)
  ht_conteudo = ht_tabela

  # Devolve a tabela HTML
  return ht_conteudo
