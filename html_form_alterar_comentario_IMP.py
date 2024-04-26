import html_bloco_dados_de_comentario
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(id_com, atrs, ses_admin):

  # Validação de argumentos (paranóia):
  assert id_com != None and type(id_com) is str
  assert atrs == None or type(atrs) is dict
  assert type(ses_admin) is bool

  # Constrói tabela com dados:
  edita_texto = True
  ht_table = html_bloco_dados_de_comentario.gera(id_com, atrs, edita_texto)

  # Constrói formulário com botões 'Confirmar' e 'Cancelar':
  ht_submit = html_elem_button_submit.gera("Confirmar alterações", 'alterar_comentario', None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')
  conteudo_form = \
    ( ht_table + "<br/>\n" ) + \
    ( ht_submit + " " ) + \
    ( ht_cancel + "\n" )

  ht_form = html_elem_form.gera(conteudo_form, False)
  
  return ht_form
