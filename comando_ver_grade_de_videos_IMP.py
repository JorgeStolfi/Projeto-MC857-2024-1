import html_pag_grade_de_videos 
import obj_sessao
import obj_video

def processa(ses, cmd_args):
    
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []

  chave_de_ordenacao = 'nota'
  ordem = 0

  ordenacao = cmd_args.pop('ordem', None)

  if ordenacao is not None:
    ordem = -1 if ordenacao[0] == '-' else 1
    chave_de_ordenacao = ordenacao[1:]
  
  assert len(cmd_args) == 0, f"argumentos inválidos = {cmd_args}"

  ncols = 4  # Colunas da grade.
  nlins = 5  # Linhas da grade.
  nvids = ncols*nlins  # Total de células na grade.

  vid_ids = obj_video.obtem_amostra(nvids)
  vid_ids = obj_video.ordena_identificadores(vid_ids, chave_de_ordenacao, ordem)
      
  if len(erros) == 0:
    pag = html_pag_grade_de_videos.gera(ses, vid_ids, ncols, None)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  
  return pag
