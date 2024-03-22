import html_bloco_dados_de_video
import html_pag_generica
import html_elem_button_simples
import html_bloco_dados_de_video
import html_elem_form
import obj_video

def gera(ses, vid, erros):
  ht_bloco_vid = html_bloco_dados_de_video.gera(vid, None, False, False)

  ht_form_vid = html_elem_form.gera(ht_bloco_vid)

  pag = html_pag_generica.gera(ses, ht_bloco_vid, erros)
  return pag
