
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

  # voltar para página inicial se cmd_args['id'] não existir
  if 'id_usuario' in cmd_args:
    return html_pag_mensagem_de_erro.gera(ses, "Vídeo com id nulo não encontrado!")

  video_id = obj_video.busca_por_identificador(cmd_args['id']) #string no formato "NNNNNNNN"
  pag = html_pag_ver_video.gera(ses, video_id, None)
  return pag
