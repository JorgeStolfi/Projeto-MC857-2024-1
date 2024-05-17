import html_pag_ver_conversa
import html_pag_mensagem_de_erro
import obj_sessao
import obj_video
import obj_comentario

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []

  # Obtém o identificador do vídeo ou comentário a ver:
  vid_id = cmd_args.pop('video', None)
  com_id = cmd_args.pop('comentario', None)
  
  if vid_id == None and com_id == None:
    erros.append("O identificador do video ou comentário raiz não foi especificado")
  elif vid_id != None and com_id != None:
    erros.append("Apenas uma raiz deve ser especificada 'video' ou 'comentario'")
  
  if len(erros) == 0:
    if vid_id != None:
      vid = obj_video.obtem_objeto(vid_id)
      if vid == None:
        erros.append(f"O vídeo \"{vid_id}\" não existe")
      else:
        titulo = f"Comentários do vídeo {vid_id}"
        raizes = obj_video.busca_por_campos({'video': vid, 'pai': None }, unico = False)
    elif com_id != None:
      com = obj_comentario.obtem_objeto(com_id)
      if com == None:
        erros.append(f"O comentario \"{com_id}\" não existe")
      else:
        titulo = f"Respostas ao comentário {com_id}"
        raizes = obj_comentario.busca_por_campo('pai', com)
    else:
      # Não deveria passar aqui:
      assert False
      
  if len(erros) == 0:
    flor = obj_comentario.obtem_floresta(raizes)
    pag = html_pag_ver_conversa.gera(ses, titulo, flor, erros)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  return pag
