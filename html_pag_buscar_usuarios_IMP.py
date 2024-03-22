import html_pag_generica
import html_form_buscar_usuarios

def gera(ses, atrs, admin, erros):
  ht_form = html_form_buscar_usuarios.gera(atrs, admin)
  pag = html_pag_generica.gera(ses, ht_form, erros)
  return pag
