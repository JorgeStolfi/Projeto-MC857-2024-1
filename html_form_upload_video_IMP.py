import html_elem_input
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit
import html_elem_label
import html_bloco_tabela_de_campos

def gera(id_autor, atrs):

  atrs = atrs.copy() # Para não alterar o original.
  
  dados_linhas = [].copy()

  dados_linhas.append( ( "Autor",    "text",     'autor',     False,  None,  ) )
  dados_linhas.append( ( "Titulo",   "textarea", 'titulo',    True,   None,  ) )
  dados_linhas.append( ( "Arquivo",  "file",     'arquivo',   True,   None,  ) )

  ht_tabela = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)

  ht_submit = html_elem_button_submit.gera("Enviar", "fazer_upload_video", None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')

  ht_conteudo = f"{ht_tabela}\n{ht_rotulo} {ht_upload}\n\n{ht_submit}\n{ht_cancel}"

  ht_form = html_elem_form.gera(ht_conteudo)
  
  return ht_form
