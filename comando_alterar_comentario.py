import comando_alterar_comentario_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o usuário aperta o botão "Confirmar alterações"
  (ou equivalente) em um formulário para editar dados de um comentário {com}, 
  após ter preenchido os campos do mesmo.  Veja {html_pag_alterar_comentario.gera}.
  
  O parâmetro {ses} não pode ser {None} e deve ser um objeto de tipo
  {obj_sessao.Class}. A sessão deve estar aberta.  
  
  O parâmetro {cmd_args} deve ser um dicionário contendo um campo 'comentario'
  cujo valor é o identificador do comentário {com} a alterar, mais um subconjunto
  dos atributos de um comentário (vide {obj_comentario.Classe}) com valores
  que devem substituir os atualmente válidos no objeto {com}. 
  
  Por enquanto o único atributo que pode ser alterado é o 'texto'
  do comentário, e só se o dono da sessão {ses} for um administrador 
  ou o autor do comentário {com}.  Os atributos que não podem ser
  alterados, se estiverem no dicionário {cmd_args}, devm ter
  os valores atuais no objeto.
  
  Se os dados forem aceitáveis, a função altera o comentário {com} na
  base de dados, e retorna outra página mostrando os dados do
  comentário, para o usuário conferir. Veja
  {html_pag_ver_comentario.gera}.

  Se os dados não forem aceitáveis, a função devolve outra vez uma
  página com o formulário de alterar comentário, porém com os mesmos dados
  {cmd_args} e mais uma ou mais mensagens de erro adequadas."""
  return comando_alterar_comentario_IMP.processa(ses, cmd_args)
