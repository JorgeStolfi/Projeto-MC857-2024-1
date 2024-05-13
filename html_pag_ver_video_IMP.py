import html_bloco_dados_de_video
import html_pag_generica
import html_elem_button_simples
import html_elem_form
import obj_video

def gera(ses, vid, erros):

  vid_id = obj_video.obtem_identificador(vid)
  atrs_vid = obj_video.obtem_atributos(vid)
  
  ses_dono = obj_sessao.obtem_dono(ses)
  vid_autor = obj_video.obtem_autor(vid)
  
  editavel = False
  para_admin = obj_sessao.de_administrador(ses)
  para_proprio = ( ses_dono == vid-autor )
  ht_bloco_vid = html_bloco_dados_de_video.gera(vid_id, atrs_vid, editavel, para_admin, para_proprio)

  pag = html_pag_generica.gera(ses, ht_bloco_vid, erros)
  return pag
