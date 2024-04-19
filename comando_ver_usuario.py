import comando_ver_usuario_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP "ver_usuario".
  Esse comando é tipicamente emitido quando um usuário (mesmo não logado)
  quer examinar os atributos de um determinado usuário.
  
  O parâmetro {ses} é a sessão de login que emitiu o comando. Deve ser
  {None} (se quem pediu não está logado), ou uma objeto de tipo
  {obj_sessao.Classe}, atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário com um único campo
  com chave 'usuario', cujo valor é o identificador do usuário (um string
  no formato "U-{NNNNNNNN}").  Se for vazio, ou o valor for {None},
  supõe que é o dono da sessão {ses} (que nesse caso não pode ser {None}).
  
  Alguns campos, como 'email', só podem ser vistos por administradores
  ou pelo poprio usuário em questão.  O campo 'senha' nunca é exibido.
  
  Normalmente a função devolve uma página que exibe o usuario, criada
  por {html_pag_ver_usuario.gera}. Dependendo de quem pediu, a página
  pode ter botões para alterar os dados do usuário, e buscar vídeos,
  sessões, e comentários do usuário.
  
  Se o comando falhou (por exemplo, se o campo {cmd_args['usuario']}
  está faltando ou é {None}, ou o usuário indicado não existe), devolve a
  página principal do site com uma mensagem de erro.
  """
  return comando_ver_usuario_IMP.processa(ses, cmd_args)

