import comando_alterar_usuario_IMP


def processa(ses, cmd_args):
  """
  Esta função é chamada quando alguém aperta o botão "Confirmar
  alterações" (ou equivalente) em um formulário para alterar os dados de
  um usuário {usr}, após ter preenchido os campos do mesmo. Veja
  {html_form_criar_alterar_usuario.gera}. Os dados do usuário com as
  alterações devem estar definidos no dicionário {cmd_args}.
  
  O parâmetro {ses} não pode ser {None} e deve ser um objeto de tipo
  {obj_sessao.Class}. A sessão deve estar aberta. Se {cmd_args} tiver um campo 'usuario'
  não nulo, este campo deve ser o identificador do usuário {usr} a alterar. Caso
  contrário, o usuário {usr} a alterar será o próprio dono da sessão {ses}.
  
  O dicionário {cmd_args} deve incluir um campo 'senha' com valor não
  nulo, e um campo 'conf_senha' com o mesmo valor.
  
  O campo 'administrador' só pode ser alterado se o dono da sessão {ses}
  for um administrador. Todos os demais campos, exceto o índice (e
  identificador), podem ser alterados se o dono de {ses} for um
  administrador ou o próprio usuário {usr}.
  
  Se os dados forem aceitáveis, a função altera o usuário {usr}, na base
  de dado; e retorna outra página que exibe os atributos do objeto {usr}
  depois da alteração, para o usuário conferir. Veja
  {html_pag_ver_usuario.gera}.

  Se os dados não forem aceitáveis, a função devolve outra vez uma
  página com o formulário de alterar usuário, porém com os mesmos dados
  {cmd_args} e mais uma ou mais mensagens de erro adequadas.
  """
  return comando_alterar_usuario_IMP.processa(ses, cmd_args)
