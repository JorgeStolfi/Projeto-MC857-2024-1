import html_bloco_tabela_de_campos
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(atrs):

  dados_linhas = ( 
    ("autor", "text", "autor", False, None),
    ("video", "text", "video", False, None),
    ("pai", "text", "pai", False, None),
    ("texto", "text", "texto", True, "Texto exemplo.")
  )

  ht_tabela = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)
  
  ht_submit = html_elem_button_submit.gera("Enviar", "fazer_postar_comentario", None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')
  ht_conteudo = \
    ( ht_tabela + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )

  ht_form = html_elem_form.gera(ht_conteudo, False)
  
  return ht_form
