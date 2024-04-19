import html_elem_input
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit
import html_elem_label

def gera(id_autor, atrs):
  # Constrói tabela com dados:
  atrs = { 'autor': id_autor } 
  
  # !!! módulo html_pag_upload_video ainda não terminado !!!"
  ht_rotulo = html_elem_label.gera("Arquivo", ":")
  ht_tabela = html_elem_input.gera("file", 'arq', None, None, None, True, "Escolha", "fazer_upload", True)

  # dados_linhas = ( ... )
  # ht_tabela = html_bloco_tabela_de_campos.gera(dados_linas, atrs)

  ht_submit = html_elem_button_submit.gera("Enviar", "fazer_upload_video", None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')
  ht_conteudo = \
    ( ht_tabela + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )

  ht_form = html_elem_form.gera(ht_conteudo)
  
  return ht_form
