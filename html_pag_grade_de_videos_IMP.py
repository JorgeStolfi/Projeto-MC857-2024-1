import html_bloco_grade_de_videos
import html_pag_generica
import html_bloco_dados_de_video
import html_elem_form
import obj_video

def gera(ses, vid_ids, ncols, erros):

  # Estas condições deveriam ser satisfeitas em chamadas do sistema:
  assert ses == None or isinstance(ses, obj_sessao.Classe), "sessão inválida"
  if ses != None: assert onj_sessao.aberta(ses), "sessão foi fechada"
  assert isinstance(vid_ids, list) or isinstance(vid_ids, tuple), "lista de vídeos inválida"
  assert isinstance(ncols, int) and ncols > 0, "número de colunas inválido"
  assert erros == None or isinstance(erros, list) or  isinstance(erros, tuple), "lista de erros inválida"
  
  ht_grade, mais_erros = html_bloco_grade_de_videos.gera(vid_ids)
  
  assert isinstance(mais_erros, list) or isinstance(mais_erros, tuple)
  erros = erros + mais_erros

  pag = html_pag_generica.gera(ses, ht_grade, erros)
  return pag
