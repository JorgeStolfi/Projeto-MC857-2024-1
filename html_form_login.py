import html_form_login_IMP

def gera():
  """Retorna o HTML do formulário "<form>...</form>" para o usuário fazer login.
  O formulário contém campos editáveis onde o usuário deverá digitar
  o email e a senha, e um botão 'Entrar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Entrar', será emitido um comando POST
  com ação {fazer_login}.  Os argumentos desse
  POST são { 'email': {email}, 'senha': {senha} }."""
  return html_form_login_IMP.gera()
