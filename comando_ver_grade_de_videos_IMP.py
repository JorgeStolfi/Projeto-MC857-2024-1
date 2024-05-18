import html_pag_grade_de_videos 
import obj_sessao
import obj_video

def processa(ses, cmd_args):
    
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []

  if len(erros) == 0:
    ncols = 4  # Colunas da grade.
    nlins = 3  # Linhas da grade.
    nvids = ncols*nlins  # Total de videos na grade.

    ordem = int(cmd_args.pop('ordem')) if len(cmd_args) > 0 else 0

    vid_ids = obj_video.obtem_amostra(nvids, ordem)

    pag = html_pag_grade_de_videos.gera(ses, vid_ids, ncols, None)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  
  return pag
