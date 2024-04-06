import comando_ver_videos_de_usuario_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando um usuário aperta o botão "Ver meus vídeos"
  ou "Ver videos" de algum usuário.

  Se {cmd_args} possui um campo 'id_usuario' então a página mostra da lista
  de vídeos deste usuário. Do contrário, mostra os vídeos do usuário da sessão {ses}.

  A função retorna uma página HTML com a lista resumida dos vídeos."""
  return comando_ver_videos_de_usuario_IMP.processa(ses, cmd_args)
