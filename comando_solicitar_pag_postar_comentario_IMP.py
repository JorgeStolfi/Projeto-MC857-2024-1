import html_pag_postar_comentario

def processa(ses, cmd_args):
  erros = [ ].copy()
  erros.append("!!! O comando 'alterar_video' ainda não foi implementado !!!")

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    id_vid = cmd_args['video'] if 'video' in cmd_args else None
    id_pai = cmd_args['pai'] if 'pai' in cmd_args else None
    pag = html_pag_postar_comentario.gera(ses, id_vid, id_pai, {}, None)
  return pag
    
