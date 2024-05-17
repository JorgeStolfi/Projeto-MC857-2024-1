import html_pag_generica
import html_form_buscar_usuarios
import obj_sessao

def gera(ses, atrs, erros):
  para_admin = obj_sessao.de_administrador(ses) if ses != None else False
  ht_form = html_form_buscar_usuarios.gera(atrs, para_admin)
  pag = html_pag_generica.gera(ses, ht_form, erros)
  return pag
