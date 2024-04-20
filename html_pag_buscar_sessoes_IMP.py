import html_pag_generica
import html_form_buscar_sessoes
import obj_sessao

def gera(ses, atrs, erros):
  admin = obj_sessao.de_administrador(ses)

  ht_form = html_form_buscar_sessoes.gera(atrs, admin)
  pag = html_pag_generica.gera(ses, ht_form, erros)
  return pag
