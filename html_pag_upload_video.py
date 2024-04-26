import html_pag_upload_video_IMP

def gera(ses, atrs, erros):
  """
  Retorna uma página HTML que inclui o formulário "<form>...</form>"
  para o usuário fazer upload de um video. O formulário contém campos
  editáveis onde o usuário deverá digitar o nome do arquivo (a escolher
  na máquina do usuário) e o título do arquivo. A página deve ter também
  um botão 'Enviar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Enviar', será emitido um comando POST
  com ação {fazer_upload_video}.  Os argumentos desse
  POST serão 'titulo' (o título) e 'conteudo' (o conteúdo do arquivo).
  
  O parâmetro {atrs} deve ser um dict que opcionalmente especifica
  valores inicial para o campo 'titulo'.  O parâmetro
  {erros} deve ser {None} ou uma lista de mensagens (strings) a mostrar
  na página.

  Os parâmetros {atrs} e {erros} são usados quando tentativa de fazer
  upload dá erro, e a pagina precisa ser exibida de novo com os valores
  dos campos que o usuário preencheu anteriormente. Neste caso, {erros}
  deve ser a lista das mensagens referentes a essa tentativa.
  """
  return html_pag_upload_video_IMP.gera(ses, atrs, erros)
