import html_pag_ver_conversa
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_comentario

def processa(ses, cmd_args):
  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"
  
  erros = [].copy()

  # Obtém o identificador do vídeo ou comentário a ver:
  id_vid = cmd_args['video'] if 'video' in cmd_args else None
  id_com = cmd_args['comentario'] if 'comentario' in cmd_args else None
  
  if id_vid == None and id_com == None:
    erros.append("O identificador do veo ou comentário raiz não foi especificado")
  elif id_vid != None and id_com != None:
    erros.append("Apenas uma raiz deve ser especificada 'video' ou 'comentario'")
  
  if len_erros == 0:
    if id_vid != None:
      vid = obj_video.obtem_objeto(id_vid)
      if vid == None:
        erros.append(f"O vídeo {id_vid} não existe")
      else
        titulo = f"Comentários do vídeo {id_vid}"
        raizes = obj_video.busca_por_campos({'video': vid, 'pai': None })
    elif id_com != None:
      com = obj_comentario.obtem_objeto(id_com)
      if com == None:
        erros.append(f"O comentario {id_com} não existe")
      else
        titulo = f"Respostas ao comentário {id_com}"
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
