import obj_usuario
import html_bloco_resumo_de_usuario
import html_elem_table
import html_elem_div
import html_elem_span
import sys
import html_estilo_cabecalho_de_tabela
import html_bloco_cabecalho

def gera(lista_ids_usr, bt_ver, bt_fechar):

  # Linha de cabeçalho:
  cabs_raw = ['Usuário', 'Email']
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_elem_div.gera(html_estilo_cabecalho_de_tabela.gera(), cb))

  linhas = [].copy()
  for id_usr in lista_ids_usr:
    # busca por identificador da usuario no banco
    ses = obj_usuario.busca_por_identificador(id_usr)

    # Gera uma lista de fragmentos HTML com as informacoes dessa usuario
    res_campos = html_bloco_resumo_de_usuario.gera(ses, bt_ver, bt_fechar)

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)
  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_elem_table.gera(linhas, cabs_div)

  ht_cabe = html_bloco_cabecalho.gera("Minhas Sessões", False)
  ht_conteudo = \
      ht_cabe + "<br/>\n" + \
      ht_itens

  # Devolve a tabela HTML
  return ht_conteudo
