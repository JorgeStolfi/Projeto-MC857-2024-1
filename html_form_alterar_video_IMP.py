import html_bloco_dados_de_video
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(vid_id, atrs, para_admin):

  # Validação de argumentos (paranóia):
  assert vid_id != None and type(vid_id) is str
  assert atrs == None or type(atrs) is dict
  assert type(para_admin) is bool

  # Constrói tabela com dados:
  editavel = True
  para_proprio = not para_admin
  ht_table = html_bloco_dados_de_video.gera(vid_id, atrs, editavel, para_admin, para_proprio)

  # Constrói formulário vid botão 'Confirmar':
  ht_submit = html_elem_button_submit.gera("Confirmar alterações", 'alterar_video', None, '#55ee55')
  conteudo_form = \
    ( ht_table + "<br/>\n" ) + \
    ( ht_submit + " " )

  ht_form = html_elem_form.gera(conteudo_form, False)
  
  return ht_form
