import html_pag_alterar_video
import html_pag_mensagem_de_erro
import obj_sessao
import obj_video
import obj_usuario
from util_erros import erro_prog, aviso_prog

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)

  erros = []

  if ses == None:
    erros.append("É preciso estar logado para efetuar esta ação")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi encerrada. É preciso estar logado para efetuar esta ação")
  else:
    vid_id = cmd_args.get('video', None)
    vid = obj_video.obtem_objeto(vid_id) if vid_id != None else None
    if vid == None:
      erros.append(f"O vídeo \"{vid_id}\" não existe")
    else:
      vid_atrs = obj_video.obtem_atributos(vid)
      vid_autor = vid_atrs['autor']
      assert vid_autor != None
      vid_autor_id = obj_usuario.obtem_identificador(vid_autor)

      ses_dono = obj_sessao.obtem_dono(ses)
      para_admin = obj_usuario.eh_administrador(ses_dono);
      ses_dono_id = obj_usuario.obtem_identificador(ses_dono)

      editavel = para_admin or (vid_autor_id == ses_dono_id)
      if not editavel:
        erros.append("Você não tem permissão para editar este vídeo")
    
  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_alterar_video.gera(ses, vid_id, vid_atrs, None)

  return pag
    
