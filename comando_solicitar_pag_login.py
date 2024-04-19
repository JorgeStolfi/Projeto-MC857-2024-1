# Este módulo processa o acionamento do botão "Entrar" (login) do menu principla pelo usuário.

import comando_solicitar_pag_login_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o servidor recebe um comando HTTP
  "solicitar_pag_login".  Tipicamente esse comando é emitido pelo
  browser do usuário qando este aperta o botão "Entrar" (login) 
  no menu geral de uma página qualquer.  
  
  O parâmetro {ses} será a sessão de login corrente, que emitiu o 
  comando.  Deve ser {None}, indicando que quem pediu não está logado.
  
  O parâmetro {cmd_args} será um dicionário com os argumentos do comando.
  Atualmente deve ser um dicionário vazio, ou {None}.
  
  A função retorna a página HTML {pag}, com o formulário para o usuário fazer login.
  Veja {html_pag_login.gera}."""
  return comando_solicitar_pag_login_IMP.processa(ses, cmd_args)

