# Este módulo processa o acionamento do botão "Fechar sessão" de uma página de "ver sessão". 

import comando_fechar_sessao_IMP

def processa(ses, args):
  """Esta função é chamada quando um administrador aperta o botão "Fechar sessão"
  durante a visualização de um objeto sessão.
  
  A sessão {ses} não pode ser {None}, e deve estar aberta. O dicionário
  {args} deve conter o campo 'id_sessao' com o ID da sessão a ser fechada.
  
  A função fecha a sessão cujo ID é args['id_sessao'] e retorna o HTML da página 
  principal (homepage) da loja. 

  Caso a sessão a ser fechada seja a sessão atual do usuário, redireciona pra homepage após encerrar."""
  return comando_fechar_sessao_IMP.processa(ses, args)
