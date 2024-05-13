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
  autor_id = None # For now, redefined if exists.
  if ses == None:
    erros.append("Não pode postar sem fazer login")
  elif not obj_sessao.aberta(ses):
    erros.append("Sessão de login já foi encerrada")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
    autor = ses_dono
    autor_id = obj_usuario.obtem_identificador(ses_dono)
    
  # Determina o vídeo e possivelmente o comentário pai:
  vid_id = cmd_args.get('video', None)
  pai_id = cmd_args.get('pai', None)
  pai_vid_id = None # For now, redefined if exists.
  
  if pai_id == None and vid_id == None:
    erros.append("Nem o vídeo nem o comentário pai foram especificados")
  else:
    # Valida {vid_id,pai_id}:
    if pai_id != None:
      pai = obj_comentario.obtem_objeto(pai_id)
      if pai == None:
        erros.append(f"O comentário {pai_id} não existe")
      else:
        pai_vid = obj_comentario.obtem_atributo(pai, 'video')
        assert pai_vid != None
        pai_vid_id = obj_video.obtem_identificador(pai_vid)
        if vid_id == None:
          vid_id = pai_vid_id 

    if vid_id != None:
      vid = obj_video.obtem_objeto(vid_id)
      if vid == None:
        erros.append(f"O vídeo {vid_id} não existe")

    if pai_vid_id != None and vid_id != None and pai_vid_id != vid_id:
      erros.append(f"O comentário {pai_id} é do vídeo {pai_vid_id} e não de {vid_id}")
    
  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    assert autor_id != None
    assert vid_id != None
    atrs = { 'autor': autor_id, 'video': vid_id }
    if pai_id != None: atrs['pai'] = pai_id
    pag = html_pag_postar_comentario.gera(ses, atrs, None)
  return pag

