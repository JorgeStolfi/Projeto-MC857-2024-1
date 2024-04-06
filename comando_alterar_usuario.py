import comando_alterar_usuario_IMP


def processa(ses, cmd_args):
  """Esta função é chamada quando alguém aperta o botão "Alterar"
  em um formulário para alterar os dados de um usuário {usr}, 
  após ter preenchido os campos do mesmo.  Os novos dados do usuário 
  (possivelmente não alterados) devem estar definidos
  no dicionário {cmd_args}. 

  O parâmetro {ses} não pode ser {None} e deve ser um objeto de tipo
  {obj_sessao.Class}. A sessão deve estar aberta. Se o dono da sessão
  {ses} for um administrador e {cmd_args} tiver um campo 'id_usuario'
  não nulo, este campo define o usuário {usr} a alterar. Caso
  contrário, o usuário {usr} será o próprio dono da sessão {ses}.

  O dicionário {cmd_args} deve incluir um campo 'senha' com valor não
  nulo, e um campo 'conf_senha' com o mesmo valor.

  Se os dados forem aceitáveis, a função altera o usuário {usr}, na
  base de dado; e retorna outra página com o formulário de alteração, com os 
  campos alterados, para o uusário conferir.

  Se os dados não forem aceitáveis, a função devolve o mesmo
  formulário de alterar usuário, com os mesmos dados nos campos
  preenchidos, com uma ou mais mensagens de erro adequadas."""
  return comando_alterar_usuario_IMP.processa(ses, cmd_args)
