import html_pag_postar_comentario_IMP

def gera(ses, atrs, erros):
  """
  Retorna uma página HTML que inclui o formulário "<form>...</form>"
  para o usuário fazer postar de um comentario. O formulário contém alguns campos
  editáveis a serem preenhidos pelo usuário.

  O parâmetro {ses} deve ser a sessão de login que pediu esta página.
  Não deve ser {None} e deve ser um objeto de tipo {obj_sessao.Classe}
  aberta.
  
  O parâmetro {atrs} deve ser um dict que especifica os 
  valores dos campos não-editáveis ('autor', 'pai', 'video')
  e opcionalmente o valor inicial para o campo 'texto'.
  Não deve especificar a 'data'.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens
  (strings) a mostrar na página.

  Os parâmetros {atrs} e {erros} são usados quando tentativa de fazer
  postar dá erro, e a pagina precisa ser exibida de novo com os valores
  dos campos que o usuário preencheu anteriormente. Neste caso, {erros}
  deve ser a lista das mensagens referentes a essa tentativa. 
  
  A página terá também um botão "Postar" ou equivalente (de tipo
  'submit'). Quando o usuário clicar nesse botão, será emitido um
  comando POST com ação "postar_comentario". Os argumentos desse POST
  serão 'autor', 'pai', 'video', e 'texto' (o texto do comentário).
  """
  return html_pag_postar_comentario.gera(ses, atrs, erros)
