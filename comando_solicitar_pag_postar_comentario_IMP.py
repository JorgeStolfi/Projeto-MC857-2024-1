import html_pag_postar_comentario
import html_pag_mensagem_de_erro

def processa(ses, cmd_args):
  erros = [ ].copy()

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    id_vid = cmd_args['video'] if 'video' in cmd_args else None
    id_pai = cmd_args['pai'] if 'pai' in cmd_args else None
    id_autor = cmd_args['autor'] if 'autor' in cmd_args else None

    attrs = {"autor": id_autor,
             "pai":id_pai ,
             "video":id_vid }
    pag = html_pag_postar_comentario.gera(ses, attrs, erros)
  return pag
    
