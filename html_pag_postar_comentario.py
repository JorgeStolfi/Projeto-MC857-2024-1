import html_pag_postar_comentario_IMP

def gera(ses, atrs, erros):
  """
  Retorna uma página HTML que inclui o formulário "<form>...</form>"
  para o usuário postar um novo comentario. O formulário contém alguns campos
  editáveis a serem preenhidos pelo usuário.

  O parâmetro {ses} deve ser a sessão de login que pediu esta página.
  Deve ser um objeto de tipo {obj_sessao.Classe}, atualmente aberta.
  Não pode ser {None}.
  
  Se {atrs} não for {None}, deve ser um dicionário que define valores
  iniciais (default) para alguns ou todos os atributos do novo
  comentário. Deve incluir obrigatoriamente pelo menos um dos atributos
  'video' e 'pai'. Não deve incluir atributos que serão definidos
  internamente quando o comentário for armazenado no banco de dados,
  como 'data'. Atributos cujo valor deveria ser um objeto podem estar
  representados em {atrs} pelos seus identificadores.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens
  (strings) a mostrar na página.

  O parâmetro {erros} é usado quando tentativa de fazer postar dá erro,
  e a pagina precisa ser exibida de novo com os valores dos campos que o
  usuário preencheu nessa tentativa. Neste caso, {erros} deve ser a
  lista das mensagens que explicam porque a tentativa falhou.
  
  A página terá também um botão "Postar" ou equivalente (de tipo
  'submit'). Quando o usuário clicar nesse botão, será emitido um
  comando POST com ação "postar_comentario". Os argumentos desse POST
  serão 'autor', 'video', 'pai', e 'texto' (o texto do comentário
  que consta no formulário).
  """
  return html_pag_postar_comentario_IMP.gera(ses, atrs, erros)
