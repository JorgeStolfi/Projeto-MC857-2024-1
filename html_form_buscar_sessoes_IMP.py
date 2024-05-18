import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form

def gera(atrs, admin):

  dados_linhas = (
      ( "Usuário", "text",     'dono',    True,  "U-nnnnnnnn" ),
      ( "Sessão",  "text",     'sessao',  True,  "S-nnnnnnnn" ),
      ( "Aberta",  "checkbox", 'aberta',  True,  ""           ),
      ( "Cookie",  "text",     'cookie',  True,  ""           ),
    )
  #'#55ee55'
  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)
  ht_submit = html_elem_button_submit.gera("Buscar", "buscar_sessoes", None, None)
  ht_cancel = html_elem_button_simples.gera("Cancelar", "pag_principal", None, None)

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  ht_form = html_elem_form.gera(ht_conteudo, False)
  
  return ht_form
