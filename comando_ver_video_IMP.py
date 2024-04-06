
# Interfaces do projeto usadas por esta implementação:
import html_elem_video
import html_pag_ver_video
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_video

def processa(ses, cmd_args):
  assert ses != None
  assert obj_sessao.aberta(ses)
  assert obj_sessao.eh_administrador(ses)

  video_id = obj_video.busca_por_campo('titulo', cmd_args['titulo'])
  pag = html_pag_ver_video.gera(ses, video_id, None)
  return pag
