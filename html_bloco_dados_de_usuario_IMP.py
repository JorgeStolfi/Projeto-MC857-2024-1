import html_elem_input
import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form

def gera(id_usr, atrs, admin):

  # For simplicity:
  atrs = {}.copy() if atrs == None else atrs.copy()
  atrs.update( { 'id_usuario': id_usr } )

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = \
    (
      ( "Nome",             "text",     "nome",          None,                  False, ),
      ( "E-mail",           "email",    "email",         "xxx@xxx.xxx.xx",      False, ),
      ( "Senha",            "password", "senha",         None,                  False, ),
      ( "Confirmar senha",  "password", "conf_senha",    None,                  False, ),
      ( "Administrador",    "checkbox", "administrador", None,                  True,  ),
    )
    
  if id_usr != None:
    dados_linhas += \
      ( 
        ( "Identificador",    "readonly",  'id_usuario',     None,                  True, ),
      )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs, admin)

  return ht_table
