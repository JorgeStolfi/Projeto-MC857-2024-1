import html_pag_alterar_video
import html_pag_mensagem_de_erro
import obj_sessao
import obj_video
from util_erros import erro_prog

def processa(ses, cmd_args):
  erros = [ ].copy()
  erros.append("!!! O comando 'solicitar_pag_alterar_video' ainda não foi implementado !!!")

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    id_vid = cmd_args['video'] if 'video' in cmd_args else None
    pag = html_pag_alterar_video.gera(ses, id_vid, {}, None)
  return pag
    
