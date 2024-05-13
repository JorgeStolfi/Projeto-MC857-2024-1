import obj_video
import obj_sessao
import obj_usuario

import html_form_alterar_video
import html_pag_generica
import html_elem_button_simples

def gera(ses, vid_id, atrs, erros):

  # Páginas geradas pelo sistema deveriam satisfazer estas condições:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert vid_id != None and type(vid_id) is str, "Identificador de vídeo inválido"
  assert atrs == None or type(atrs) is dict
  assert erros == None or type(erros) is tuple or type(erros) is list
  
  # Obtem o vídeo a alterar. Nesta altura deve existir:
  vid = obj_video.obtem_objeto(vid_id) 
  assert vid != None, f"Vídeo {vid_id} não existe"
  
  # Obtem o usuário da sessão, para determinar que campos são editáveis:
  usr_ses = obj_sessao.obtem_dono(ses)
  assert usr_ses != None
  para_admin = obj_usuario.eh_administrador(usr_ses)
  
  # Cria o formulário básico:
  ht_form = html_form_alterar_video.gera(vid_id, atrs, para_admin)
    
  ht_conteudo = ht_form

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)

  return pag
