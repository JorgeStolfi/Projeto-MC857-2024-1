import html_bloco_dados_de_video
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(id_vid, atrs, ses_admin):

  # Validação de argumentos (paranóia):
  assert id_vid != None and type(id_vid) is str
  assert atrs == None or type(atrs) is dict
  assert type(ses_admin) is bool

  # Constrói tabela vid dados:
  auto = not ses_admin # Caso o pedinte não seja administardor, supõe que é o autor.
  ht_table = html_bloco_dados_de_video.gera(id_vid, atrs, ses_admin, auto)

  # Constrói formulário vid botões 'Confirmar' e 'Cancelar':
  ht_submit = html_elem_button_submit.gera("Confirmar alterações", 'alterar_video', None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')
  conteudo_form = \
    ( ht_table + "<br/>\n" ) + \
    ( ht_submit + " " ) + \
    ( ht_cancel + "\n" )

  ht_form = html_elem_form.gera(conteudo_form)
  
  return ht_form
