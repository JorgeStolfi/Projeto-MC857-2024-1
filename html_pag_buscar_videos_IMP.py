import html_pag_generica
import html_form_buscar_videos

def gera(ses, atrs, admin, erros):
  ht_form = html_form_buscar_videos.gera(atrs, admin)
  pag = html_pag_generica.gera(ses, ht_form, erros)
  return pag
