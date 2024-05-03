import obj_sessao
import html_linha_resumo_de_sessao
import html_elem_table
import html_elem_div
import html_elem_span
import sys
import html_bloco_titulo

import sys

def gera(lista_ids_ses, bt_ver, bt_fechar):

  linhas = [].copy()
  
  cabecalhos = html_linha_resumo_de_sessao.gera(None, False, False)
  linhas.append(cabecalhos)
  
  for id_ses in lista_ids_ses:
    # busca por identificador da sessao no banco
    ses = obj_sessao.obtem_objeto(id_ses)

    # Gera uma lista de fragmentos HTML com as informacoes dessa sessao
    res_campos = html_linha_resumo_de_sessao.gera(ses, bt_ver, bt_fechar)

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)
    
  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas)

  # Devolve a tabela HTML
  return ht_tabela
