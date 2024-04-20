import comando_alterar_comentario_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o usuário aperta o botão "Confirmar alterações"
  (ou equivalente) em um formulário para editar dados de um comentário {com}, 
  após ter preenchido os campos do mesmo.  Veja html_form_alterar_comentario.gera}.
  Os novos dados do comentário com eventuais alterações devem estar definidos
  no dicionário {cmd_args}.   
  
  O parâmetro {ses} não pode ser {None} e deve ser um objeto de tipo
  {obj_sessao.Class}. (VV). A sessão deve estar aberta. (V)  O dicionário {cmd_args}
  deve ter um campo 'comentario' não nulo, cujo valor é o identificador do
  comentário {com} a alterar. (V)
  (V)
  
  Por enquanto o único campo que pode ser alterado é o 'texto'
  do comentário, e só se o dono da sessão {ses} for um 'administrador' 
  ou o autor do comentário {com}.
  
  Se os dados forem aceitáveis, a função altera o comentário {com} na
  base de dado; e retorna outra página mostrando os dados do
  comentário, para o usuário conferir. Veja
  {html_pag_ver_comentario.gera}.

  Se os dados não forem aceitáveis, a função devolve outra vez uma
  página com o formulário de alterar comentário, porém com os mesmos dados
  {cmd_args} e mais uma ou mais mensagens de erro adequadas."""
  return comando_alterar_comentario_IMP.processa(ses, cmd_args)
