import html_pag_postar_comentario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_video
import obj_usuario
import obj_comentario

def processa(ses, cmd_args):
  
  # Validação de tipos (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert cmd_args != None and isinstance(cmd_args, dict)

  erros = []
  
  # Valida a sessão do usuário, define o autor:
  autor = None # For now, redefined if exists.
  autor_id = None # For now, redefined if exists.
  if ses == None:
    erros.append("É preciso estar logado para executar esta ação")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para executar esta ação")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
    autor = ses_dono
    autor_id = obj_usuario.obtem_identificador(ses_dono)
    
  # Determina o vídeo e possivelmente o comentário comentario:
  vid_id = cmd_args.pop('video', None)
  comentario_id = cmd_args.pop('comentario', None)
  comentario_vid_id = None # For now, redefined if exists.
  if comentario_id == None and vid_id == None:
    erros.append("Nem o vídeo nem o comentário comentario foram especificados")
  else:
    # Valida {vid_id,comentario_id}:
    if comentario_id != None:
      comentario = obj_comentario.obtem_objeto(comentario_id)
      if comentario == None:
        erros.append(f"O comentário \"{comentario_id}\" não existe")
      else:
        comentario_vid = obj_comentario.obtem_atributo(comentario, 'video')
        assert comentario_vid != None
        comentario_vid_id = obj_video.obtem_identificador(comentario_vid)
        if vid_id == None:
          vid_id = comentario_vid_id 

    if vid_id != None:
      vid = obj_video.obtem_objeto(vid_id)
      if vid == None:
        erros.append(f"O vídeo \"{vid_id}\" não existe")

    if comentario_vid_id != None and vid_id != None and comentario_vid_id != vid_id:
      erros.append(f"O comentário \"{comentario_id}\" é do vídeo \"{comentario_vid_id}\" e não de \"{vid_id}\"")
    
  assert len(cmd_args) == 0, f"Argumentos espúrios \"{cmd_args}\""

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    assert autor_id != None
    assert vid_id != None
    atrs = { 'autor': autor_id, 'video': vid_id }
    if comentario_id != None: atrs['pai'] = comentario_id
    pag = html_pag_postar_comentario.gera(ses, atrs, None)
  return pag

