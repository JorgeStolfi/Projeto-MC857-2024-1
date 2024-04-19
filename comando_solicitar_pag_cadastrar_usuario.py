import comando_solicitar_pag_cadastrar_usuario_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o servidor do site recebe um comando HTTP
  "solicitar_pag_cadastrar_usuario".  Tipicamnte esse comando é emitido pelo
  browser do usuário quando o este aperta o botão "Cadastrar"
  no menu geral de uma página qualquer. Devolve uma página que permite
  especificar os dados do novo usuário.
  
  A função retorna uma página HTML {pag} contendo o formulário para definir um
  os atributos do novo usuário, e um botão de sumbissão "Cadastrar".
  
  O parãmetro {ses} é a sessão de login corrente, que emitiu o comando.
  Pode ser {None}, indicando que o usuário que pediu não estava logado.
  Se não for {None}, deve ser um objeto de tipo {obj_sessao.Classe}, e deve estar
  aberta.
  
  O parâmetro {cmd_args} deve ser dicionário com os argumentos do comando 
  de argumentos. Atualmente deve ser vazio.
  
  Normalmente o resultado é uma página criada por {html_pag_cadastrar_usuario.gera}.
  Essa página contém um formulário onde o usuário corrente pode preencher os dados
  do novo usuário. A página também inclui um botão "Cadastrar" que 
  emite o comando "cadastrar_usuario"."""
  return comando_solicitar_pag_cadastrar_usuario_IMP.processa(ses, cmd_args)

