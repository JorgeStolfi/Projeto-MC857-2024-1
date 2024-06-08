import comando_buscar_usuarios_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o usuário aperta o botão "Buscar" em
  uma formulário de busca de usuários (vide
  {html_form_buscar_usuarios.gera}). Ela procura na base de dados os
  usuários cujos atributos casam 
  os dados especificados em {cmd_args}. 
  
  O resultado será uma página com a lista dos usuários encontrados, em
  forma resumida. Vide {html_bloco_lista_de_usuarios.gera}.
  
  O parâmetro {ses} deve ser {None} (indicando que o leitor não está
  logado) ou o objeto {obj_sessao.Classe} de uma sessão.
  
  O parâmetro {cmd_args} deve ser um dicionário que contém os parâmetros
  da busca, que o usuário preencheu no formulário. Devem ser um
  subconjunto dos atributos de um objeto usuário ({obj_usuario.Classe})
  --- por exemplo, {{'nome': "João", 'email': "joao@email.com"}},
  excluindo 'senha' e 'administrador'. O dicionário {cmd_args} pode ter também um
  campo 'usuario' com o ID de um usuário específico, por exemplo
  {{'usuario': "U-00001234"}}.
  
  Atributos de {obj_usuario.Classe} que tem valor {None} em
  {cmd_args} (ou estão omitidos) serão ignorados na busca.
  
  No casos dos campos 'usuario', 'email', 'vnota' e 'data', a busca será feita
  pelo valor exato. Nos caso do campo 'nome', será feita uma busca por
  valor aproximado. Especificamente, será usado o operador SQL "LIKE"
  com argumento "%{nm}%" onde {nm} é o valor de {cmd_args['nome']}
  Quaisquer caracteres "%" e "_" em {nm} serão interpretados como nesse
  operador SQL. A busca vai ignorar a distinção maiúsculas e minúsculas.

  Se houver erros nos argumentos, ou a busca não encontrar nenhum usuário,
  devolve o formulário de buscar usuários com os campos {cmd_args}
  preenchidos, mais os avisos de erro.
  """
  return comando_buscar_usuarios_IMP.processa(ses, cmd_args)
