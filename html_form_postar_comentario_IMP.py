import html_bloco_tabela_de_campos
import html_elem_input
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(id_autor, atrs):
  # Constrói tabela com dados:
  atrs = { 'autor': id_autor } 
  
  # dados_linhas = ( ... )
  # ht_tabela = html_bloco_tabela_de_campos.gera(dados_linas, atrs)
  
  ht_tabela = "!!! implementação de {html_form_postar_comentario.gera} ainda não completada !!!"

  ht_submit = html_elem_button_submit.gera("Enviar", "fazer_upload_video", None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')
  ht_conteudo = \
    ( ht_tabela + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )

  ht_form = html_elem_form.gera(ht_conteudo)
  
  return ht_form
