
import html_elem_input
import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form
import obj_usuario
import obj_sessao

def gera(atrs, ses):

  if ses != None and obj_sessao.aberta(ses):
    # Obtem o dono da sessão corrente:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
    para_admin = obj_usuario.eh_administrador(ses_dono)
  else:
    para_admin = False

  # Tupla contendo as seguintes informações: {rot} {tipo} {chave} {editavel} {dica}
  # Para um maior detalhamento, cheque a documentação de `html_bloco_tabela_de_campos.gera`.
  dados_linhas = (
    ( "ID",       "text",   'video',  True,  "V-NNNNNNNN",      ),
    ( "Título",   "text",   'titulo', True,  "Bla bla bla",     ),
    ( "Autor",    "text",   'autor',  True,  "U-NNNNNNNN",   ),
    ( "Data",     "text",   'data',   True,  "2024",            ),
  )

  if para_admin:
    dados_linhas += (("Bloqueado", "checkbox", 'bloqueado', True, ""),)
  # #55ee55
  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)
  ht_submit = html_elem_button_submit.gera("Buscar", "buscar_videos", None, None)
  ht_cancel = html_elem_button_simples.gera("Cancelar", "pag_principal", None, None)

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_elem_form.gera(ht_conteudo, False)
