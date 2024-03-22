import comando_ver_sessao_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando um usuário aperta o botão "Ver sessões"

  Se {cmd_args} possui um campo 'id_usuario' então a página mostra da lista de sessões deste usuário.
  Do contrário, mostra as sessões do usuário da sessão {ses}, como em 
  {comando_ver_sessoes}.

  A função retorna uma página HTML com a lista resumida de sessões."""
  return comando_ver_sessao_IMP.processa(ses, cmd_args)
