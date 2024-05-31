import html_pag_generica
import html_form_buscar_comentarios
import html_bloco_titulo
import obj_sessao

def gera(ses, atrs, erros):
  para_admin = ses != None and obj_sessao.de_administrador(ses)
  titulo = html_bloco_titulo.gera('Dados para busca de comentários')
  ht_form = html_form_buscar_comentarios.gera(atrs, para_admin)

  html = titulo + ht_form
  pag = html_pag_generica.gera(ses, html, erros)
  return pag
