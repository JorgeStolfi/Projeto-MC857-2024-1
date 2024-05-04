
import html_elem_input
import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form

def gera(atrs, admin):

  dados_linhas = (
      ( "ID",         "text",   "usuario",   True,  "U-nnnnnnnn",       ),
      ( "Nome",       "text",   "nome",      True,  "Fulano de tal",    ),
      ( "email",      "email",  "email",     True,  "fulano@gmail.com", ),
    )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)
  ht_submit = html_elem_button_submit.gera("Buscar", "buscar_usuarios", None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", "pag_principal", None, '#ee5555')

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_elem_form.gera(ht_conteudo, False)
