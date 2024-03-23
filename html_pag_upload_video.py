import html_form_upload_video_IMP

def gera(ses, cmd_args):
  """Retorna o HTML do formulário "<form>...</form>" para o usuário fazer upload de um video.
  O formulário contém campos editáveis onde o usuário deverá digitar
  o nome do arquivo (a escolher na máquina do usuário)
  e o título do arquivo. A página deve ter também um 
  botão 'Entrar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Entrar', será emitido um comando POST
  com ação {fazer_upload_video}.  Os argumentos desse
  POST são { 'email': {email}, 'senha': {senha} }."""
  return html_form_upload_video_IMP.gera(ses)
