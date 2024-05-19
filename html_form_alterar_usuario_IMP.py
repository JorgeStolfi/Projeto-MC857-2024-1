import html_bloco_dados_de_usuario
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(usr_id, atrs, para_admin):

  # Validação de argumentos (paranóia):
  assert usr_id != None and type(usr_id) is str
  assert atrs == None or type(atrs) is dict
  assert type(para_admin) is bool

  # Constrói tabela com dados:
  editavel = True
  para_proprio = not para_admin
  ht_table = html_bloco_dados_de_usuario.gera(usr_id, atrs, editavel, para_admin, para_proprio)

  # Constrói formulário com botões 'Confirmar' e 'Cancelar':
  ht_submit = html_elem_button_submit.gera("Confirmar alterações", 'alterar_usuario', None, None)
  conteudo_form = \
    ( ht_table + "<br/>\n" ) + \
    ( ht_submit + " " )

  ht_form = html_elem_form.gera(conteudo_form, False)
  
  return ht_form
