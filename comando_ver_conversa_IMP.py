import html_pag_ver_conversa
import html_pag_mensagem_de_erro
import obj_sessao
import obj_video
import obj_comentario
import obj_video

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []

  # Obtém o identificador do vídeo ou comentário a ver:
  vid_id = cmd_args.pop('video', None)
  com_id = cmd_args.pop('comentario', None)
  max_coms = cmd_args.pop('max_coms', 100)
  max_nivels = cmd_args.pop('max_nivels', 100)
  
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
        raizes = obj_comentario.busca_por_video(vid_id, {False})
    
    elif com_id != None:
      com = obj_comentario.obtem_objeto(com_id)
      
      if com == None:
        erros.append(f"O comentario \"{com_id}\" não existe")
      
      else:
        raizes = obj_comentario.busca_por_campo('pai', com)
        
        if len(raizes) > 0:
          titulo =  f"Respostas ao comentário {com_id}" 
        
        else:
          titulo = f"Não há respostas ao comentário {com_id}"
    
    else:
      # Não deveria passar aqui:
      assert False
      
  if len(erros) == 0:
    flor = obj_comentario.obtem_conversa(raizes, max_coms, max_nivels)
    pag = html_pag_ver_conversa.gera(ses, titulo, flor, erros)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  return pag
