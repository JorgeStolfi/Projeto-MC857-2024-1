import html_pag_grade_de_videos 
import obj_sessao
import obj_video

def processa(ses, cmd_args):
    
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []

  assert len(cmd_args) == 0, f"Argumentos espúrios \"{cmd_args}\""

  if len(erros) == 0:
    ncols = 4  # Colunas da grade.
    nlins = 3  # Linhas da grade.
    nvids = ncols*nlins  # Total de videos na grade.

    vid_ids = obj_video.obtem_amostra(nvids)

    pag = html_pag_grade_de_videos.gera(ses, vid_ids, ncols, None)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  
  return pag
