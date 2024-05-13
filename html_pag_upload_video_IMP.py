import html_form_upload_video
import html_elem_paragraph
import html_elem_button_submit
import html_elem_form
import obj_sessao
import obj_usuario
import html_pag_generica

def gera(ses, atrs, erros):

  # Validação de tipos (paranóia):
  assert ses != None and isinstance(ses, obj_sessao.Classe), "Sessao inválida"
  assert obj_sessao.aberta(ses), "Sessao já fechada"
  assert atrs == None or isinstance(atrs, dict), "{atrs} inválido"
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple), "{erros} inválido"
  
  # Obtém dono da sessão {ses}:
  usr_ses = obj_sessao.obtem_dono(ses)
  assert usr_ses != None
  usr_ses_id = obj_usuario.obtem_identificador(usr_ses)
  para_admin = obj_usuario.eh_administrador(usr_ses)
  
  atrs_pag = atrs.copy() if atrs != None else { }
  
  # Garante atributos essenciais (paranóia):
  if 'autor' in atrs_pag:
    assert atrs_pag['autor'] == usr_ses_id
  else:
    atrs_pag['autor'] = usr_ses_id

  ht_form = html_form_upload_video.gera(atrs_pag, para_admin)
  
  ht_conteudo = ht_form

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
  
