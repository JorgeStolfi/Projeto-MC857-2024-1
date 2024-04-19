import html_bloco_dados_de_video
import html_pag_generica
import html_elem_button_simples
import html_bloco_dados_de_video
import html_elem_form
import obj_video

def gera(ses, vid, erros):

  id_vid = obj_video.obtem_identificador(vid)
  atrs_vid = obj_video.obtem_atributos(vid)
  ht_bloco_vid = html_bloco_dados_de_video.gera(id_vid, atrs_vid, True, False)
  ht_form_vid = html_elem_form.gera(ht_bloco_vid)

  pag = html_pag_generica.gera(ses, ht_bloco_vid, erros)
  return pag
