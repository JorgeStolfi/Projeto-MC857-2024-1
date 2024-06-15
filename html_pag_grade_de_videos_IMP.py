import html_bloco_grade_de_videos
import html_bloco_catalogo_de_videos
import html_pag_generica
import html_pag_mensagem_de_erro
import html_elem_form
import obj_video
import obj_sessao
import sys

from util_erros import ErroAtrib

def gera(ses, vid_ids, ncols, catalogo, erros):

  # Estas condições deveriam ser satisfeitas em chamadas do sistema:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(vid_ids, list) or isinstance(vid_ids, tuple)
  assert isinstance(ncols, int) and ncols > 0
  assert erros == None or isinstance(erros, list) or  isinstance(erros, tuple)

  mostra_autor = True
  erros = [ ] if erros == None else list(erros)
  
  try:
    if(catalogo == 'True'):
      ht_grade = html_bloco_catalogo_de_videos.gera(vid_ids, ncols)
    else:
      ht_grade = html_bloco_grade_de_videos.gera(vid_ids, mostra_autor)
  except ErroAtrib as ex:
    erros += ex.args[0]
  
  if len(erros) > 0:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_grade, None)
  return pag
