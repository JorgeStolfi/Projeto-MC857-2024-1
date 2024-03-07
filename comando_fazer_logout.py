# Este módulo processa o acionamento do botão "Sair" do menu geral pelo usuário. 

import comando_fazer_logout_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Sair" (logout)
  no menu geral de uma página da loja.
  
  A sessão {ses} não pode ser {None}, e deve estar aberta.  O dicionário
  {args} é ignorado, e deveria ser vazio.
  
  A função fecha a sessão corrente {ses} dada e retorna o HTML da página 
  principal (homepage) da loja. 
  
  ATENÇÃO: retorna também a nova sessão, geralmente {None}."""
  return comando_fazer_logout_IMP.processa(ses, args)
