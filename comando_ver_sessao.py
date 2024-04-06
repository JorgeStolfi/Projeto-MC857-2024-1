import comando_ver_sessao_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando um usuário aperta o botão "Ver sessão"
  ou similar.

  Se {cmd_args} possui um campo 'id_sessao' então a página mostra essa sessão.
  Do contrário, mostra a sessão corrente {ses}. 
  
  A sessão corrente {ses} não deve ser {None} e deve estar aberta. Se o dono de {ses}
  não for administrador, a sessão a ver deve pertencer ao mesmo usuário.

  A função retorna uma página HTML com os dados da sessão {ses_a_ver} e um botão "Fechar" que
  fecha essa sessão."""
  return comando_ver_sessao_IMP.processa(ses, cmd_args)
