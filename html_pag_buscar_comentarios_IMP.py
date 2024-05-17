import html_pag_generica
import html_form_buscar_comentarios
import obj_sessao

def gera(ses, atrs, erros):
  para_admin = ses != None and obj_sessao.de_administrador(ses)
  ht_form = html_form_buscar_comentarios.gera(atrs, para_admin)
  pag = html_pag_generica.gera(ses, ht_form, erros)
  return pag
