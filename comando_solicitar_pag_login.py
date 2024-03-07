# Este módulo processa o acionamento do botão "Entrar" (login) do menu principla pelo usuário.

import comando_solicitar_pag_login_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Entrar" (login) 
  no menu geral de uma página qualquer.  
  
  A sessão corrente {ses} e o dicionário de argumentos {args}
  são irrelevantes e podem ser {None}.
  
  A função retorna a página HTML {pag}, com o formulário para o usuário fazer login
  (com campos "email" e "senha", e um botão de sumbissão "Entrar")."""
  return comando_solicitar_pag_login_IMP.processa(ses, args)

