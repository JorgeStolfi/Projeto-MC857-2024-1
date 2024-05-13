import obj_usuario
import html_linha_resumo_de_usuario
import html_elem_table
import html_elem_div
import html_elem_span
import sys

def gera(usr_ids):
  linhas = []
  
  cabecalhos = html_linha_resumo_de_usuario.gera(None)
  linhas.append(cabecalhos)

  for usr_id in usr_ids:
    # busca por identificador da usuario no banco
    usr = obj_usuario.obtem_objeto(usr_id)

    # Gera uma lista de fragmentos HTML com as informacoes dessa usuario
    res_campos = html_linha_resumo_de_usuario.gera(usr)

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)

  # Gera a tabela HTML a partir da lista de linhas
  ht_tabela = html_elem_table.gera(linhas)

  return ht_tabela
