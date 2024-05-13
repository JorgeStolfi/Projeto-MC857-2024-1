import html_form_login_IMP

def gera():
  """Retorna um formulário HTML (elemento "<form>...</form>")
  para o usuário fazer login. O formulário terá campos editáveis
  onde o usuário deverá digitar o email e a senha.
  
  O formulário também terá um botão 'Entrar' (de tipo 'submit').
  Quando o usuário clicar esse botão, será emitido um comando POST
  com ação {fazer_login}.  Os argumentos desse
  POST serão { 'email': {email}, 'senha': {senha} }."""
  return html_form_login_IMP.gera()
