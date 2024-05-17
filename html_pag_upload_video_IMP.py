import html_form_upload_video
import html_elem_paragraph
import html_elem_button_submit
import html_elem_form
import obj_sessao
import obj_usuario
import html_pag_generica

import sys

def gera(ses, atrs_novo, erros):

  # Chamadas pelo sistema devem satisfazer estas condições:
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  assert obj_sessao.aberta(ses)
  assert atrs_novo == None or isinstance(atrs_novo, dict)
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple)

  # Obtém dono da sessão {ses}:
  ses_dono = obj_sessao.obtem_dono(ses)
  assert ses_dono != None
  ses_dono_id = obj_usuario.obtem_identificador(ses_dono)
  para_admin = obj_usuario.eh_administrador(ses_dono)
  
  atrs_novo = atrs_novo.copy() if atrs_novo != None else { }
  
  # Garante atributos essenciais (paranóia):
  if 'autor' in atrs_novo:
    autor_novo = atrs_novo['autor']
    assert atrs_novo['autor'] == ses_dono_id
  else:
    atrs_novo['autor'] = ses_dono_id

  ht_form = html_form_upload_video.gera(atrs_novo, para_admin)
  
  ht_conteudo = ht_form

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
  
