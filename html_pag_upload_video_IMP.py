import html_form_upload_video
import html_elem_paragraph
import html_elem_button_submit
import html_elem_form
import obj_sessao
import obj_usuario
import html_pag_generica

def gera(ses, atrs, erros):

  # Estas condições deveriam ser garantidas para pedidos gerados pelo site:
  assert ses != None and type(ses) is obj_sessao.Classe
  assert obj_sessao.aberta(ses)
  assert atrs == None or type(atrs) is dict
  assert erros == None or type(erros) is list or type(erros) is tuple

  # !!! Fazer funcionar !!!
  
  usr_ses = obj_sessao.obtem_usuario(ses)
  assert usr_ses != None
  usr_ses_id = obj_usuario.obtem_identificador(usr_ses)
  
  autor_id = usr_ses_id
  atrs_id = { }
  
  ht_form = html_form_upload_video.gera(usr_ses_id, atrs_id)
  
  ht_conteudo = ht_form

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
  
