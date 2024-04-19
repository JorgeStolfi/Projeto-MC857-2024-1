import html_pag_generica
import html_form_buscar_comentarios

def gera(ses, atrs, erros):
  ht_form = html_form_buscar_comentarios.gera(atrs)
  pag = html_pag_generica.gera(ses, ht_form, erros)
  return pag
