import html_elem_video
import html_pag_ver_video
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_video

def processa(ses, cmd_args):
  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"
  
  erros = [].copy()

  # Obtém o vídeo {vid}:
  id_vid = cmd_args['video'] if 'video' in cmd_args else None
  if 'video' == None:
    erros.append("O identificador do vídeo não foi especificado")
    vid = None
  else:
    vid = obj_video.obtem_objeto(id_vid)
    if vid == None:
      erros.append(f"O vídeo {id_vid} não existe")
  
  if vid == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_ver_video.gera(ses, vid, erros)
  return pag
