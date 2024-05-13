import html_pag_alterar_video
import html_pag_mensagem_de_erro
import obj_sessao
import obj_video
import obj_usuario
from util_erros import erro_prog

def processa(ses, cmd_args):
  erros = []

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    vid_id = cmd_args['video'] if 'video' in cmd_args else None

    vid = obj_video.obtem_objeto(vid_id)
    if vid == None:
      erros.append(f"O vídeo {vid_id} não existe")
    else:
      atrs_vid = obj_video.obtem_atributos(vid)
      autor_vid = atrs_vid['autor']
      autor_vid_id = obj_usuario.obtem_identificador(autor_vid)

      if (ses == None):
        erros.append("Você precisa logar para editar o vídeo.")
        pag = html_pag_mensagem_de_erro.gera(ses, erros)
        return pag

      admin = obj_sessao.de_administrador(ses);
      usr_ses = obj_sessao.obtem_dono(ses)
      usr_id = obj_usuario.obtem_identificador(usr_ses)

      if (not admin or (autor_vid_id != usr_id)):
        erros.append("Usuário não tem permissão para editar o vídeo escolhido.")

      if (len(erros) > 0):
        pag = html_pag_mensagem_de_erro.gera(ses, erros)
      else:
        pag = html_pag_alterar_video.gera(ses, vid_id, {}, None)

      return pag
    
