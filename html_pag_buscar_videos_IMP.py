import obj_sessao

import html_pag_generica
import html_bloco_titulo
import html_form_buscar_videos

def gera(ses, atrs, erros):
  
  # Verificação de tipos de dados (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(atrs, dict)
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple)

  if ses == None or not obj_sessao.aberta(ses):
    para_admin = False
  else:
    para_admin = obj_sessao.de_administrador(ses)

  ht_titulo = html_bloco_titulo.gera("Dados para a busca de vídeos")
  ht_form = html_form_buscar_videos.gera(atrs, para_admin)
  ht_bloco = \
    ht_titulo + "<br/>\n" + \
    ht_form
  pag = html_pag_generica.gera(ses, ht_bloco, erros)
  
  return pag
