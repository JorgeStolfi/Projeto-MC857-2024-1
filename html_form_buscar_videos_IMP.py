
import html_elem_input
import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form
import obj_usuario
import obj_sessao

def gera(atrs, para_admin):

  # Tupla contendo as seguintes informações: {rot} {tipo} {chave} {editavel} {dica}
  # Para um maior detalhamento, cheque a documentação de `html_bloco_tabela_de_campos.gera`.
  dados_linhas = (
      ( "ID",           "text",   'video',      True, "V-NNNNNNNN", ),
      ( "Título",       "text",   'titulo',     True, "Bla bla bla", ),
      ( "Autor",        "text",   'autor',      True, "U-NNNNNNNN", ),
      ( "Desde data",   "text",   'data_min',   True, "2024-05-20 15:00:00 UTC", ),
      ( "Até data",     "text",   'data_max',   True, "2024-05-24 15:00:00 UTC", ),
      ( "Nota min",     "text",   'nota_min',   True, "0.00" ),
      ( "Nota max",     "text",   'nota_max',   True, "4.00" ),
      ( "Vistas desde", "number", 'vistas_min', True, "0" ),
      ( "Vistas até",   "number", 'vistas_max', True, "10" ),
    )
    
  # Se que pediu é administardor, deixa fazer busca também por 'bloqueado'.
  if para_admin:
    dados_linhas += ( ( "Bloqueado", "checkbox", 'bloqueado', True, ""), )
    
  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)
  ht_submit = html_elem_button_submit.gera("Buscar", "buscar_videos", None, None)
  ht_cancel = html_elem_button_simples.gera("Cancelar", "pag_principal", None, None)

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_elem_form.gera(ht_conteudo, False)
