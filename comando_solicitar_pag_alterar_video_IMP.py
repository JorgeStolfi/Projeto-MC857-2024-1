import html_pag_alterar_video
import html_pag_mensagem_de_erro
import obj_sessao
import obj_video
import obj_usuario
from util_erros import erro_prog

def processa(ses, cmd_args):
  erros = [ ].copy()

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    id_vid = cmd_args['video'] if 'video' in cmd_args else None

    vid = obj_video.busca_por_identificador(id_vid)
    if vid == None:
      erros.append(f"O vídeo {id_vid} não existe")
    else:
      atrs_vid = obj_video.obtem_atributos(vid)
      autor_vid = atrs_vid['autor']
      autor_vid_id = obj_usuario.obtem_identificador(autor_vid)

      if (ses == None):
        erros.append("Você precisa logar para editar o vídeo.")
        pag = html_pag_mensagem_de_erro.gera(ses, erros)
        return pag

      admin = obj_sessao.de_administrador(ses);
      usr_ses = obj_sessao.obtem_usuario(ses)
      id_usr = obj_usuario.obtem_identificador(usr_ses)

      if (not admin or (autor_vid_id != id_usr)):
        erros.append("Usuário não tem permissão para editar o vídeo escolhido.")

      if (len(erros) > 0):
        pag = html_pag_mensagem_de_erro.gera(ses, erros)
      else:
        pag = html_pag_alterar_video.gera(ses, id_vid, {}, None)

      return pag
    
