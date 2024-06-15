import html_pag_grade_de_videos 
import obj_sessao
import obj_video
import sys

def processa(ses, cmd_args):
    
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []
  
  arg_ordem = cmd_args.pop('ordem', None)
  arg_catalogo = cmd_args.pop('catalogo', None)

  # valores default
  chave_de_ordenacao = 'nota' 
  ordem = 0

  if arg_ordem is not None:
    operator = arg_ordem[0]
    chave_de_ordenacao = arg_ordem[1:]

    if arg_ordem[0] == '+':
      ordem = +1
    elif arg_ordem[0] == '-':
      ordem = -1
    else:
      ordem = 0
    chave_de_ordenacao = arg_ordem[1:]
  
  assert len(cmd_args) == 0, f"argumentos inválidos = {cmd_args}"

  ncols = 4  # Colunas da grade.
  nlins = 5  # Linhas da grade.
  nvids = ncols*nlins  # Total de células na grade.

  vid_ids = obj_video.obtem_amostra(nvids)
  vid_ids = obj_video.ordena_identificadores(vid_ids, chave_de_ordenacao, ordem)
      
  if len(erros) == 0:
    pag = html_pag_grade_de_videos.gera(ses, vid_ids, ncols, arg_catalogo, None)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  
  return pag
