import comando_ver_sessoes_IMP

def processa(ses, args):
  """Esta função é chamada quando um usuário aperta o botão "Ver sessões"

  Se {args} possui um {id} então a página mostra da lista de sessões deste usuário.
  Do contrário, mostra as sessões do usuário da sessão {ses}.

  A função retorna uma página HTML com a lista de sessões."""
  return comando_ver_sessoes_IMP.processa(ses, args)
