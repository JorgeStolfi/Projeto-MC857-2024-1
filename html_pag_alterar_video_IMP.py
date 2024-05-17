import obj_video
import obj_sessao
import obj_usuario

import html_form_alterar_video
import html_pag_generica
import html_elem_button_simples

def gera(ses, vid_id, atrs_mod, erros):

  # Páginas geradas pelo sistema deveriam satisfazer estas condições:
  assert ses != None and obj_sessao.aberta(ses)
  assert vid_id != None and type(vid_id) is str
  assert atrs_mod == None or type(atrs_mod) is dict
  assert erros == None or type(erros) is tuple or type(erros) is list
  
  atrs_mod = atrs_mod.copy() if atrs_mod != None else { }
  
  # Obtem o vídeo a alterar. Nesta altura deve existir:
  vid = obj_video.obtem_objeto(vid_id) 
  assert vid != None, f"Vídeo {vid_id} não existe"
  
  # Obtem o usuário da sessão, para determinar que campos são editáveis:
  ses_dono = obj_sessao.obtem_dono(ses)
  assert ses_dono != None
  para_admin = obj_usuario.eh_administrador(ses_dono)
  
  # Cria o formulário básico:
  ed_nota = para_admin
  ht_form = html_form_alterar_video.gera(vid_id, atrs_mod, ed_nota)
    
  ht_conteudo = ht_form

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)

  return pag
