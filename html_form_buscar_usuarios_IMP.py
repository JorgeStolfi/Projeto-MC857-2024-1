
import html_elem_input
import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form

def gera(atrs, para_admin):

  dados_linhas = [
      ( "ID",           "text",     "usuario",    True,     "U-nnnnnnnn",        ),
      ( "Nome",         "text",     "nome",       True,     "Fulano de tal",     ),
      ( "Vnota desde",  "number",   "vnotaMin",   True,     "Nota mínima",   True),
      ( "Vnota até",    "number",   "vnotaMax",   True,     "Nota máxima",   True),
      ( "Cnota desde",  "number",   "cnotaMin",   True,     "Nota mínima",   True),
      ( "Cnota até",    "number",   "cnotaMax",   True,     "Nota máxima",   True),
    ]
  atrs["vnotaMin_min"] = 0
  atrs["vnotaMax_min"] = 0
  atrs["cnotaMin_min"] = 0
  atrs["cnotaMax_min"] = 0
  
  if para_admin:
    dados_linhas.append( ( "email", "text", "email", True,  "fulano@lugar.com", ) )
  #'#55ee55'
  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)
  ht_submit = html_elem_button_submit.gera("Buscar", "buscar_usuarios", None, None)
  ht_cancel = html_elem_button_simples.gera("Cancelar", "pag_principal", None, None)

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_elem_form.gera(ht_conteudo, False)
