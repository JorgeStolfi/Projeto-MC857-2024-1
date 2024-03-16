import comando_fazer_login_IMP

def processa(ses, dados):
  """Esta função é chamada quando o usuário (que não deve estar cadastrado) 
  aperta o botão "Entrar" no formulário de login.  Recebe no dicionário {dados}
  os campos 'email' e 'senha' que o usuário preencheu nesse formulário. 
  Deve criar uma nova uma sessão para esse usuário, com um novo cookie; 
  e devolver a página de entrada.
  
  ATENÇÃO: esta função também devolve a nova sessão {ses_nova},
  que pode ser {ses} se o login falhou."""
  return comando_fazer_login_IMP.processa(ses, dados)
