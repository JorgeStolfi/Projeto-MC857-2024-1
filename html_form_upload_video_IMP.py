import html_bloco_dados_de_video
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(id_usr):
  # Constrói tabela com dados:

  atrs = { 'usr': id_usr } 
  ht_table = html_bloco_dados_de_video.gera(None, atrs, None, None)

  # Constrói formulário com botões 'Entrar' e 'Cancelar':
  ht_submit = html_elem_button_submit.gera("Enviar", "fazer_upload_video", None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'principal', None, '#ee5555')
  conteudo_form = \
    ( ht_table + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )

  ht_form = html_elem_form.gera(conteudo_form)
  
  return ht_form
