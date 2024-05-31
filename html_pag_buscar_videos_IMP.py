import html_pag_generica
import html_bloco_titulo
import html_form_buscar_videos

def gera(ses, atrs, erros):
  ht_titulo = html_bloco_titulo.gera("Dados para a busca de vídeos")
  ht_form = html_form_buscar_videos.gera(ses, atrs)
  ht_bloco = \
    ht_titulo + "<br/>\n" + \
    ht_form
  pag = html_pag_generica.gera(ses, ht_bloco, erros)
  return pag
