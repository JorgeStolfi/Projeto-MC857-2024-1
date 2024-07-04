import obj_sessao
import html_linha_resumo_de_sessao
import html_elem_table
import html_elem_div
import html_elem_span
import sys
import html_bloco_titulo

import sys

def gera(ses_ids, bt_ver, bt_fechar, mostra_dono):

  linhas = []
  
  cabecalhos = html_linha_resumo_de_sessao.gera(None, False, False, mostra_dono)
  linhas.append(cabecalhos)
  
  for ses_id in ses_ids[::-1]:
    # busca por identificador da sessao no banco
    ses = obj_sessao.obtem_objeto(ses_id)

    # Gera uma lista de fragmentos HTML com as informacoes dessa sessao
    res_campos = html_linha_resumo_de_sessao.gera(ses, bt_ver, bt_fechar, mostra_dono)

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)
    
  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas, None)

  # Devolve a tabela HTML
  return ht_tabela
