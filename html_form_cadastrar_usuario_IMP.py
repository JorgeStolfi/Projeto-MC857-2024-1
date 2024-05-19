import html_bloco_dados_de_usuario
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(atrs, para_admin):

  # Validação de argumentos (paranóia):
  assert atrs == None or isinstance(atrs, dict), "{atrs} inválido"
  assert isinstance(para_admin, bool), "{para_admin} inválido"

  atrs_tab = atrs.copy() if atrs != None else {}

  # Constrói tabela com dados:
  usr_id = None
  editavel = True
  para_proprio = True # Porque vai ser criado
  ht_tabela = html_bloco_dados_de_usuario.gera(usr_id, atrs_tab, editavel, para_admin, para_proprio)

  # Constrói formulário com botões 'Confirmar' e 'Cancelar':
  ht_bt_submit = html_elem_button_submit.gera("Cadastrar", 'cadastrar_usuario', None, None)
  ht_bt_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal',     None, None)
  
  ht_conteudo = \
    ( ht_tabela + "<br/>\n" ) + \
    ( ht_bt_submit + " " ) + \
    ( ht_bt_cancel + "\n" )

  ht_form = html_elem_form.gera(ht_conteudo, False)
  
  return ht_form
