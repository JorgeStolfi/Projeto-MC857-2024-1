import comando_ver_sessoes_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando um usuário aperta o botão "Ver sessões"

  Se {cmd_args} possui um campo 'id_usuario' então a página mostra da lista de sessões deste usuário.
  Do contrário, mostra as sessões do usuário da sessão {ses}.

  A função retorna uma página HTML com a lista resumida das sessões."""
  return comando_ver_sessoes_IMP.processa(ses, cmd_args)

def extrai_titulo(ht_conteudo):
  """Dado {ht_conteudo} como um conteudo em HTML, extrai o título da página
  a partir da tag <title></title>, com auxilio do BeautifulSoup."""
  return comando_ver_sessoes_IMP.extrai_titulo(ht_conteudo)
